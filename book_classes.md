---
layout: default
title: Book a Fluency Coaching Session
permalink: /book_classes/
---

<div class="booking-container">

  <h1>Book a Fluency Coaching Session</h1>

  <p>
    <strong>Session:</strong>
    €<span id="price">—</span> · <span id="length">—</span> minutes
  </p>

  <div id="slots">
    <button>Loading slots...</button>
  </div>

  <p id="error" style="color:red;"></p>

</div>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

<script>
const API_BASE = "https://hybrid-english-backend.onrender.com";

const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
const SUPABASE_ANON_KEY = "YOUR_ANON_KEY_HERE";

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

let currentUser = null;

// 🔐 Check login
async function requireAuth() {
    const { data } = await supabase.auth.getUser();
    currentUser = data?.user;

    if (!currentUser) {
        document.getElementById("slots").innerHTML = `
            <p>First you need to log in (or sign up, if you haven't done so).</p>
            <a href="/login/">Go to Login</a>
        `;
        return false;
    }

    return true;
}

// 💰 Load price
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

// 📅 Render slots
function renderSlots(slots) {
    const container = document.getElementById("slots");
    container.innerHTML = "";

    slots.forEach(slot => {
        const btn = document.createElement("button");
        btn.innerText = slot.label;

        btn.onclick = () => bookSlot(slot, btn);

        container.appendChild(btn);
    });
}

// 📡 Load slots
async function loadSlots() {
    try {
        const res = await fetch(`${API_BASE}/api/slots`);
        const slots = await res.json();

        renderSlots(slots);
    } catch {
        document.getElementById("slots").innerHTML = "Error loading slots.";
    }
}

// 💳 Book slot (SECURE VERSION)
async function bookSlot(slot, btn) {
    const errorBox = document.getElementById("error");
    errorBox.innerText = "";

    btn.disabled = true;
    btn.innerText = "Processing...";

    try {
        const { data: sessionData } = await supabase.auth.getSession();
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

    } catch {
        errorBox.innerText = "Something went wrong.";
        btn.disabled = false;
        btn.innerText = slot.label;
    }
}

// 🚀 Init
async function init() {
    const ok = await requireAuth();
    if (!ok) return;

    loadPrice();
    loadSlots();
}

init();
</script>
