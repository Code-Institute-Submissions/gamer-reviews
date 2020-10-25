function loginFormValidation() {
    let name = document.getElementById('usernameLogin');
    let pass = document.getElementById('passwordLogin');
    
    name.addEventListener('keypress', function(event) {
        let key = event.keyCode;
        if (key === 32) {
            event.preventDefault();
        }
    });
    
    pass.addEventListener('keypress', function(event) {
       let key = event.keyCode;
       if (key === 32) {
           event.preventDefault();
       }
    });
}
