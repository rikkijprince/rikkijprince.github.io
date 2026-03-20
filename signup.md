---
layout: default
title: Sign Up
description: "Sign up to Hybrid English 5.0"
keywords: "subscribe, signup, Hybrid English"
permalink: /signup/
---
<!-- Google Search Console verification -->
<meta name="google-site-verification" content="9DOZpcg5hHHOQJJdTX8Qtb0kxCDqbQHfnVktEjjZdO4" />

<!-- Author Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Rikki J Prince",
  "jobTitle": "Author",
  "url": "https://www.rikkijprince.com",
  "sameAs": [
    "https://www.amazon.com/author/rikkijprince",
    "https://linkedin.com/in/rikki-jaffar-prince-53a5a729"
  ]
}
</script>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q8PEN408E6"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-Q8PEN408E6');
</script>


<h1>Create Your Account</h1>

<form id="signupForm">
  <label for="email">Email</label><br />
  <input id="email" name="email" type="email" autocomplete="email" required /><br /><br />

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
    return await supabaseClient.auth.signUp({ email, password });
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
