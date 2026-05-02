---
layout: default
title: Book a Fluency Coaching Session
permalink: /book_classes/
---

<style>
.booking-container {
  max-width: 720px;
  margin: 60px auto;
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}

.booking-title {
  font-size: 2rem;
  margin-bottom: 10px;
}

.booking-subtitle {
  color: #666;
  margin-bottom: 30px;
}

.slot {
  display: block;
  width: 100%;
  padding: 14px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
  cursor: pointer;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>

<div class="booking-container">

  <div class="booking-title">Book a Fluency Coaching Session</div>
  <div class="booking-subtitle">
    1:1 live tutorial session with native English speaker.
  </div>

  <p>
    <strong>Session:</strong>
    €<span id="price">—</span>
    · <span id="length">—</span> minutes
  </p>

  <div id="slots">
    <button class="slot">Loading slots...</button>
  </div>

  <div id="error" class="error"></div>

</div>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
const API_BASE = "https://hybrid-english-backend-1.onrender.com";

const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVybnhiYWxranFybG5nbnVtc3VoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM2MDg0NjIsImV4cCI6MjA4OTE4NDQ2Mn0.qDnHmgHRfYv_mcLj-JTmI6IT31zo2W2g8RFD3BRb4DU"; // keep as-is or move to env if needed

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

let currentUser = null;

// 🔐 AUTH CHECK
async function requireAuth() {
    const { data, error } = await supabase.auth.getUser();

    if (error || !data?.user) {
        document.getElementById("slots").innerHTML = `
          <div>
            First you need to log in (or sign up, if you haven't done so).<br><br>
            <a href="/login/" class="cta-button">Go to Login</a>
          </div>
        `;
        return false;
    }

    currentUser = data.user;
    return true;
}

// 🔥 LOAD PRICE
async function loadPrice() {
    try {
        const res = await fetch(`${API_BASE}/api/price`);
        const data = await res.json();

        document.getElementById("price").innerText = data.price_eur ?? "?";
        document.getElementById("length").innerText = data.session_length ?? "?";

    } catch (err) {
        console.error("Price load error:", err);
        document.getElementById("price").innerText = "?";
        document.getElementById("length").innerText = "?";
    }
}

// 🔥 LOAD SLOTS
async function loadSlots() {
    const container = document.getElementById("slots");

    try {
        const res = await fetch(`${API_BASE}/api/slots`);
        const slots = await res.json();

        container.innerHTML = "";

        if (!Array.isArray(slots) || slots.length === 0) {
            container.innerHTML = "<div>No slots available right now.</div>";
            return;
        }

        slots.forEach(slot => {
            const btn = document.createElement("button");
            btn.className = "slot";
            btn.innerText = slot.label;

            btn.onclick = () => bookSlot(slot, btn);

            container.appendChild(btn);
        });

    } catch (err) {
        console.error("Slots load error:", err);
        container.innerHTML = `
          <div>
            Could not load slots.<br><br>
            <button onclick="loadSlots()">Retry</button>
          </div>
        `;
    }
}

// 💳 BOOK SLOT
async function bookSlot(slot, btn) {
    const errorBox = document.getElementById("error");
    errorBox.innerText = "";

    btn.disabled = true;
    btn.innerText = "Processing...";

    try {
        const { data: sessionData } = await supabase.auth.getSession();

        if (!sessionData?.session?.access_token) {
            throw new Error("No session token");
        }

        const token = sessionData.session.access_token;

        const res = await fetch(`${API_BASE}/api/book`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({
                slot: slot.datetime
            })
        });

        const data = await res.json();

        if (data.error) {
            errorBox.innerText = data.error;
            btn.disabled = false;
            btn.innerText = slot.label;
            return;
        }

        window.location.href = data.checkout_url;

    } catch (err) {
        console.error("Booking error:", err);
        errorBox.innerText = "Something went wrong.";
        btn.disabled = false;
        btn.innerText = slot.label;
    }
}

// 🚀 INIT
async function init() {
    await loadPrice();
    const ok = await requireAuth();
    if (!ok) return;

    await loadSlots();
}

init();
</script>
