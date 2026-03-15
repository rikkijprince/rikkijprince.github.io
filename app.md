const { data: { user } } = await supabase.auth.getUser()

if(!user){
window.location="/login/"
}
