/*
function generate() {
    //window.location.href = "https://your-api-url/worksheet";
    //window.location.href = "http://127.0.0.1:5000/worksheet";
    window.location.href = "https://mad-min.onrender.com/worksheet";
}
*/

function generate() {

    //const max = document.getElementById("max").value;
    //const problems = document.getElementById("problems").value;

    const url =
    "http://127.0.0.1:5000/worksheet" + "?r";
    //+ "?max=" + max
    //+ "&problems=" + problems;

    window.location.href = url;
}

function generate_single_digit(single_digit) {

    //const single_digit = document.getElementById("single_digit").value;
    //const problems = document.getElementById("problems").value;
    //"/worksheet_single_digit"
    const url =
    "http://127.0.0.1:5000/worksheet_single_digit"
    + "?single_digit=" + single_digit;
    

    window.location.href = url;
}