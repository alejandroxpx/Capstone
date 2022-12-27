//*******************************DomContentLoaded*********************************************
//          DomContentLoaded
//********************************************************************************************
document.addEventListener('DOMContentLoaded',function() {
    // Hide planets except home page at the start
    document.querySelector('div#Home.planets').style.display = 'block';
    document.querySelector('div#Mercury.planets').style.display = 'none';
    document.querySelector('div#Venus.planets').style.display = 'none';
    document.querySelector('div#Earth.planets').style.display = 'none';
    document.querySelector('div#Mars.planets').style.display = 'none';
    document.querySelector('div#Jupiter.planets').style.display = 'none';
    document.querySelector('div#Saturn.planets').style.display = 'none';
    document.querySelector('div#Uranus.planets').style.display = 'none';
    document.querySelector('div#Neptune.planets').style.display = 'none';
        
    let i = 0;
    // select all canvas and give it an id
    document.querySelectorAll('canvas').forEach( canvas =>{
        //enumerate each canvas
        canvas.setAttribute('id',`${i}`)
        i++;
    })
    // Hide planets except home page at the start
    document.getElementById('0').style.display = 'block';
    document.getElementById('1').style.display = 'none';
    document.getElementById('2').style.display = 'none';
    document.getElementById('3').style.display = 'none';
    document.getElementById('4').style.display = 'none';
    document.getElementById('5').style.display = 'none';
    document.getElementById('6').style.display = 'none';
    document.getElementById('7').style.display = 'none';
    document.getElementById('8').style.display = 'none';

   // Select all buttons
   document.querySelectorAll('button.planets-button').forEach(button => {

    // When a button is clicked, switch to that page
    button.onclick = function() {
        showPage(this.dataset.page);
        showCanvas(this.dataset.page);
    }
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
}
// function that'll hide the canvas and only show the correct one depending on the button pushed.
function showCanvas(page){
    let j = 0;
    const list = [0,1,2,3,4,5,6,7,8,9]
    const planet_arr = ["Home","Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"];
    let index = planet_arr.indexOf(`${page}`, list);
    document.querySelectorAll('canvas').forEach(canvas =>{
        // Hide all the canvas
        canvas.style.display = 'none';
    });
  
    // Show the canvas provided in the argument
    document.getElementById(`${index}`).style.display = 'block';

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
