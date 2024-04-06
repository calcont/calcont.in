const precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
};


function processSpacedExpression(input) {
    return input.trim().split(/\s+|([+\-*\/])/).filter(Boolean);
}

function removeExtraSpaces(input) {
    return input.replace(/\s+/g, "");
}

function reverseString(input) {
    return input.split("").reverse().join("");
}

function roundToThreeDecimalPlaces(number) {
    return Math.round(number * 1000) / 1000;
}

function isOperand(operand) {
    if ((operand >= 'a' && operand <= 'z') || (operand >= 'A' && operand <= 'Z') || (operand >= '0' && operand <= '9')) {
        return (1);
    } else {
        return (0);
    }
}

function isOperator(operator) {
    return ['+', '-', '*', '/', '^', '(', ')'].includes(operator);
}

function updateTable(index, value, stack, exp, contentRef) {
    let expString = exp.join(" ");
    let strStack = stack.join(" ");
    let table =
        `<tr>
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
                ${expString}
            </td>
      </tr>`;

    contentRef.innerHTML += table;
}
