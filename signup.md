---
layout: default
title: Sign Up
permalink: /signup/
---

<h1>Create Your Account</h1>

<form id="signupForm">
  <label>Full Name</label><br />
  <input id="full_name" required /><br /><br />

  <label>Username</label><br />
  <input id="username" required /><br /><br />

  <label>Email</label><br />
  <input id="email" type="email" required /><br /><br />

  <label>Phone</label><br />
  <input id="phone" required /><br /><br />

  <label>Password</label><br />
  <input id="password" type="password" required /><br /><br />

  <button type="submit">Create account</button>
</form>

<p id="message"></p>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
const SUPABASE_ANON_KEY = "YOUR_ANON_KEY";

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

document.getElementById("signupForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const msg = document.getElementById("message");
  msg.textContent = "Creating account...";

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  const full_name = document.getElementById("full_name").value;
  const username = document.getElementById("username").value;
  const phone = document.getElementById("phone").value;

  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: {
      emailRedirectTo: "https://www.rikkijprince.com/login/"
    }
  });

  if (error) {
    msg.textContent = "❌ " + error.message;
    return;
  }

  // Save profile (optional but recommended)
  if (data.user) {
    await supabase.from("profiles").insert([{
      id: data.user.id,
      full_name,
      username,
      phone
    }]);
  }

  msg.textContent = "✅ Account created. Check your email to confirm.";
});
</script>
}
</script>
