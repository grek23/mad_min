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

    //for local processing
    //const url = "http://127.0.0.1:5000/worksheet" + "?r";
    //+ "?max=" + max
    //+ "&problems=" + problems;

    //For processing on Render
    const url = "https://mad-min.onrender.com/worksheet" + "?r";


    window.location.href = url;
}

function generate_single_digit(single_digit) {

    //const single_digit = document.getElementById("single_digit").value;
    //const problems = document.getElementById("problems").value;
    //"/worksheet_single_digit"

    //for local processing
    //const url = "http://127.0.0.1:5000/worksheet_single_digit" + "?single_digit=" + single_digit;
    
    //For processing on render
    const url = "https://mad-min.onrender.com/worksheet_single_digit" + "?single_digit=" + single_digit;

    window.location.href = url;
}