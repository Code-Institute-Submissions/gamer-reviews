function regFormValidation() {
    let name = document.getElementById('username-reg');
    let pass = document.getElementById('password-reg');
    
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
