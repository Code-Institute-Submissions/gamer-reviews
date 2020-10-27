function preventEmptyString() {
  let inputs = document.getElementsByClassName('form-control').value;
  
  if (event.which === 32 && event.target.selectionStart === 0) {
    event.preventDefault();
    alert("Error! Can't start with space.");
    return false;
  }
}
