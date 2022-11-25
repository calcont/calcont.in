$(".con").click(function (e) {
  var infixed = document.getElementById("Infix").value;
  var infix = infixed.split("");
  for (var i = 0; i < infix.length; i++) {
    if (infix[i] == "(") {
      infix[i] = ")";
    } else if (infix[i] == ")") {
      infix[i] = "(";
    }
  }
  infix = infix.reverse();
  var stack = [],
    prefix = [];
  var operand, prec;
  document.getElementById("OutTable").style.display = "block";
  $("#content").empty();

  function isOperand(operand) {
    if (
      (operand >= "a" && operand <= "z") ||
      (operand >= "A" && operand <= "Z") ||
      (operand >= "0" && operand <= "9")
    ) {
      return 1;
    } else {
      return 0;
    }
  }
  function valinTable(i, infix, stack, prefix) {
    var strPre = prefix.toString();

    var strStack = stack.toString();
    tble = `<tr >
                        <td class="rounded-lg">
                        ${i}
                        </td>
                        <td class="rounded-lg">
                        ${infix[i]}
                        </td>
                        <td class="rounded-lg">
                        ${strStack.replaceAll(",", "")}
                        </td>
                        <td class="rounded-lg">
                        ${strPre.replaceAll(",", "")}
                        </td>
                      </tr>`;

    $("#content").append(tble);
  }
  function precedence(prec) {
    if (prec == "(") {
      return 4;
    }
    if (prec == "^" || prec == "%") {
      return 3;
    }
    if (prec == "*" || prec == "/") {
      return 2;
    }
    if (prec == "+" || prec == "-") {
      return 1;
    }
    if (prec == ")") {
      return 0;
    }
    return -1;
  }
  for (var i = 0; i < infix.length; i++) {
    if (isOperand(infix[i])) {
      prefix.push(infix[i]);
    } else if (infix[i] == " ") {
      continue;
    } else if (stack.length == 0) {
      stack.push(infix[i]);
    } else if (infix[i] == ")") {
      while (stack[stack.length - 1] != "(") {
        prefix.push(stack.pop());
      }
      stack.pop();
    } else if (precedence(infix[i]) > precedence(stack[stack.length - 1])) {
      stack.push(infix[i]);
    } else {
      while (
        precedence(infix[i]) <= precedence(stack[stack.length - 1]) &&
        stack.length != 0 &&
        stack[stack.length - 1] != "("
      ) {
        prefix.push(stack.pop());
      }
      stack.push(infix[i]);
    }
    valinTable(i, infix, stack, prefix);
  }
  while (stack.length != 0) {
    prefix.push(stack.pop());
  }
  infix[i] = " ";
  valinTable(i, infix, stack, prefix);
  prefix = prefix.reverse();
  var strPre = prefix.toString();
  document.getElementById("prefix").value = strPre.replaceAll(",", "");
  e.preventDefault();
});
