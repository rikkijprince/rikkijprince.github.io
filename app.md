const { data: { user } } = await supabaseClient.auth.getUser()

if(!user){
window.location="/login/"
}

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>
<script src="/assets/js/auth.js"></script>

<script>
requireLogin()
</script>
