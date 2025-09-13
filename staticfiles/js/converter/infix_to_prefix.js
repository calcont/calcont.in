const Ans = document.getElementById("prefix");
const content = document.getElementById("content");
let infix, stack, prefix, tble;

$(".con").click(function (e) {
    e.preventDefault();
    infix = document.getElementById("Infix").value;
    if (infix === "") {
        Ans.value = "Please enter a valid infix expression";
        return;
    }
    infix = removeExtraSpaces(infix);
    document.getElementById("OutTable").style.display = "block";
    content.innerHTML = "";

    let operators = [];
    let operands = [];

    for (let i = 0; i < infix.length; i++) {
        if (infix[i] === '(') {
            operators.push(infix[i]);
        } else if (infix[i] === ')') {
            while (operators.length !== 0 &&
            operators[operators.length - 1] !== '(') {
                operandsPushLogic(operands, operators);
            }
            operators.pop();
        } else if (!isOperatorWithParenthesis(infix[i])) {
            operands.push(infix[i] + "");
        } else {
            while (operators.length &&
            precedence[infix[i]] <=
            precedence[operators[operators.length - 1]]) {
                operandsPushLogic(operands, operators)
            }
            operators.push(infix[i]);
        }
        updateTable(i, infix[i], operators, operands, content)
    }
    while (operators.length !== 0) {
        operandsPushLogic(operands, operators);
    }
    updateTable(infix.length, '', operators, operands, content)
    Ans.value = operands.pop();
});


function operandsPushLogic(operands, operators) {
    let op1 = pop(operands);
    let op2 = pop(operands);
    let op = pop(operators);
    let tmp = op + op2 + op1;
    operands.push(tmp);
    return operands;
}

function pop(arr) {
    if (arr.length === 0) {
        return "";
    }
    return arr.pop();
}