var canvas = this.__canvas = new fabric.Canvas('c');
canvas.setHeight(300);
canvas.setWidth(500);

addText();

function addText() {
    canvas.add(new fabric.Textbox('Sample Text', {
        left: 50,
        top: 100,
        fontFamily: 'arial black',
        fill: '#fff',
        fontSize: 50
    }));
}

function checkActiveObject() {
    if (canvas.getActiveObject()) {
        return true;
    }
    alert('Please select a text');
    return false;
}

function updateCanvasObject(property, value) {
    if (checkActiveObject()) {
        canvas.getActiveObject().set(property, value);
        canvas.renderAll();
    }
}

document.getElementById('canvas-bg-color').oninput = function () {
    canvas.setBackgroundColor(this.value);
    canvas.renderAll();
};

document.getElementById('text-color').oninput = function () {
    updateCanvasObject('fill', this.value);
};

document.getElementById('text-lines-bg-color').oninput = function () {
    updateCanvasObject('textBackgroundColor', this.value);
};

document.getElementById('text-stroke-color').oninput = function () {
    updateCanvasObject('stroke', this.value);
};

document.getElementById('text-stroke-width').oninput = function () {
    updateCanvasObject('strokeWidth', this.value);
};

document.getElementById('font-family').onchange = function () {
    updateCanvasObject("fontFamily", this.value);
};

document.getElementById('text-font-size').oninput = function () {
    updateCanvasObject('fontSize', this.value);
};

document.getElementById('text-line-height').oninput = function () {
    updateCanvasObject('lineHeight', this.value);
};

document.getElementById('text-align').onchange = function () {
    updateCanvasObject('textAlign', this.value);
};



radios5 = document.getElementsByName("fonttype");  // wijzig naar button
for (var i = 0, max = radios5.length; i < max; i++) {
    radios5[i].onclick = function () {

        if (document.getElementById(this.id).checked == true) {
            if (this.id == "text-cmd-bold") {
                canvas.getActiveObject().set("fontWeight", "bold");
            }
            if (this.id == "text-cmd-italic") {
                canvas.getActiveObject().set("fontStyle", "italic");
            }
            if (this.id == "text-cmd-underline") {
                canvas.getActiveObject().set("underline", this.value);
            }
            if (this.id == "text-cmd-linethrough") {
                canvas.getActiveObject().set("linethrough", this.value);
            }
            if (this.id == "text-cmd-overline") {
                canvas.getActiveObject().set("overline", this.value);
            }
        } else {
            if (this.id == "text-cmd-bold") {
                canvas.getActiveObject().set("fontWeight", "");
            }
            if (this.id == "text-cmd-italic") {
                canvas.getActiveObject().set("fontStyle", "");
            }
            if (this.id == "text-cmd-underline") {
                canvas.getActiveObject().set("underline", false);
            }
            if (this.id == "text-cmd-linethrough") {
                canvas.getActiveObject().set("linethrough", false);
            }
            if (this.id == "text-cmd-overline") {
                canvas.getActiveObject().set("overline", false);
            }
        }
        canvas.renderAll();
    }
}

function downloadCanvas() {
    // Get the data URL of the canvas as a PNG image
    var dataURL = canvas.toDataURL({ format: 'png' });

    // Set the data URL as the href attribute of the download button
    var downloadBtn = document.getElementById('link');
    downloadBtn.href = dataURL;
    downloadBtn.download = 'calcont-img-frm-text.png';
}

$('#link').click(function () {
    downloadCanvas();
});

$('#reset').click(function (e) {
    e.preventDefault();
    canvas.clear();
    addText();
});

$('#transparent-bg').click(function () {
    if (document.getElementById('transparent-bg').checked ==true) {
        canvas.setBackgroundColor('rgba(0,0,0,0)');
        canvas.renderAll();
    }
});