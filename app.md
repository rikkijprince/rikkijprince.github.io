---
layout: default
title: Hybrid English 5.0 App
description: "English fluency App: Hybrid English 5.0, fluency trainer"
keywords: "Hybrid English, app"
permalink: /app/
---

const { data: { user } } = await supabaseClient.auth.getUser()

if(!user){
window.location="/login/"
}

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>
<script src="/assets/js/auth.js"></script>

<script>
requireLogin()
</script>
