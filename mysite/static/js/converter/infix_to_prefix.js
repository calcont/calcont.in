$(".con").click(function (e) {
  var infixed = document.getElementById("Infix").value;
  infixed = infixed.replaceAll(" ", "");
  var infix = infixed.split("");
  document.getElementById("OutTable").style.display = "block";
  $("#content").empty();
  e.preventDefault();

  function valinTable(index, value, stack, prefix) {
    var strPre = prefix.join(" ");
    var strStack = stack.join(" ");
    var tble = `<tr>
                        <td class="rounded-lg">
                        ${index}
                        </td>
                        <td class="rounded-lg">
                        ${value}
                        </td>
                        <td class="rounded-lg">
                        ${strStack}
                        </td>
                        <td class="rounded-lg">
                        ${strPre}
                        </td>
                      </tr>`;

    $("#content").append(tble);
  }
  // Helper function to get the precedence of operators
  function getPrecedence(operator) {
    switch (operator) {
      case '^':
        return 4;
      case '*':
      case '/':
        return 3;
      case '+':
      case '-':
        return 2;
      case '(':
        return 1;
      default:
        return 0; // For operands
    }
  }

  // Function to check if a character is an operator
  function isOperator(char) {
    return ['+', '-', '*', '/', '^', '(', ')'].includes(char);
  }

  let operators = [];
  let operands = [];
  
  for (let i = 0; i < infix.length; i++) {
    if (infix[i] == '(') {
      operators.push(infix[i]);
    }
    else if (infix[i] == ')') {
      while (operators.length != 0 &&
        operators[operators.length - 1] != '(') {
        let op1 = operands.pop();
        let op2 = operands.pop();
        let op = operators.pop();
        let tmp = op + op2 + op1;
        operands.push(tmp);
      }
      operators.pop();
    }
    else if (!isOperator(infix[i])) {
      operands.push(infix[i] + "");
    }
    else {
      while (operators.length &&
        getPrecedence(infix[i]) <=
        getPrecedence(operators[operators.length - 1])) {
        let op1 = operands.pop();
        let op2 = operands.pop();
        let op = operators.pop();
        let tmp = op + op2 + op1;
        operands.push(tmp);
      }
      operators.push(infix[i]);
    }
    valinTable(i, infix[i], operators, operands);
  }
  while (operators.length != 0) {
    let op1 = operands.pop();
    let op2 = operands.pop();
    let op = operators.pop();
    let tmp = op + op2 + op1;
    operands.push(tmp);
  }
  valinTable(infix.length, "", operators, operands);
  document.getElementById("prefix").value = operands.pop();
});
