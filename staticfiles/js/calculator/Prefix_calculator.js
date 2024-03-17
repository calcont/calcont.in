const enabledSpaceText = "Disable Space Separation e.g 54 considered as 5 and 4";
const disabledSpaceText = 'Enable space-separated digits e.g. treat "54" as one number in "+ 54"';
const Ans = document.getElementById("Ans");
let prefix, spaceSeparationStatus = false, stack = [], idx, prefixExp, prefixAns;


$(".cal").click(function (e) {  
  e.preventDefault();
  prefix = document.getElementById("Prefix").value;
  spaceSeparationStatus = document.getElementById("prefix-switch").checked;
  if (spaceSeparationStatus) {
    prefixExp = processSpacedExpression(prefix);
  }
  else {
    prefixExp = prefix.replace(/\s/g, "").split("");
  }
  stack = [];

  //function to check whether character is number or not
  function is_numeric(str) {
    return /^\d+$/.test(str);
  }

  try {
    if (prefixExp) {
      for (let idx = prefixExp.length - 1; idx >= 0; idx--) {
        if (is_numeric(parseInt(prefixExp[idx]))) {
          stack.push(prefixExp[idx]);
        } else if (prefixExp[idx] === " ") {
          continue;
        } else {
          let tempAns = eval(stack.pop() + prefixExp[idx] + stack.pop());
          stack.push(tempAns);
        }
      }
    }
    prefixAns = stack.pop();
    if (isNaN(prefixAns)) {
      throw "Invalid Expression";
    }
    Ans.value = prefixAns;
  }
  catch (e) {
    Ans.value = "Error while parsing or Invalid Expression";
  }
});
