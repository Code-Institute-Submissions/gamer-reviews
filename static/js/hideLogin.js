// function that hides login button when user is logged in 
// and hides logout button when user isnt signed in
function hideLogin() {
    let logged = document.getElementById("logged-in").textContent;
    let loginButton = document.getElementById("login-register");
    let logout = document.getElementById("logout");
    
    if (logged === '' ) {
        loginButton.style.display = 'flex';
        logout.style.display = 'none';
    } else {
        loginButton.style.display = 'none';
        logout.style.display = 'flex';
    }
}
