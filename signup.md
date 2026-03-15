---
layout: default
title: Sign Up
permalink: /signup/
---

<h1>Create Your Account</h1>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>

<script>

const supabase = supabase.createClient(
"https://ernxbalkjqrlngnumsuh.supabase.co",
"postgresql://postgres:omFwlD36wdxZBicm@db.ernxbalkjqrlngnumsuh.supabase.co:5432/postgres"
)

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
