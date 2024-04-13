
//setup before functions
var typingTimer;                //timer identifier
var doneTypingInterval = 800;
var text = document.getElementById('HText') ,Otext;

//on keyup, start the countdown
$('#HText').on('keyup', function () {
    document.getElementById('EText').value = "Processing...";
    clearTimeout(typingTimer);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
});

//on keydown, clear the countdown 
$('#HText').on('keydown', function () {
    clearTimeout(typingTimer);
});


//user is "finished typing," do something
function doneTyping() {
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            text: text.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        encode: true,
        success: function (response) {
            var GotRes = JSON.parse(response)
            Otext = GotRes['ConTex']
            document.getElementById('EText').value = Otext;
        }
    });
}