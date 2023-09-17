let len = 0;
let isProcessing = false;
let alertM = document.getElementById('alert');
let loading = document.getElementById('loading');
let buttons = document.getElementById('buttons');
function countChar() {
    len = document.getElementById('Text').value.length;
    document.getElementById('exceed').innerHTML = "(" + len + "/1000)";
    if (len > 1000) {
        alertM.innerHTML = "Please enter text less than 1000 characters";
    }
    else {
        alertM.innerHTML = "";
    }
}
$('#check').click(function (e) {
    commonChecks(e) ? postReq("check") : null;
})

$('#correct').click(function (e) {
    commonChecks(e) ? postReq("correct") : null;
})

function commonChecks(e) {
    if (document.getElementById('Text').value.length == 0) {
        alertM.innerHTML = "Please enter some text";
        return false;
    }
    if (len > 1500) {
        alertM.innerHTML = "Please enter text less than 1000 characters";
        return false;
    }
    e.preventDefault();
    return true;
}

function postReq(type) {
    alertM.innerHTML = "";
    let payload = {
        text: document.getElementById('Text').value,
        type: type
    }
    buttons.style.display = "none";
    loading.style.display = "block";
    $.ajax({
        url: "/Analyzer/Grammar_correction/",
        type: "POST",
        data: {
            payload: JSON.stringify(payload),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            data = JSON.parse(data);
            document.getElementById('Text').value = data['text'];
            buttons.style.display = "block";
            loading.style.display = "none";
        },
    })
}