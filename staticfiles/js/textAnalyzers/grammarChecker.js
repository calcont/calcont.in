let loader = document.getElementById("loading");
let correctBtn = document.getElementById("buttons");
let alertM = document.getElementById("alert");
let alertP = document.getElementById("Palert");
let lengthThreshold = 1000;
let len = 0;
function countChar() {
    len = document.getElementById('Text').value.length;
    document.getElementById('exceed').innerHTML = "(" + len + `/${lengthThreshold})`;
    if (len > lengthThreshold) {
        alertM.innerHTML = "Please enter text less than " + lengthThreshold + " characters";
    }
    else {
        alertM.innerHTML = "";
    }
}

function processData() {
    let originalText = document.getElementById("Text").value;
    loader.style.display = "block";
    correctBtn.style.display = "none";
    $.ajax({
        url: "/Analyzer/Grammar_correction/",
        type: "POST",
        data: {
            text: originalText,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            document.getElementById("Text").value = data;
            loader.style.display = "none";
            correctBtn.style.display = "block";
            alertP.style.display = "block";
        },
        error: function (data) {
            originalText = "Error while processing the text. Please try again.";
        }
    })
}

$('#correct').click(function (e) {
    alertP.style.display = "none";
    if (len > lengthThreshold) {
        alertM.innerHTML = "Please enter text less than " + lengthThreshold + " characters";
        return;
    }
    else if (len == 0) {
        alertM.innerHTML = "Please enter some text";
        return;
    }
    alertM.innerHTML = "";
    processData();
    e.preventDefault();
})
