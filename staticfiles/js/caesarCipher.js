function encodetxt(text,shift) {
    var output = '';
        for(var i = 0; i < text.length; i++){
            var char = text[i];
            var code = char.charCodeAt(0);
             if(code >=65  && code <=90 ){
                output += String.fromCharCode((code - 65 + parseInt(shift) )%26 + 65);
            }
            else if(code>=97 && code <=122){
                output += String.fromCharCode((code - 97 + parseInt(shift) )%26 + 97);
            }
            else{
                output += char;
            }
            
        }
        return output;
}
function decodetxt(txt,shift){
    var output = '';
        for(var i = 0; i < txt.length; i++){
            
            var char = txt[i];
            var code = char.charCodeAt(0);
             if(code >=65  && code <=90 ){
                 
                output += String.fromCharCode(((((code - 65 - parseInt(shift) )%26) + 26)%26) + 65);
            }
            else if(code>=97 && code <=122){
                output += String.fromCharCode(((((code - 97 - parseInt(shift) )%26) + 26)%26) + 97);
            }
            else{
                output += char;
            }
            
        }
        return output;
}