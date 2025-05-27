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
        let token = infix[i];

        if (isOperand(token)) {
            postfix.push(token);
        } else if (token === '(') {
            stack.push(token);
        } else if (token === ')') {
            while (stack.length && stack[stack.length - 1] !== '(') {
                postfix.push(stack.pop());
            }
            stack.pop(); // remove '('
        } else {
            while (
                stack.length &&
                stack[stack.length - 1] !== '(' &&
                (
                    (associativity[token] === 'L' && precedence[token] <= precedence[stack[stack.length - 1]]) ||
                    (associativity[token] === 'R' && precedence[token] < precedence[stack[stack.length - 1]])
                )
                ) {
                postfix.push(stack.pop());
            }
            stack.push(token);
        }

        updateTable(i, token, stack, postfix, content);
    }

    while (stack.length) {
        postfix.push(stack.pop());
    }

    updateTable(i, '', stack, postfix, content);
    return removeExtraSpaces(postfix.join(''));
}
