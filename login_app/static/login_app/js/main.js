let loginBtn= document.getElementById("loginBtn");
let signinBtn= document.getElementById("signinBtn");
let nameField= document.getElementById("nameField");
let title= document.getElementById("title");

signinBtn.onclick=function(){
    // nameField.style.maxHeight='0'; //hide  name field
    loginBtn.classList.add("disable");
    // signinBtn.classList.remove("disable") //disable sign up button when we click on sign in button
}
loginBtn.onclick=function(){
    nameField.style.maxHeight='60px'; //hide  name field
    loginBtn.classList.remove("disable");
    signinBtn.classList.add("disable") //disable sign up button when we click on sign in button
}
