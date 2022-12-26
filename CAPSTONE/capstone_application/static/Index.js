//*******************************DomContentLoaded*********************************************
//          DomContentLoaded
//********************************************************************************************
document.addEventListener('DOMContentLoaded',function() {

    document.querySelector('div#Home-page.planets').style.display = 'block';
    document.querySelector('div#Mercury-page.planets').style.display = 'none';
    document.querySelector('div#Venus-page.planets').style.display = 'none';
    document.querySelector('div#Earth-page.planets').style.display = 'none';
    document.querySelector('div#Mars-page.planets').style.display = 'none';

   // Select all buttons
   document.querySelectorAll('button.planets-button').forEach(button => {

    // When a button is clicked, switch to that page
    button.onclick = function() {
        showPage(this.dataset.page);
    }
})

    let i = 0;
    // select all canvas
    document.querySelectorAll('canvas').forEach( canvas =>{
        i++;
        //enumerate each canvas
        canvas.setAttribute('id',`${i}`)
    })
//**********************************load planets *********************************************
//          DomContentLoaded

    // fetch('https://api.le-systeme-solaire.net/rest/bodies/{soleil}')
    // .then(response => response.json())
    // .then(data=>{
    //     document.querySelector('a#mercury').addEventListener('click', () => Mercury());
    // });
    // Load Mercury page
    // document.querySelector('a#mercury').addEventListener('click', () => Mercury());
    // Load Venus page
    // document.querySelector('a#venus').addEventListener('click', () => Venus());
    // Load Earth page
    // document.querySelector('a#earth').addEventListener('click', () => Earth());
    // Load Mars page
    // document.querySelector('a#mars').addEventListener('click', () => Mars());
    // Load Jupiter page
    // document.querySelector('a#jupiter').addEventListener('click', () => Jupiter());
    // Load Saturn page
    // document.querySelector('a#saturn').addEventListener('click', () => Saturn());
    // Load Uranus page
    // document.querySelector('a#uranus').addEventListener('click', () => Uranus());
    // Load Neptune page
    // document.querySelector('a#neptune').addEventListener('click', () => Neptune());
//********************************************************************************************
});
function showPage(page) {
    // Hide all of the divs:
    document.querySelectorAll('div.planets').forEach(div => {
        div.style.display = 'none';
    });

    // Show the div provided in the argument
    document.querySelector(`div#${page}.planets`).style.display = 'block';
    document.querySelector('canvas#2').style.display = 'block';
}
// function that'll hide the canvas and only show the correct one depending on the button pushed.
function showCanvas(num){

}
//****************************Login/Logout/Home/Register***************************************
//          Login/Logout/Home/Register
// // Login
// function Login(){
//     // allow people to fill out form to login
//     console.log("made it to the Login page")
// }
// // Sign out
// function Logout(){
//     // allow people to sign out from website
//     console.log("made it to the Sign out page")
// }
// // navigate through home page
// function Home(){
//     console.log("made it to the Home")
// }
// // Register
// function Register(){
//     // allow people to fill out form to register
//     console.log("made it to the Register page")
// }
//********************************************************************************************
//********************************************************************************************
//          Planets
//********************************************************************************************
// Mercury
function Mercury(){
    
    document.getElementById('description-mercury').innerHTML = data.EnglishName;
    console.log(data)
};
// Venus
function Venus(){
    // allow people to sign out from website
    console.log("made it to the Mercury page")
}
// Earth
function Earth(){
    // allow people to sign out from website
    console.log("made it to the Earth page")
}
// Mars
function Mars(){
    // allow people to sign out from website
    console.log("made it to the Mars page")
}
// Jupiter
function Jupiter(){
    // allow people to sign out from website
    console.log("made it to the Jupiter page")
}
// Saturn
function Saturn(){
    // allow people to sign out from website
    console.log("made it to the Saturn page")
}
// Uranus
function Uranus(){
    // allow people to sign out from website
    console.log("made it to the Uranus page")
}
// Neptune
function Neptune(){
    // allow people to sign out from website
    console.log("made it to the Neptune page")
}
