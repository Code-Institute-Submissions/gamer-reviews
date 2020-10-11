function rangeVal() {
    var slider = document.getElementById("myRange-1");
    var output = document.getElementById("range-1");
    output.innerHTML = slider.value;
    slider.oninput = function() {
        output.innerHTML = this.value;
    };
}

function rangeVal1() {
    var slider = document.getElementById("myRange-2");
    var output = document.getElementById("range-2");
    output.innerHTML = slider.value;
    slider.oninput = function() {
        output.innerHTML = this.value;
    };
}

function rangeVal2() {
    var slider = document.getElementById("myRange-3");
    var output = document.getElementById("range-3");
    output.innerHTML = slider.value;
    slider.oninput = function() {
        output.innerHTML = this.value;
    };
}

function rangeVal3() {
    var slider = document.getElementById("myRange-4");
    var output = document.getElementById("range-4");
    output.innerHTML = slider.value;
    slider.oninput = function() {
        output.innerHTML = this.value;
    };
}
