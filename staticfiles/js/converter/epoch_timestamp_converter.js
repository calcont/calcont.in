const epochInput = document.getElementById('epochInput');
const dateInput = document.getElementById('dateInput');
const datePicker = document.getElementById('datePicker');
const timePicker = document.getElementById('timePicker');
const timezoneSelect = document.getElementById('timezoneSelect');
const utcOutput = document.getElementById('utcOutput');
const istOutput = document.getElementById('istOutput');
const epochOutput = document.getElementById('epochOutput');
const currentTimeBtn = document.getElementById('currentTimeBtn');

// IST offset: UTC+5:30 (in milliseconds)
const IST_OFFSET_MS = 5.5 * 60 * 60 * 1000;

// Function to format date time string
function formatDateTime(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

// Function to convert epoch to UTC datetime
function epochToUTC(epoch) {
    const date = new Date(epoch * 1000); // Convert seconds to milliseconds
    return formatDateTime(date);
}

// Function to convert epoch to IST datetime
function epochToIST(epoch) {
    const date = new Date(epoch * 1000);
    const istDate = new Date(date.getTime() + IST_OFFSET_MS);
    return formatDateTime(istDate);
}

// Function to convert UTC datetime to epoch
function utcToEpoch(dateTimeString) {
    try {
        // Parse the datetime string (YYYY-MM-DD HH:MM:SS)
        const [datePart, timePart] = dateTimeString.split(' ');
        const [year, month, day] = datePart.split('-').map(Number);
        const [hours, minutes, seconds] = timePart.split(':').map(Number);
        
        const date = new Date(Date.UTC(year, month - 1, day, hours, minutes, seconds));
        return Math.floor(date.getTime() / 1000);
    } catch (e) {
        return null;
    }
}

// Function to convert IST datetime to epoch
function istToEpoch(dateTimeString) {
    try {
        // Parse the datetime string (YYYY-MM-DD HH:MM:SS)
        const [datePart, timePart] = dateTimeString.split(' ');
        const [year, month, day] = datePart.split('-').map(Number);
        const [hours, minutes, seconds] = timePart.split(':').map(Number);
        
        // Create date in local time (IST)
        const date = new Date(year, month - 1, day, hours, minutes, seconds);
        // Convert to UTC epoch by subtracting IST offset
        const utcTime = date.getTime() - IST_OFFSET_MS;
        return Math.floor(utcTime / 1000);
    } catch (e) {
        return null;
    }
}

// Function to parse datetime string
function parseDateTime(dateTimeString) {
    // Support multiple formats: YYYY-MM-DD HH:MM:SS or YYYY-MM-DD
    const formats = [
        /^(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})$/,
        /^(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})$/,
        /^(\d{4})-(\d{2})-(\d{2})$/
    ];
    
    for (let format of formats) {
        const match = dateTimeString.match(format);
        if (match) {
            const year = parseInt(match[1]);
            const month = parseInt(match[2]) - 1;
            const day = parseInt(match[3]);
            const hours = match[4] ? parseInt(match[4]) : 0;
            const minutes = match[5] ? parseInt(match[5]) : 0;
            const seconds = match[6] ? parseInt(match[6]) : 0;
            return { year, month, day, hours, minutes, seconds };
        }
    }
    return null;
}

// Function to get datetime string from date/time pickers or manual input
function getDateTimeString() {
    // Check if date and time pickers have values
    if (datePicker.value && timePicker.value) {
        // Combine date and time pickers
        const datePart = datePicker.value; // Format: YYYY-MM-DD
        const timePart = timePicker.value; // Format: HH:MM or HH:MM:SS
        // Ensure time has seconds
        const timeParts = timePart.split(':');
        if (timeParts.length === 2) {
            return `${datePart} ${timePart}:00`;
        }
        return `${datePart} ${timePart}`;
    }
    // Fall back to manual text input
    return dateInput.value.trim();
}

// Sync date/time pickers with manual input (optional helper)
function syncPickersFromManualInput() {
    const manualValue = dateInput.value.trim();
    if (manualValue) {
        const parsed = parseDateTime(manualValue);
        if (parsed) {
            const year = parsed.year;
            const month = String(parsed.month + 1).padStart(2, '0');
            const day = String(parsed.day).padStart(2, '0');
            datePicker.value = `${year}-${month}-${day}`;
            
            const hours = String(parsed.hours).padStart(2, '0');
            const minutes = String(parsed.minutes).padStart(2, '0');
            const seconds = String(parsed.seconds).padStart(2, '0');
            timePicker.value = `${hours}:${minutes}:${seconds}`;
        }
    }
}

// Sync manual input from date/time pickers
function syncManualInputFromPickers() {
    if (datePicker.value && timePicker.value) {
        const datePart = datePicker.value;
        const timePart = timePicker.value;
        const timeParts = timePart.split(':');
        if (timeParts.length === 2) {
            dateInput.value = `${datePart} ${timePart}:00`;
        } else {
            dateInput.value = `${datePart} ${timePart}`;
        }
    }
}

// Event listeners for date/time pickers
datePicker.addEventListener('change', syncManualInputFromPickers);
timePicker.addEventListener('change', syncManualInputFromPickers);
dateInput.addEventListener('change', syncPickersFromManualInput);

// Main conversion function
$('.con').click(function (e) {
    e.preventDefault();
    
    const epochValue = epochInput.value.trim();
    const dateValue = getDateTimeString();
    const timezone = timezoneSelect.value;
    
    // Clear outputs
    utcOutput.value = '';
    istOutput.value = '';
    epochOutput.value = '';
    
    if (epochValue && dateValue) {
        // If both are provided, prioritize epoch
        convertFromEpoch(epochValue);
    } else if (epochValue) {
        // Convert from epoch to datetime
        convertFromEpoch(epochValue);
    } else if (dateValue) {
        // Convert from datetime to epoch
        convertFromDateTime(dateValue, timezone);
    } else {
        utcOutput.value = 'Please enter either epoch timestamp or datetime';
        istOutput.value = '';
        epochOutput.value = '';
    }
});

function convertFromEpoch(epochStr) {
    const epoch = parseFloat(epochStr);
    
    if (isNaN(epoch) || epoch < 0) {
        utcOutput.value = 'Invalid epoch timestamp';
        istOutput.value = '';
        epochOutput.value = '';
        return;
    }
    
    const utcDateTime = epochToUTC(epoch);
    const istDateTime = epochToIST(epoch);
    
    utcOutput.value = utcDateTime;
    istOutput.value = istDateTime;
    epochOutput.value = Math.floor(epoch).toString();
}

function convertFromDateTime(dateTimeStr, timezone) {
    const parsed = parseDateTime(dateTimeStr);
    
    if (!parsed) {
        utcOutput.value = 'Invalid datetime format. Use YYYY-MM-DD HH:MM:SS';
        istOutput.value = '';
        epochOutput.value = '';
        return;
    }
    
    let epoch;
    
    if (timezone === 'IST') {
        epoch = istToEpoch(dateTimeStr);
    } else {
        epoch = utcToEpoch(dateTimeStr);
    }
    
    if (epoch === null || isNaN(epoch)) {
        utcOutput.value = 'Error converting datetime to epoch';
        istOutput.value = '';
        epochOutput.value = '';
        return;
    }
    
    // Display both UTC and IST
    const utcDateTime = epochToUTC(epoch);
    const istDateTime = epochToIST(epoch);
    
    utcOutput.value = utcDateTime;
    istOutput.value = istDateTime;
    epochOutput.value = epoch.toString();
    
    // Also update epoch input for reference
    epochInput.value = epoch.toString();
}

// Current time button
currentTimeBtn.addEventListener('click', function(e) {
    e.preventDefault();
    const now = new Date();
    const currentEpoch = Math.floor(now.getTime() / 1000);
    
    epochInput.value = currentEpoch.toString();
    dateInput.value = '';
    
    convertFromEpoch(currentEpoch.toString());
});

