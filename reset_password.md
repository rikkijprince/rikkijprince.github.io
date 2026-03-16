reset_password.md
---
layout: default
title: Reset Password
permalink: /reset_password/
---

<h1>Reset Password</h1>

<p>Enter your email and we will send a reset link.</p>

<input id="email" type="email" placeholder="Email">

<button onclick="resetPassword()">Send Reset Link</button>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>
<script src="/assets/js/auth.js"></script>
