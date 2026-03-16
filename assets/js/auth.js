// Supabase connection
const supabaseClient = supabase.createClient(
  "https://ernxbalkjqrlngnumsuh.supabase.com",
  "omFwlD36wdxZBicm
);

// SIGN UP
async function signup(){

  const email = document.getElementById("email").value
  const password = document.getElementById("password").value

  const { data, error } = await supabaseClient.auth.signUp({
    email: email,
    password: password
  })

  if(!error){
    alert("Account created. Check your email for verification.")
    window.location="/login/"
  } else {
    alert(error.message)
  }
}


// LOGIN
async function login(){

  const email = document.getElementById("email").value
  const password = document.getElementById("password").value

  const { data, error } = await supabaseClient.auth.signInWithPassword({
    email: email,
    password: password
  })

  if(!error){
    window.location="/app/"
  } else {
    alert("Login failed")
  }

}


// PASSWORD RESET REQUEST
async function resetPassword(){

  const email = document.getElementById("email").value

  const { data, error } = await supabaseClient.auth.resetPasswordForEmail(email)

  if(!error){
    alert("Password reset email sent")
  } else {
    alert(error.message)
  }

}


// CHECK LOGIN STATUS
async function requireLogin(){

  const { data: { user } } = await supabaseClient.auth.getUser()

  if(!user){
    window.location="/login/"
  }

}
This single file now powers all authentication behaviour.
________________________________________
3. Login Page
login.md
---
layout: default
title: Login
permalink: /login/
---

<h1>Login</h1>

<input id="email" type="email" placeholder="Email">

<input id="password" type="password" placeholder="Password">

<button onclick="login()">Login</button>

<p>
<a href="/reset-password/">Forgot password?</a>
</p>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>
<script src="/assets/js/auth.js"></script>
