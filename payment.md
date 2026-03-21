---
layout: default
title: Payment
description: "SProcess payments to Hybrid English 5.0"
keywords: "process payments, Hybrid English"
permalink: /payment/
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

<p id="authStatus"></p>
<button id="logoutBtn" class="cta-button" style="display:none;">Log out</button>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
  const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
  const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVybnhiYWxranFybG5nbnVtc3VoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM2MDg0NjIsImV4cCI6MjA4OTE4NDQ2Mn0.qDnHmgHRfYv_mcLj-JTmI6IT31zo2W2g8RFD3BRb4DU";
  const supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

  async function refreshAuthUI() {
    const { data } = await supabaseClient.auth.getUser();
    const user = data?.user;

    const status = document.getElementById("authStatus");
    const btn = document.getElementById("logoutBtn");

    if (user) {
      status.textContent = `Logged in as ${user.email}`;
      btn.style.display = "inline-block";
    } else {
      status.textContent = "Not logged in.";
      btn.style.display = "none";
    }
  }

  document.getElementById("logoutBtn").addEventListener("click", async () => {
    await supabaseClient.auth.signOut();
    window.location.href = "{{ '/login/' | relative_url }}";
  });

  refreshAuthUI();
</script>
<h1>Start Your Free Trial</h1>

<p>
  You have <strong>7 days</strong> to try Hybrid English 5.0 for free.
</p>
<p>
  After your trial, you’ll be charged <strong>€12.95/month</strong> to continue enhancing your fluency.
 </p>
<p> 
  You can <strong>cancel at anytime</strong>.
</p>

<hr />

<h2>Book a 1:1 Session</h2>
<p>
  You can book your first 30-minute session with your personal fluency coach using the link below.
 </p>
<p> 
  The fee is <strong€25</strong> per session.
</p>

<p>
  <a class="cta-button" href="https://calendly.com/rjpbusiness/30min" target="_blank" rel="noopener">
    Book your first session now.
  </a>
</p>

<h3>Schedule Inline</h3>
<div class="calendly-inline-widget"
     data-url="https://calendly.com/rjpbusiness/30min"
     style="min-width:320px;height:800px;"></div>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>
