$(".cal").click(function (e) {

  e.preventDefault();
  let prefixExp = document.getElementById("prefix").value;
  prefixExp = prefixExp.replace(/\s+/g, '');
  let stack = [];

  //function to check whether character is number or not
  function is_numeric(str) {
    return /^\d+$/.test(str);
  }

  if (prefixExp) {
    for (idx = prefixExp.length - 1; idx >= 0; idx--) {
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
  document.getElementById('Ans').value = stack.pop();
});
