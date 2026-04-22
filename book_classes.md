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
  border-color: #aaa;
}

.loading {
  color: #888;
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

  <div id="slots" class="loading">Loading available slots...</div>

  <div id="error" class="error"></div>

</div>

<script>
const API_BASE = "https://your-api-url.com"; // 🔁 replace this

async function loadSlots() {
    try {
        const res = await fetch(`${API_BASE}/api/slots`);
        const slots = await res.json();

        const container = document.getElementById("slots");
        container.innerHTML = "";

        if (!slots.length) {
            container.innerHTML = "No available sessions this week.";
            return;
        }

        slots.forEach(slot => {
            const btn = document.createElement("button");
            btn.className = "slot";
            btn.innerText = slot.label;

            btn.onclick = () => bookSlot(slot);

            container.appendChild(btn);
        });

    } catch (err) {
        document.getElementById("slots").innerText = "Failed to load slots.";
    }
}

async function loadPrice() {
    try {
        const res = await fetch(`${API_BASE}/api/price`);
        const data = await res.json();
        document.getElementById("price").innerText = data.fee;
    } catch {
        document.getElementById("price").innerText = "?";
    }
}

async function bookSlot(slot) {
    const errorBox = document.getElementById("error");
    errorBox.innerText = "";

    try {
        const res = await fetch(`${API_BASE}/api/book`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                slot: slot.datetime,
                user: {
                    name: "Guest User"
                }
            })
        });

        const data = await res.json();

        if (data.error) {
            errorBox.innerText = data.error;
            return;
        }

        // Redirect to Stripe Checkout
        window.location.href = data.checkout_url;

    } catch (err) {
        errorBox.innerText = "Something went wrong. Please try again.";
    }
}

loadPrice();
loadSlots();
</script>
