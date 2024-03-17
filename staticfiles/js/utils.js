function processSpacedExpression(input) {
    const tokens = input.trim().split(/\s+|([+\-*\/])/).filter(Boolean);
    return tokens;
}