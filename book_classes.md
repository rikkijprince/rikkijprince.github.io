# book_classes.md

---
layout: default
title: Book a Fluency Coaching Session
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
    1:1 session focused on clarity of thought, expression, and confidence in English.
  </div>

  <p><strong>Session price:</strong> €<span id="price">—</span></p>

  <!-- Instant UI (no blank state) -->
  <div id="slots">
    <button class="slot">Checking availability...</button>
    <button class="slot">Checking availability...</button>
    <button class="slot">Checking availability...</button>
  </div>

  <div id="error" class="error"></div>

</div>

<script>
const API_BASE = "https://your-api-url.com"; // 🔁 CHANGE THIS

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
        document.getElementById("price").innerText = data.fee;
    } catch {
        document.getElementById("price").innerText = "?";
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
                user: { name: "Guest User" }
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

// Init
loadPrice();
loadSlots();
</script>
