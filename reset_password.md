reset_password.md
---
layout: default
title: Reset Password
permalink: /reset_password/
---
---
layout: default
title: Hybrid English 5.0
description: "Hybrid English 5.0 landing page"
keywords: "subscribe, signup, Hybrid English, English fluency enhancer, fluency trainer"
permalink: /hybrid_english/
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


<h1>Reset Password</h1>

<p>Enter your email and we will send a reset link.</p>

<input id="email" type="email" placeholder="Email">

<button onclick="resetPassword()">Send Reset Link</button>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>
<script src="/assets/js/auth.js"></script>
