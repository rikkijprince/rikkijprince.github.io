---
layout: default
title: Login
permalink: /login/
---

<h1>Login</h1>

<form id="loginForm">
  <label>Email</label><br />
  <input id="email" type="email" required /><br /><br />

  <label>Password</label><br />
  <input id="password" type="password" required /><br /><br />

  <button type="submit">Log in</button>
</form>

<p id="message"></p>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
const SUPABASE_ANON_KEY = "YOUR_ANON_KEY";

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const msg = document.getElementById("message");
  msg.textContent = "Logging in...";

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password
  });

  if (error) {
    msg.textContent = "❌ " + error.message;
    return;
  }

  // ✅ Save session for booking page
  localStorage.setItem("user_session", JSON.stringify({
    email: data.user.email,
    id: data.user.id
  }));

  msg.textContent = "✅ Login successful. Redirecting...";

  setTimeout(() => {
    window.location.href = "/book_classes/";
  }, 800);
});
</script>

    // You said you want payment after login/signup:
    window.location.href = "{{ '/payment/' | relative_url }}";
  });
</script>
