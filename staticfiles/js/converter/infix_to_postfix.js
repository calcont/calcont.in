const Ans = document.getElementById('Postfix');
let content = document.getElementById('content');
let infix;


$('.con').click(function (e) {
    e.preventDefault();
    infix = document.getElementById('Infix').value;
    if (infix === "") {
        Ans.value = "Please enter a valid infix expression";
        return;
    }
    document.getElementById('OutTable').style.display = "block";
    content.innerHTML = "";
    Ans.value = removeExtraSpaces(infixToPostfix(infix));
});

function infixToPostfix(infix) {
    infix = removeExtraSpaces(infix);
    let stack = [];
    let postfix = [];
    let i;
    for (i = 0; i < infix.length; i++) {
        if (isOperand(infix[i])) {
            postfix.push(infix[i]);
        } else if (stack.length === 0) {
            stack.push(infix[i]);
        } else if (infix[i] === ')') {
            while (stack[stack.length - 1] !== '(') {
                postfix.push(stack.pop());
            }
            stack.pop();
        } else if (precedence[infix[i]] > precedence[stack[stack.length - 1]]) {
            stack.push(infix[i]);
        } else {
            while (precedence[infix[i]] <=  precedence[stack[stack.length - 1]] && stack.length !== 0 && stack[stack.length - 1] !== '(') {
                postfix.push(stack.pop());
            }
            stack.push(infix[i]);
        }
        updateTable(i, infix[i], stack, postfix, content);
    }
    while (stack.length !== 0) {
        postfix.push(stack.pop());
    }
    updateTable(i, '', stack, postfix, content);
    let postfixString = postfix.join('');
    return removeExtraSpaces(postfixString);
}
