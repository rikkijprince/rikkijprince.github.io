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

const msg = document.getElementById("message");

function show(text, color="black") {

  msg.style.color = color;
  msg.innerHTML += "<br>" + text;

  console.log(text);
}

show("Page loaded.");


// -------------------------------------------------
// CHECK SUPABASE LIBRARY
// -------------------------------------------------

if (!window.supabase) {

  show("❌ Supabase library failed to load.", "red");

} else {

  show("✅ Supabase library loaded.", "green");
}


// -------------------------------------------------
// CONFIG
// -------------------------------------------------

const SUPABASE_URL =
  "https://ernxbalkjqrlngnumsuh.supabase.co";

const SUPABASE_ANON_KEY =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVybnhiYWxranFybG5nbnVtc3VoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM2MDg0NjIsImV4cCI6MjA4OTE4NDQ2Mn0.qDnHmgHRfYv_mcLj-JTmI6IT31zo2W2g8RFD3BRb4DU";


// -------------------------------------------------
// CREATE CLIENT
// -------------------------------------------------

let supabase;

try {

  supabase =
    window.supabase.createClient(
      SUPABASE_URL,
      SUPABASE_ANON_KEY
    );

  show("✅ Supabase client created.", "green");

}

catch(err) {

  show(
    "❌ Client creation failed: " + err.message,
    "red"
  );
}


// -------------------------------------------------
// BUTTON
// -------------------------------------------------

const button =
  document.getElementById("signupButton");


button.addEventListener("click", async () => {

  show("Button clicked.");

  try {

    const email =
      document.getElementById("email").value.trim();

    const password =
      document.getElementById("password").value;

    show("Attempting signup...");
    show("Email = " + email);

    const result =
      await supabase.auth.signUp({

        email,
        password

      });

    show("Signup request completed.");

    console.log(result);

    if (result.error) {

      show(
        "❌ Signup error: " +
        result.error.message,
        "red"
      );

      return;
    }

    show("✅ Signup succeeded.", "green");


    // -------------------------------------------------
    // PROFILE INSERT
    // -------------------------------------------------

    const insertResult =
      await supabase
        .from("profiles")
        .insert([{

          id: result.data.user.id,

          full_name:
            document.getElementById("full_name").value,

          username:
            document.getElementById("username").value,

          phone:
            document.getElementById("phone").value

        }]);


    console.log(insertResult);

    if (insertResult.error) {

      show(
        "❌ Profile insert failed: " +
        insertResult.error.message,
        "red"
      );

      return;
    }

    show(
      "✅ Profile inserted successfully.",
      "green"
    );

  }

  catch(err) {

    console.error(err);

    show(
      "❌ Unexpected error: " + err.message,
      "red"
    );
  }

});

</script>
