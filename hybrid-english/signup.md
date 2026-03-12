---
layout: default
title: Sign Up
permalink: /signup/
---

<h1>Create Your Account</h1>

<form id="signupForm">
<input type="text" name="name" placeholder="Full Name" required>
<input type="email" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>

<button type="submit">Create Account</button>
</form>

<script>
document.getElementById("signupForm").addEventListener("submit", function(e){

e.preventDefault();

var data = new FormData(this);

fetch("YOUR_GOOGLE_SCRIPT_URL",{
method:"POST",
body:data
})
.then(res => res.text())
.then(data => {
window.location.href="/payment/";
})
})
</script>
