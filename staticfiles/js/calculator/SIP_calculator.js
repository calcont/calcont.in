let currentMode = 'SIP'; // 'SIP' or 'LUMPSUM'

// Format currency in Indian format
function formatCurrency(amount) {
    if (!amount || isNaN(amount)) return '₹ 0';
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

// Calculate SIP
function calculateSIP(monthlyInvestment, annualReturn, years, stepUpPercent = 0) {
    const monthlyRate = getMonthlyRate(annualReturn);
    let totalInvested = 0;
    let totalValue = 0;

    let currentInvestment = monthlyInvestment;
    const stepUpMultiplier = 1 + (stepUpPercent / 100);

    for (let year = 1; year <= years; year++) {
        // For each year, do 12 months of SIP
        for (let month = 1; month <= 12; month++) {
            totalInvested += currentInvestment;
            const monthsRemaining = (years - year) * 12 + (12 - month + 1);
            totalValue += currentInvestment * Math.pow(1 + monthlyRate, monthsRemaining);
        }
        currentInvestment *= stepUpMultiplier; // Increase SIP for next year
    }

    const estimatedReturns = totalValue - totalInvested;

    return {
        totalInvested,
        estimatedReturns,
        totalValue
    };
}

// Calculate Lumpsum
function calculateLumpsum(principal, annualReturn, years) {
    // A = P × (1 + r)^n
    const totalInvested = principal;
    const totalValue = principal * Math.pow(1 + annualReturn / 100, years);
    const estimatedReturns = totalValue - totalInvested;
    
    return {
        totalInvested: totalInvested,
        estimatedReturns: estimatedReturns,
        totalValue: totalValue
    };
}

// Update results display
function updateResults() {
    let result;
    
    if (currentMode === 'SIP') {
        const monthlyInvestment = parseFloat(document.getElementById('monthlyInvestment').value);
        const annualReturn = parseFloat(document.getElementById('expectedReturn').value);
        const years = parseInt(document.getElementById('timePeriod').value);
        const stepUpPercent = parseFloat(document.getElementById('sipStepup').value);

        result = calculateSIP(monthlyInvestment, annualReturn, years, stepUpPercent);
    } else {
        const lumpsumAmount = parseFloat(document.getElementById('lumpsumAmount').value);
        const annualReturn = parseFloat(document.getElementById('lumpsumReturn').value);
        const years = parseInt(document.getElementById('lumpsumPeriod').value);
        
        result = calculateLumpsum(lumpsumAmount, annualReturn, years);
    }
    
    // Update display
    document.getElementById('investedAmount').textContent = formatCurrency(result.totalInvested);
    document.getElementById('estimatedReturns').textContent = formatCurrency(result.estimatedReturns);
    document.getElementById('totalValue').textContent = formatCurrency(result.totalValue);
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
    if (currentMode === 'SIP') {
        const monthlyInvestment = parseFloat(document.getElementById('monthlyInvestment').value);
        const annualReturn = parseFloat(document.getElementById('expectedReturn').value);
        const years = parseInt(document.getElementById('timePeriod').value);
        const stepUpPercent = parseFloat(document.getElementById('sipStepup').value);

        document.getElementById('sipStepupDisplay').value = formatPercentage(stepUpPercent);
        document.getElementById('monthlyInvestmentDisplay').value = formatCurrency(monthlyInvestment);
        document.getElementById('expectedReturnDisplay').value = formatPercentage(annualReturn);
        document.getElementById('timePeriodDisplay').value = formatYears(years);
        
        updateSliderFill('monthlyInvestment', 'monthlyInvestmentFill');
        updateSliderFill('expectedReturn', 'expectedReturnFill');
        updateSliderFill('timePeriod', 'timePeriodFill');
        updateSliderFill('sipStepup', 'sipStepupFill');
    } else {
        const lumpsumAmount = parseFloat(document.getElementById('lumpsumAmount').value);
        const annualReturn = parseFloat(document.getElementById('lumpsumReturn').value);
        const years = parseInt(document.getElementById('lumpsumPeriod').value);
        
        document.getElementById('lumpsumAmountDisplay').value = formatCurrency(lumpsumAmount);
        document.getElementById('lumpsumReturnDisplay').value = formatPercentage(annualReturn);
        document.getElementById('lumpsumPeriodDisplay').value = formatYears(years);
        
        updateSliderFill('lumpsumAmount', 'lumpsumAmountFill');
        updateSliderFill('lumpsumReturn', 'lumpsumReturnFill');
        updateSliderFill('lumpsumPeriod', 'lumpsumPeriodFill');
    }
    
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

// Toggle between SIP and Lumpsum
document.getElementById('sipToggle').addEventListener('click', function() {
    currentMode = 'SIP';
    document.getElementById('sipToggle').classList.add('active');
    document.getElementById('lumpsumToggle').classList.remove('active');
    document.getElementById('sipInputs').classList.remove('hidden');
    document.getElementById('lumpsumInputs').classList.add('hidden');
    updateDisplays();
});

document.getElementById('lumpsumToggle').addEventListener('click', function() {
    currentMode = 'LUMPSUM';
    document.getElementById('lumpsumToggle').classList.add('active');
    document.getElementById('sipToggle').classList.remove('active');
    document.getElementById('lumpsumInputs').classList.remove('hidden');
    document.getElementById('sipInputs').classList.add('hidden');
    updateDisplays();
});

// SIP sliders event listeners
document.getElementById('monthlyInvestment').addEventListener('input', updateDisplays);
document.getElementById('expectedReturn').addEventListener('input', updateDisplays);
document.getElementById('timePeriod').addEventListener('input', updateDisplays);
document.getElementById('sipStepup').addEventListener('input', updateDisplays);

// Lumpsum sliders event listeners
document.getElementById('lumpsumAmount').addEventListener('input', updateDisplays);
document.getElementById('lumpsumReturn').addEventListener('input', updateDisplays);
document.getElementById('lumpsumPeriod').addEventListener('input', updateDisplays);

// SIP display input event listeners (editable fields)
document.getElementById('monthlyInvestmentDisplay').addEventListener('blur', function() {
    updateFromDisplay('monthlyInvestmentDisplay', 'monthlyInvestment', 'currency');
});
document.getElementById('expectedReturnDisplay').addEventListener('blur', function() {
    updateFromDisplay('expectedReturnDisplay', 'expectedReturn', 'percentage');
});
document.getElementById('timePeriodDisplay').addEventListener('blur', function() {
    updateFromDisplay('timePeriodDisplay', 'timePeriod', 'years');
});

// Lumpsum display input event listeners (editable fields)
document.getElementById('lumpsumAmountDisplay').addEventListener('blur', function() {
    updateFromDisplay('lumpsumAmountDisplay', 'lumpsumAmount', 'currency');
});
document.getElementById('lumpsumReturnDisplay').addEventListener('blur', function() {
    updateFromDisplay('lumpsumReturnDisplay', 'lumpsumReturn', 'percentage');
});
document.getElementById('lumpsumPeriodDisplay').addEventListener('blur', function() {
    updateFromDisplay('lumpsumPeriodDisplay', 'lumpsumPeriod', 'years');
});

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    updateDisplays();
});
