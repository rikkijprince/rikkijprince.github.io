---
layout: default
title: Sign Up
permalink: /signup/
---
layout: default
title: Login
decription: "Log in to Hybrid English 5.0"
keywords: "login,, Hybrid English"
permalink: /login/
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

<h1>Create Your Account</h1>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>

<script>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
  const SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co";
  const SUPABASE_ANON_KEY = "sb_publishable_3G9E1jSXWZzEaEtKeIU6Sg_sxOKiTTB";

  const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
</script>

async function signUp(){

const email = document.getElementById("email").value
const password = document.getElementById("password").value

const { data, error } = await supabase.auth.signUp({
email: email,
password: password
})

if(!error){
window.location="/payment/"
}

}

</script>
