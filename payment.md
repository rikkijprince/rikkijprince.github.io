---
layout: default
title: Your Account
permalink: /payment/
---

<h1>Your Account</h1>

<p id="authStatus"></p>
<button id="logoutBtn" class="cta-button" style="display:none;">Log out</button>

<hr />

<h2>Next Step</h2>

<p>
  You're ready to book your first 1-to-1 session.
</p>

<a class="cta-button" href="{{ '/book_classes/' | relative_url }}">
  Book a Session
</a>

<p id="message" style="margin-top:20px;"></p>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...";

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

async function init() {
  const { data } = await supabase.auth.getUser();
  const user = data?.user;

  const status = document.getElementById("authStatus");
  const logoutBtn = document.getElementById("logoutBtn");

  if (!user) {
    window.location.href = "{{ '/login/' | relative_url }}";
    return;
  }

  status.textContent = `Logged in as ${user.email}`;
  logoutBtn.style.display = "inline-block";
}

document.getElementById("logoutBtn").addEventListener("click", async () => {
  await supabase.auth.signOut();
  window.location.href = "{{ '/login/' | relative_url }}";
});

init();
</script>
