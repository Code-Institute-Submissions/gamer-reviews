function regFormValidation() {
    let name = document.getElementById('username-reg');
    let pass = document.getElementById('password-reg');
    
    name.addEventListener('keypress', function(event) {
        if (event.which === 32 && event.target.selectionStart === 0) {
            event.preventDefault();
        }
    });
    
    pass.addEventListener('keypress', function(event) {
       if (event.which === 32 && event.target.selectionStart === 0) {
           event.preventDefault();
       }
    });
}
