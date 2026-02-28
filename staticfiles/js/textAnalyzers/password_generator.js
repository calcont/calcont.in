document.addEventListener('DOMContentLoaded', () => {
    const passwordDisplay = document.getElementById('generated-password');
    const lengthSlider = document.getElementById('password-length');
    const lengthVal = document.getElementById('length-val');
    const uppercaseCb = document.getElementById('include-uppercase');
    const lowercaseCb = document.getElementById('include-lowercase');
    const numbersCb = document.getElementById('include-numbers');
    const symbolsCb = document.getElementById('include-symbols');
    const generateBtn = document.getElementById('generate-btn');
    const copyBtn = document.getElementById('copy-password-btn');

    const UPPERCASE_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const LOWERCASE_CHARS = 'abcdefghijklmnopqrstuvwxyz';
    const NUMBER_CHARS = '0123456789';
    const SYMBOL_CHARS = '!@#$%^&*()_+~`|}{[]:;?><,./-=';

    function generatePassword() {
        let chars = '';
        if (uppercaseCb.checked) chars += UPPERCASE_CHARS;
        if (lowercaseCb.checked) chars += LOWERCASE_CHARS;
        if (numbersCb.checked) chars += NUMBER_CHARS;
        if (symbolsCb.checked) chars += SYMBOL_CHARS;

        if (chars.length === 0) {
            passwordDisplay.textContent = 'Please select at least one option';
            return;
        }

        let password = '';
        const length = parseInt(lengthSlider.value);

        let requiredChars = [];
        if (uppercaseCb.checked) requiredChars.push(UPPERCASE_CHARS[Math.floor(Math.random() * UPPERCASE_CHARS.length)]);
        if (lowercaseCb.checked) requiredChars.push(LOWERCASE_CHARS[Math.floor(Math.random() * LOWERCASE_CHARS.length)]);
        if (numbersCb.checked) requiredChars.push(NUMBER_CHARS[Math.floor(Math.random() * NUMBER_CHARS.length)]);
        if (symbolsCb.checked) requiredChars.push(SYMBOL_CHARS[Math.floor(Math.random() * SYMBOL_CHARS.length)]);

        // Always put one character of each requirement
        for (let i = 0; i < requiredChars.length && i < length; i++) {
            password += requiredChars[i];
        }

        for (let i = password.length; i < length; i++) {
            const randomIndex = Math.floor(Math.random() * chars.length);
            password += chars[randomIndex];
        }

        password = password.split('').sort(() => 0.5 - Math.random()).join('');

        passwordDisplay.textContent = password;
    }

    // Event Listeners
    lengthSlider.addEventListener('input', (e) => {
        lengthVal.textContent = e.target.value;
        generatePassword();
    });

    [uppercaseCb, lowercaseCb, numbersCb, symbolsCb].forEach(cb => {
        cb.addEventListener('change', generatePassword);
    });

    generateBtn.addEventListener('click', generatePassword);

    copyBtn.addEventListener('click', () => {
        const textToCopy = passwordDisplay.textContent;
        if (textToCopy === 'Please select at least one option' || textToCopy === 'Generating...') return;

        navigator.clipboard.writeText(textToCopy).then(() => {
            const originalHTML = copyBtn.innerHTML;
            copyBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#28a745" class="bi bi-check" viewBox="0 0 16 16">
                    <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
                </svg>
            `;
            setTimeout(() => {
                copyBtn.innerHTML = originalHTML;
            }, 2000);
        });
    });

    // Initial Generation
    generatePassword();
});
