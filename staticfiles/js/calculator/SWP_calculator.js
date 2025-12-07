// Format currency in Indian format
function formatCurrency(amount) {
    if (amount === undefined || amount === null || isNaN(amount)) return '₹ 0';
    return '₹ ' + Math.round(amount).toLocaleString('en-IN');
}

// Format percentage
function formatPercentage(value) {
    return value.toFixed(1) + '%';
}

// Format years
function formatYears(value) {
    return value + ' Yr';
}

// Update slider fill (visual indicator)
function updateSliderFill(sliderId, fillId) {
    const slider = document.getElementById(sliderId);
    const fill = document.getElementById(fillId);
    if (slider && fill) {
        const min = parseFloat(slider.min);
        const max = parseFloat(slider.max);
        const value = parseFloat(slider.value);
        const percentage = ((value - min) / (max - min)) * 100;
        fill.style.width = percentage + '%';
    }
}

// Calculate monthly rate of return from annual return
function getMonthlyRate(annualReturn) {
    return Math.pow(1 + annualReturn / 100, 1 / 12) - 1;
}

// Calculate SWP
function calculateSWP(totalInvestment, withdrawalAmount, annualReturn, years) {
    const monthlyRate = getMonthlyRate(annualReturn);
    let currentBalance = totalInvestment;
    let totalWithdrawn = 0;
    const totalMonths = years * 12;

    for (let month = 1; month <= totalMonths; month++) {
        // Add returns for the month
        currentBalance += currentBalance * monthlyRate;

        // Subtract withdrawal (allow negative balance)
        currentBalance -= withdrawalAmount;
        totalWithdrawn += withdrawalAmount;
    }

    return {
        totalInvestment: totalInvestment,
        totalWithdrawn: totalWithdrawn,
        finalValue: currentBalance
    };
}

// Update results display
function updateResults() {
    const totalInvestment = parseFloat(document.getElementById('totalInvestment').value);
    const withdrawalAmount = parseFloat(document.getElementById('withdrawalAmount').value);
    const annualReturn = parseFloat(document.getElementById('expectedReturn').value);
    const years = parseInt(document.getElementById('timePeriod').value);

    const result = calculateSWP(totalInvestment, withdrawalAmount, annualReturn, years);

    // Update display
    document.getElementById('resultTotalInvestment').textContent = formatCurrency(result.totalInvestment);
    document.getElementById('totalWithdrawal').textContent = formatCurrency(result.totalWithdrawn);
    document.getElementById('finalValue').textContent = formatCurrency(result.finalValue);
}

// Parse value from display string (remove currency/percentage symbols)
function parseDisplayValue(displayValue, type) {
    if (!displayValue) return 0;
    let cleanValue = displayValue.toString().replace(/[₹,\s%Yr]/g, '');
    cleanValue = cleanValue.trim();
    const numValue = parseFloat(cleanValue);
    return isNaN(numValue) ? 0 : numValue;
}

// Update display values and slider fills
function updateDisplays() {
    const totalInvestment = parseFloat(document.getElementById('totalInvestment').value);
    const withdrawalAmount = parseFloat(document.getElementById('withdrawalAmount').value);
    const annualReturn = parseFloat(document.getElementById('expectedReturn').value);
    const years = parseInt(document.getElementById('timePeriod').value);

    document.getElementById('totalInvestmentDisplay').value = formatCurrency(totalInvestment);
    document.getElementById('withdrawalAmountDisplay').value = formatCurrency(withdrawalAmount);
    document.getElementById('expectedReturnDisplay').value = formatPercentage(annualReturn);
    document.getElementById('timePeriodDisplay').value = formatYears(years);

    updateSliderFill('totalInvestment', 'totalInvestmentFill');
    updateSliderFill('withdrawalAmount', 'withdrawalAmountFill');
    updateSliderFill('expectedReturn', 'expectedReturnFill');
    updateSliderFill('timePeriod', 'timePeriodFill');

    updateResults();
}

// Update sliders from display inputs
function updateFromDisplay(displayId, sliderId, type) {
    const display = document.getElementById(displayId);
    const slider = document.getElementById(sliderId);

    if (!display || !slider) return;

    let value = parseDisplayValue(display.value, type);
    const min = parseFloat(slider.min);
    const max = parseFloat(slider.max);

    // Clamp value to slider range
    value = Math.max(min, Math.min(max, value));

    // Update slider
    slider.value = value;
    updateDisplays();
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function () {
    // Event listeners for sliders
    document.getElementById('totalInvestment').addEventListener('input', updateDisplays);
    document.getElementById('withdrawalAmount').addEventListener('input', updateDisplays);
    document.getElementById('expectedReturn').addEventListener('input', updateDisplays);
    document.getElementById('timePeriod').addEventListener('input', updateDisplays);

    // Display input event listeners (editable fields) - use blur to allow editing
    document.getElementById('totalInvestmentDisplay').addEventListener('blur', function () {
        updateFromDisplay('totalInvestmentDisplay', 'totalInvestment', 'currency');
    });
    document.getElementById('withdrawalAmountDisplay').addEventListener('blur', function () {
        updateFromDisplay('withdrawalAmountDisplay', 'withdrawalAmount', 'currency');
    });
    document.getElementById('expectedReturnDisplay').addEventListener('blur', function () {
        updateFromDisplay('expectedReturnDisplay', 'expectedReturn', 'percentage');
    });
    document.getElementById('timePeriodDisplay').addEventListener('blur', function () {
        updateFromDisplay('timePeriodDisplay', 'timePeriod', 'years');
    });

    // Initial calculation
    updateDisplays();
});
