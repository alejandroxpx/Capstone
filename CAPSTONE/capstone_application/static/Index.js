document.addEventListener('DOMContentLoaded',function() {
    // Load Login page
    document.querySelector('#Login').addEventListener('click', () => Login());
    // Load Register page
    document.querySelector('#Register').addEventListener('click', () => Register());
    // Loaf sign out page
    document.querySelector('#Logout').addEventListener('click', () => Logout());
    // Load Home page
    document.querySelector('#Home').addEventListener('click', () => Home());
    // Load Lost page
    document.querySelector('#Lost').addEventListener('click', () => Lost());
    // Load Homeless page
    document.querySelector('#Homeless').addEventListener('click', () => Homeless());
    // Load Stories page
    document.querySelector('#Stories').addEventListener('click', () => Stories());
})
// navigate through home page
function Home(){
    console.log("made it to the Home")
    return false
}
// navigate through lost page
function Lost(){
    console.log("made it to the Lost tab")
}
// navigate through homeless page
function Homeless(){
    console.log("made it to the Homeless tab")
}
// navigate through stories page
function Stories(){
    console.log("made it to the Stories tab")  
}
// Login
function Login(){
    console.log("made it to the Login page")
    return false
}
// Register
function Register(){
    console.log("made it to the Register page")
    return false
}
// Sign out
function Logout(){
    console.log("made it to the Sign out page")
    return false
}