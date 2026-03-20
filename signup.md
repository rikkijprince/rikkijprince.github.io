---
layout: default
title: Sign Up
permalink: /signup/
---

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
