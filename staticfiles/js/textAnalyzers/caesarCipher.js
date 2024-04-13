document.getElementById("encode-decode").addEventListener("click", function (e) {
    e.preventDefault();
    const text = document.getElementById("text").value;
    const action = document.getElementById("action").value;
    const shift = document.getElementById("shift").value;
    const output = document.getElementById("output");
    if (text.length === 0) {
        alert('Please enter text');
    } else {
        output.value = transformText(text, shift, action);
    }
})

function transformText(text, shift, action) {
    let output = '';
    let strategy = new strategyInterface();
    if (action === 'encode') {
        strategy.strategy = new encodeStrategy(shift);
    } else if (action === 'decode') {
        strategy.strategy = new decodeStrategy(shift);
    }
    for (let i = 0; i < text.length; i++) {
        let code = text[i].charCodeAt(0);
        let transformedText = strategy.execute(code);
        if (transformedText === '') {
            output += text[i];
        } else {
            output += transformedText;
        }
    }
    return output;
}

class strategyInterface {

    constructor(shift) {
        this.strategy = null;
        this.shift = shift;
    }

    execute(code) {
        let currentOutput = '';
        currentOutput += this.capitalCase(code);
        currentOutput += this.smallCase(code);
        return currentOutput;

    }

    capitalCase(code) {
        if (code >= 65 && code <= 90) {
            return this.strategy.capitalCase(code);
        }
        return '';
    }

    smallCase(code) {
        if (code >= 97 && code <= 122) {
            return this.strategy.smallCase(code);
        }
        return '';
    }
}

class encodeStrategy extends strategyInterface {

    capitalCase(code) {
        return String.fromCharCode((code - 65 + parseInt(this.shift)) % 26 + 65);
    }

    smallCase(code) {
        return String.fromCharCode((code - 97 + parseInt(this.shift)) % 26 + 97);
    }
}

class decodeStrategy extends strategyInterface {

    capitalCase(code) {
        return String.fromCharCode(((((code - 65 - parseInt(this.shift)) % 26) + 26) % 26) + 65);
    }

    smallCase(code) {
        return String.fromCharCode(((((code - 97 - parseInt(this.shift)) % 26) + 26) % 26) + 97);
    }

}