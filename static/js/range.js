var slider1;
var slider2;
var slider3;
var slider4;

// function that gets gameplay rating
function rangeVal() {
    slider1 = document.getElementById("myRange-1");
    var output = document.getElementById("range-1");
    output.innerHTML = slider1.value;
    //function that displays rating score 
    slider1.oninput = function() {
        output.innerHTML = this.value;
    };
}

// function that gets story rating
function rangeVal1() {
    slider2 = document.getElementById("myRange-2");
    var output = document.getElementById("range-2");
    output.innerHTML = slider2.value;
    //function that displays rating score 
    slider2.oninput = function() {
        output.innerHTML = this.value;
    };
}

// function that gets production-quality rating
function rangeVal2() {
    slider3 = document.getElementById("myRange-3");
    var output = document.getElementById("range-3");
    output.innerHTML = slider3.value;
    //function that displays rating score 
    slider3.oninput = function() {
        output.innerHTML = this.value;
    };
}

// function that gets price rating
function rangeVal3() {
    slider4 = document.getElementById("myRange-4");
    var output = document.getElementById("range-4");
    output.innerHTML = slider4.value;
    //function that displays rating score 
    slider4.oninput = function() {
        output.innerHTML = this.value;
    };
}

// function that gets total rating
function getTotal() {
    slider1 = document.getElementById('myRange-1').value;
    slider2 = document.getElementById('myRange-2').value;
    slider3 = document.getElementById('myRange-3').value;
    slider4 = document.getElementById('myRange-4').value;
    
    //variable that stores total score
    let total = Number(slider1) + Number(slider2) + Number(slider3) + + Number(slider4);
    //variable that stores avg rating
    let avgTotal = total/4;
    //variable that stores rounded avg
    let avgTotalRound = Math.round(avgTotal);
    let totalRange = document.getElementById('myRange-total');
    //sets value attribute for total range
    totalRange.setAttribute('value', avgTotalRound);
    
    let output = document.getElementById('range-5');
    //displays total on write-review.html
    output.innerHTML = avgTotalRound;
}