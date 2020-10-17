var slider1;
var slider2;
var slider3;
var slider4;

function rangeVal() {
    slider1 = document.getElementById("myRange-1");
    var output = document.getElementById("range-1");
    output.innerHTML = slider1.value;
    slider1.oninput = function() {
        output.innerHTML = this.value;
    };
}

function rangeVal1() {
    slider2 = document.getElementById("myRange-2");
    var output = document.getElementById("range-2");
    output.innerHTML = slider2.value;
    slider2.oninput = function() {
        output.innerHTML = this.value;
    };
}

function rangeVal2() {
    slider3 = document.getElementById("myRange-3");
    var output = document.getElementById("range-3");
    output.innerHTML = slider3.value;
    slider3.oninput = function() {
        output.innerHTML = this.value;
    };
}

function rangeVal3() {
    slider4 = document.getElementById("myRange-4");
    var output = document.getElementById("range-4");
    output.innerHTML = slider4.value;
    slider4.oninput = function() {
        output.innerHTML = this.value;
    };
}

function getTotal() {
    slider1 = document.getElementById('myRange-1').value;
    slider2 = document.getElementById('myRange-2').value;
    slider3 = document.getElementById('myRange-3').value;
    slider4 = document.getElementById('myRange-4').value;
    
    let total = Number(slider1) + Number(slider2) + Number(slider3) + + Number(slider4);
    let avgTotal = total/4;
    let avgTotalRound = Math.round(avgTotal);
    console.log(avgTotalRound);
    let totalRange = document.getElementById('myRange-total');
    totalRange.setAttribute('value', avgTotalRound);
    
    let output = document.getElementById('range-5');
    output.innerHTML = avgTotalRound;
}