---
layout: default
title: Hybrid English 5.0 App
decription: "English fluency App: Hybrid English 5.0, fluency trainer"
keywords: "Hybrid English, app"
permalink: /app/
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
    "https://twitter.com/YOURPROFILE"
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

![Rikki J Prince](/assets/images/Family profile.webp){:style="max-width:200px;border-radius:50%;"}

const { data: { user } } = await supabaseClient.auth.getUser()

if(!user){
window.location="/login/"
}

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>
<script src="/assets/js/auth.js"></script>

<script>
requireLogin()
</script>
