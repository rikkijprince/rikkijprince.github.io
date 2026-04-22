# backend/modules/booking/calendar_service.py

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os.path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# =========================
# CONFIGURATION
# =========================

SCOPES = ['https://www.googleapis.com/auth/calendar']

# Calendars to check for conflicts
CALENDAR_IDS = [
    "rjpbusiness@gmail.com",  # booking calendar
    "rjpxpr@gmail.com"        # personal calendar
]

# Calendar where bookings are CREATED
BOOKING_CALENDAR_ID = "rjpbusiness@gmail.com"

# Time settings
TIMEZONE = ZoneInfo("Europe/Madrid")

SLOT_DURATION = 40  # minutes
BUFFER_MINUTES = 10
WORK_START_HOUR = 9
WORK_END_HOUR = 18
DAYS_AHEAD = 7


# =========================
# AUTHENTICATION
# =========================

def get_calendar_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)


# =========================
# BUSY TIMES (MULTI-CALENDAR)
# =========================

def get_busy_times(service, time_min, time_max):
    body = {
        "timeMin": time_min.isoformat(),
        "timeMax": time_max.isoformat(),
        "items": [{"id": cal_id} for cal_id in CALENDAR_IDS]
    }

    result = service.freebusy().query(body=body).execute()

    busy_times = []

    for cal_id in CALENDAR_IDS:
        for b in result['calendars'][cal_id]['busy']:
            busy_times.append((
                datetime.fromisoformat(b['start']),
                datetime.fromisoformat(b['end'])
            ))

    return busy_times


# =========================
# SLOT GENERATION ENGINE
# =========================

def get_available_slots():
    service = get_calendar_service()

    now = datetime.now(TIMEZONE)
    MIN_NOTICE_HOURS = 12
    cutoff = now + timedelta(hours=MIN_NOTICE_HOURS)
    end_window = now + timedelta(days=DAYS_AHEAD)

    busy_times = get_busy_times(service, now, end_window)

    slots = []
    current_day = now

    while current_day < end_window:

        day_start = current_day.replace(
            hour=WORK_START_HOUR, minute=0, second=0, microsecond=0
        )

        day_end = current_day.replace(
            hour=WORK_END_HOUR, minute=0, second=0, microsecond=0
        )

        current_slot = day_start

        while current_slot + timedelta(minutes=SLOT_DURATION) <= day_end:

            slot_end = current_slot + timedelta(minutes=SLOT_DURATION)

            # Check overlap
            overlap = False
            for busy_start, busy_end in busy_times:
                if not (slot_end <= busy_start or current_slot >= busy_end):
                    overlap = True
                    break

            if not overlap and current_slot > cutoff:
                slots.append(current_slot)

            current_slot += timedelta(
                minutes=SLOT_DURATION + BUFFER_MINUTES
            )

        current_day += timedelta(days=1)

    return slots


# =========================
# FORMAT FOR DISPLAY
# =========================

def format_slots(slots, state):
    formatted = []

    tz_str = getattr(state, "user_timezone", "UTC")

    try:
        user_tz = ZoneInfo(tz_str)
    except:
        user_tz = ZoneInfo("UTC")

    for i, slot in enumerate(slots):
        # Convert to user's local time
        local_slot = slot.astimezone(user_tz)

        label = local_slot.strftime("%a %d %b | %H:%M")

        formatted.append({
            "index": i + 1,
            "label": label,
            "datetime": slot,              # original (Madrid) → keep!
            "local_datetime": local_slot   # optional but useful
        })

    return formatted

def display_slots(formatted_slots, state):
    from zoneinfo import ZoneInfo

    print("\n--- Available Slots ---\n")

    tz_str = getattr(state, "user_timezone", "UTC")

    try:
        tz = ZoneInfo(tz_str)
        tz_label = tz.key.split("/")[-1].replace("_", " ")
    except:
        tz_label = "Local time"

    print(f"Times shown in: {tz_label}\n")

    current_day = None

    for slot in formatted_slots:
        day = slot["local_datetime"].strftime("%A %d %B")

        if day != current_day:
            current_day = day
            print(f"\n{day}")
            print("-" * len(day))

        print(f"{slot['index']:>2}. {slot['label']}")
        
        
# =========================
# EVENT CREATION (TENTATIVE)
# =========================

def create_tentative_event(user, start_time):
    service = get_calendar_service()

    end_time = start_time + timedelta(minutes=SLOT_DURATION)

    event = {
        'summary': f"Fluency Session - {user['username']}",
        'description': "Pending payment",
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Europe/Madrid'
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Europe/Madrid'
        },
        'status': 'tentative'
    }

    event = service.events().insert(
        calendarId=BOOKING_CALENDAR_ID,
        body=event
    ).execute()

    return event['id']


# =========================
# CONFIRM EVENT
# =========================

def confirm_event(event_id):
    service = get_calendar_service()

    event = service.events().get(
        calendarId=BOOKING_CALENDAR_ID,
        eventId=event_id
    ).execute()

    event['status'] = 'confirmed'
    event['description'] = "Paid and confirmed"

    service.events().update(
        calendarId=BOOKING_CALENDAR_ID,
        eventId=event_id,
        body=event
    ).execute()


# =========================
# CANCEL EVENT
# =========================

def cancel_event(event_id):
    service = get_calendar_service()

    service.events().delete(
        calendarId=BOOKING_CALENDAR_ID,
        eventId=event_id
    ).execute()


# ===============================
# SAFETY CHECK (ANTI DOUBLE-BOOK)
# ===============================

def is_slot_still_available(start_time):
    service = get_calendar_service()

    end_time = start_time + timedelta(minutes=SLOT_DURATION)

    busy_times = get_busy_times(service, start_time, end_time)

    for busy_start, busy_end in busy_times:
        if not (end_time <= busy_start or start_time >= busy_end):
            return False

    return True
