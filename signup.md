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
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVybnhiYWxranFybG5nbnVtc3VoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM2MDg0NjIsImV4cCI6MjA4OTE4NDQ2Mn0.qDnHmgHRfYv_mcLj-JTmI6IT31zo2W2g8RFD3BRb4DU";

const supabase =
  window.supabase.createClient(
    SUPABASE_URL,
    SUPABASE_ANON_KEY
  );

const form = document.getElementById("signupForm");
const msg = document.getElementById("message");

form.addEventListener("submit", async (e) => {

  e.preventDefault();

  msg.style.color = "black";
  msg.textContent = "Creating account...";

  const email =
    document.getElementById("email").value.trim();

  const password =
    document.getElementById("password").value;

  const full_name =
    document.getElementById("full_name").value.trim();

  const username =
    document.getElementById("username").value.trim();

  const phone =
    document.getElementById("phone").value.trim();

  try {

    console.log("Starting signup...");

    // -------------------------------------------------
    // SIGNUP
    // -------------------------------------------------

    const { data, error } =
      await supabase.auth.signUp({

        email,
        password,

        options: {
          emailRedirectTo:
            "https://www.rikkijprince.com/login/"
        }

      });

    console.log("Signup response:", data);

    if (error) {

      console.error("Signup error:", error);

      msg.style.color = "red";
      msg.textContent =
        "❌ Signup failed: " + error.message;

      setTimeout(() => {
        window.location.href = "/";
      }, 5000);

      return;
    }

    // -------------------------------------------------
    // PROFILE INSERT
    // -------------------------------------------------

    if (data.user) {

      const { error: profileError } =
        await supabase
          .from("profiles")
          .insert([{
            id: data.user.id,
            full_name,
            username,
            phone
          }]);

      if (profileError) {

        console.error(
          "Profile insert error:",
          profileError
        );

        msg.style.color = "red";
        msg.textContent =
          "❌ Account created, but profile save failed.";

        setTimeout(() => {
          window.location.href = "/";
        }, 5000);

        return;
      }
    }

    // -------------------------------------------------
    // SUCCESS
    // -------------------------------------------------

    msg.style.color = "green";
    msg.textContent =
      "✅ Account created successfully. Please check your email.";

    console.log("Signup completed successfully.");

    setTimeout(() => {
      window.location.href = "/";
    }, 5000);

  }

  catch (err) {

    console.error("Unexpected error:", err);

    msg.style.color = "red";
    msg.textContent =
      "❌ Unexpected error. Please try again.";

    setTimeout(() => {
      window.location.href = "/";
    }, 5000);
  }

});

</script>
