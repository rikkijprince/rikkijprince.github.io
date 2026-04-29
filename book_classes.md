---
layout: default
title: Book a Fluency Coaching Session
permalink: /book_classes/
---

const API_BASE = "https://hybrid-english-backend.onrender.com";

const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...";

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

let currentUser = null;

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
  transition: all 0.2s ease;
}

.slot:hover {
  background: #f5f5f5;
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

  <!-- Instant UI (no blank state) -->
  <div id="slots">
    <button class="slot">Checking availability...</button>
    <button class="slot">Checking availability...</button>
    <button class="slot">Checking availability...</button>
  </div>

  <div id="error" class="error"></div>

</div>

<script>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

// 🔐 Check if user is logged in
  
const userSession = localStorage.getItem("user_session");

if (!userSession) {
    alert("Please log in to book a session.");
    window.location.href = "/login/";
}
  
const API_BASE = "https://hybrid-english-backend.onrender.com";

// 🔥 1. Warm up backend immediately
fetch(`${API_BASE}/api/slots`).catch(() => {});

// 🔥 2. Load cached slots instantly (if available)
function renderSlots(slots) {
    const container = document.getElementById("slots");
    container.innerHTML = "";

    slots.forEach(slot => {
        const btn = document.createElement("button");
        btn.className = "slot";
        btn.innerText = slot.label;

        btn.onclick = () => bookSlot(slot, btn);

        container.appendChild(btn);
    });
}

const cached = localStorage.getItem("slots_cache");
if (cached) {
    try {
        renderSlots(JSON.parse(cached));
    } catch {}
}

// 🔥 3. Load fresh slots with timeout protection
async function loadSlots() {
    const container = document.getElementById("slots");

    const timeout = new Promise((_, reject) =>
        setTimeout(() => reject("timeout"), 4000)
    );

    try {
        const res = await Promise.race([
            fetch(`${API_BASE}/api/slots`),
            timeout
        ]);

        const slots = await res.json();

        localStorage.setItem("slots_cache", JSON.stringify(slots));

        renderSlots(slots);

    } catch {
        container.innerHTML = `
          <div>
            Still waking things up…<br><br>
            <button onclick="loadSlots()">Try again</button>
          </div>
        `;
    }
}

// 🔥 4. Load price
async function loadPrice() {
    try {
        const res = await fetch(`${API_BASE}/api/price`);
        const data = await res.json();

        document.getElementById("price").innerText = data.price_eur;
        document.getElementById("length").innerText = data.session_length;

    } catch {
        document.getElementById("price").innerText = "?";
        document.getElementById("length").innerText = "?";
    }
}

// 🔥 5. Booking flow
async function bookSlot(slot, btn) {
    const errorBox = document.getElementById("error");
    errorBox.innerText = "";

    // Prevent double clicks
    btn.disabled = true;
    btn.innerText = "Processing...";

    try {
        const res = await fetch(`${API_BASE}/api/book`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                slot: slot.datetime,
                const user = JSON.parse(userSession);
                user: {
                  name: currentUser.email
                }
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

    } catch {
        errorBox.innerText = "Something went wrong.";
        btn.disabled = false;
        btn.innerText = slot.label;
    }
async function requireAuth() {
    const { data } = await supabase.auth.getUser();
    currentUser = data?.user;

    if (!currentUser) {
        document.getElementById("slots").innerHTML = `
          <div>
            First you need to log in (or sign up, if you haven't done so).<br><br>
            <a href="/login/" class="cta-button">Go to Login</a>
          </div>
        `;
        return false;
    }

    return true;
}
}

// Init
async function init() {
    const isLoggedIn = await requireAuth();
    if (!isLoggedIn) return;

    loadPrice();
    loadSlots();
}

init();
</script>
