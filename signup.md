---
layout: default
title: Sign Up
description: "Sign up to Hybrid English 5.0"
keywords: "subscribe, signup, Hybrid English"
permalink: /signup/
---

<h1>Create Your Account</h1>

<form id="signupForm">
  <label for="full_name">Full Name</label><br />
  <input id="full_name" full_name="full_name" type="full_name" autocomplete="full_name" required /><br /><br />

  <label for="username">Username</label><br />
  <input id="username" name="username" type="username" autocomplete="username" required /><br /><br />

  <label for="email">Email</label><br />
  <input id="email" name="email" type="email" autocomplete="email" required /><br /><br />

  <label for="phone">Phone (include country code)</label><br />
  <input id="phone" name="phone" type="phone" autocomplete="phone" required /><br /><br />

  <label for="password">Password</label><br />
  <input id="password" name="password" type="password" autocomplete="new-password" required /><br /><br />

  <button type="submit" class="cta-button">Create account</button>
</form>

<p id="message" style="margin-top:12px;"></p>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
  const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
  const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVybnhiYWxranFybG5nbnVtc3VoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM2MDg0NjIsImV4cCI6MjA4OTE4NDQ2Mn0.qDnHmgHRfYv_mcLj-JTmI6IT31zo2W2g8RFD3BRb4DU";

  const supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

  async function signUp(email, password) {
    return await supabaseClient.auth.signUp({
  full-name,
  username,
  email,
  phone,
  password,
  options: {
    emailRedirectTo: "https://rikkijprince.com/login/"
    }
  });
  }

  document.getElementById("signupForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const msg = document.getElementById("message");
    msg.textContent = "Creating account...";

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    const { data, error } = await signUp(email, password);

    if (error) {
      msg.textContent = error.message;
      return;
    }

    // Redirect after signup
    window.location.href = "{{ '/payment/' | relative_url }}";
  });
</script>
