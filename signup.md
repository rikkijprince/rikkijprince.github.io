---
layout: default
title: Sign Up
permalink: /signup/
---

<h1>Create Your Account</h1>

<form id="signupForm" onsubmit="return false;">

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

  <button id="signupButton" type="button">
    Create account
  </button>

</form>

<p id="message"></p>


<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

<script>

const SUPABASE_URL =
  "https://ernxbalkjqrlngnumsuh.supabase.co";

const SUPABASE_ANON_KEY =
  "YOUR_REAL_SUPABASE_ANON_KEY";

const supabase =
  window.supabase.createClient(
    SUPABASE_URL,
    SUPABASE_ANON_KEY
  );

const button =
  document.getElementById("signupButton");

const msg =
  document.getElementById("message");


button.addEventListener("click", async () => {

  msg.style.color = "black";
  msg.textContent = "Creating account...";

  try {

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

    console.log("Attempting signup...");

    // -------------------------------------------------
    // AUTH SIGNUP
    // -------------------------------------------------

    const response =
      await supabase.auth.signUp({

        email,
        password,

        options: {
          emailRedirectTo:
            "https://www.rikkijprince.com/login/"
        }

      });

    console.log(response);

    const data = response.data;
    const error = response.error;

    // -------------------------------------------------
    // HANDLE AUTH ERROR
    // -------------------------------------------------

    if (error) {

      console.error(error);

      msg.style.color = "red";

      msg.textContent =
        "❌ Signup failed: " + error.message;

      setTimeout(() => {
        window.location.href = "/";
      }, 5000);

      return;
    }

    // -------------------------------------------------
    // INSERT PROFILE
    // -------------------------------------------------

    if (data.user) {

      const profileResponse =
        await supabase
          .from("profiles")
          .insert([{
            id: data.user.id,
            full_name,
            username,
            phone
          }]);

      console.log(profileResponse);

      if (profileResponse.error) {

        console.error(profileResponse.error);

        msg.style.color = "red";

        msg.textContent =
          "❌ Profile save failed.";

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
      "✅ Signup successful. Please check your email.";

    setTimeout(() => {
      window.location.href = "/";
    }, 5000);

  }

  catch (err) {

    console.error("Unexpected error:", err);

    msg.style.color = "red";

    msg.textContent =
      "❌ Unexpected error. Check browser console.";

    setTimeout(() => {
      window.location.href = "/";
    }, 5000);
  }

});

</script>
</script>
