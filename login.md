async function login(){

const email = document.getElementById("email").value
const password = document.getElementById("password").value

const { data, error } = await supabase.auth.signInWithPassword({
email: email,
password: password
})

if(!error){
window.location="/app/"
}

}
