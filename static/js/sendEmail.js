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
        function(error) {
            // message that pops up if email wasnt sent
            alert("Email failed to send!");
        });
        return false;
}