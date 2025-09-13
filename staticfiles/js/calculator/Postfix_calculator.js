const enabledSpaceText = "Disable Space Separation e.g 54 considered as 5 and 4";
const disabledSpaceText = 'Enable space-separated digits e.g. treat "54" as one number in "54 +"';
const Ans = document.getElementById("Ans");
let postfix, spaceSeparationStatus = false;
let stack, stackTop;
let i, a, b, result, pEval, ch;

$(".cal").click(function (e) {
  e.preventDefault();
  postfix = document.getElementById("Postfix").value;
  if (postfix === "") {
    Ans.value = "Please enter a valid postfix expression";
    return;
  }
  spaceSeparationStatus = document.getElementById("postfix-switch").checked;
  if (spaceSeparationStatus) {
    postfix = processSpacedExpression(postfix);
  }
  else {
    postfix = removeExtraSpaces(postfix).split("");
  }

  stack = [] ;
  stackTop = -1;

  try {
    for (i = 0; i <= postfix.length; i++) {
      ch = postfix[i];

      if (!isNaN(parseInt(ch))) {
        stack[++stackTop] = parseInt(ch);
      } else if (ch == "+" || ch == "-" || ch == "*" || ch == "/" || ch == "^") {
        b = stack[stackTop];
        stackTop--;
        a = stack[stackTop];
        stackTop--;

        switch (ch) {
          case "+":
            result = a + b;
            break;
          case "-":
            result = a - b;
            break;
          case "*":
            result = a * b;
            break;
          case "/":
            result = a / b;
            break;
          case "^":
            result = Math.pow(a, b);
            break;
        }
        stack[++stackTop] = result;
      }
    }

    pEval = stack[stackTop];
    if (isNaN(pEval)) {
      throw "Invalid Expression";
    }
    Ans.value = roundToThreeDecimalPlaces(pEval);
  }
  catch (e) {
    Ans.value = "Invalid Expression";
  }

});

document.getElementById("postfix-switch").addEventListener("change", function () {
  let spaceSeparationText = document.getElementById("postfix-switch_text");
  spaceSeparationText.innerText = this.checked ? enabledSpaceText : disabledSpaceText;
});
