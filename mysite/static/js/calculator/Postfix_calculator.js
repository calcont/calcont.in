$(".cal").click(function (e) {
  var postfix = document.getElementById("Postfix").value;
  var stack = [],
    top = -1;

  var i, a, b, result, pEval, ch;

  for (i = 0; i <= postfix.length; i++) {
    ch = postfix[i];

    if (!isNaN(parseInt(ch))) {
      stack[++top] = parseInt(ch);
    } else if (ch == "+" || ch == "-" || ch == "*" || ch == "/") {
      b = stack[top];
      top--;
      a = stack[top];
      top--;

      if (ch == "+") {
        result = a + b;
      } else if (ch == "-") {
        result = a - b;
      } else if (ch == "*") {
        result = a * b;
      } else if (ch == "/") {
        result = a / b;
      }
      stack[++top] = result;
    }
  }

  pEval = stack[top];

  // top--;

  document.getElementById("Ans").value = pEval;

  e.preventDefault();
});
