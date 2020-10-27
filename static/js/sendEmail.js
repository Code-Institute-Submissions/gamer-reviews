// function that sends email from contact page using emailjs
function sendMail(contactForm) {
    emailjs.send("gmail", "gamer-review", {
        //values taken from contact form
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "subject": contactForm.subject.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            // message that pops up if email was sent 
            alert("Email sent!");
        },
        // message that pops up if email wasnt sent
        function(error) {
            alert("Email failed to send!");
        });
        resetForm();
        return false;
}

function resetForm() {
    document.getElementById('contact-form').reset();
}