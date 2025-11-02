const istDatePicker = document.getElementById('istDatePicker');
const istTimePicker = document.getElementById('istTimePicker');
const utcDatePicker = document.getElementById('utcDatePicker');
const utcTimePicker = document.getElementById('utcTimePicker');
const currentTimeBtn = document.getElementById('currentTimeBtn');

// IST offset: UTC+5:30 (in milliseconds)
const IST_OFFSET_MS = 5.5 * 60 * 60 * 1000;

// Flag to prevent infinite loops during updates
let isUpdating = false;

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

// Function to get IST datetime from pickers
function getISTDateTime() {
    if (!istDatePicker.value || !istTimePicker.value) {
        return null;
    }
    const datePart = istDatePicker.value; // YYYY-MM-DD
    const timePart = istTimePicker.value; // HH:MM
    // Always add seconds as 00 since we removed seconds from time picker
    return `${datePart} ${timePart}:00`;
}

// Function to get UTC datetime from pickers
function getUTCDateTime() {
    if (!utcDatePicker.value || !utcTimePicker.value) {
        return null;
    }
    const datePart = utcDatePicker.value; // YYYY-MM-DD
    const timePart = utcTimePicker.value; // HH:MM
    // Always add seconds as 00 since we removed seconds from time picker
    return `${datePart} ${timePart}:00`;
}

// Function to parse datetime string
function parseDateTime(dateTimeString) {
    if (!dateTimeString) return null;
    
    const formats = [
        /^(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})$/,
        /^(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})$/
    ];
    
    for (let format of formats) {
        const match = dateTimeString.match(format);
        if (match) {
            const year = parseInt(match[1]);
            const month = parseInt(match[2]) - 1;
            const day = parseInt(match[3]);
            const hours = parseInt(match[4]) || 0;
            const minutes = parseInt(match[5]) || 0;
            const seconds = parseInt(match[6]) || 0;
            return { year, month, day, hours, minutes, seconds };
        }
    }
    return null;
}

// Function to convert IST to UTC
function istToUTC(dateTimeString) {
    try {
        const parsed = parseDateTime(dateTimeString);
        if (!parsed) return null;
        
        // Create date treating input as IST (local time in IST context)
        // Since IST is UTC+5:30, we need to subtract the offset
        const istDate = new Date(parsed.year, parsed.month, parsed.day, parsed.hours, parsed.minutes, parsed.seconds);
        const utcDate = new Date(istDate.getTime() - IST_OFFSET_MS);
        return formatDateTime(utcDate);
    } catch (e) {
        return null;
    }
}

// Function to convert UTC to IST
function utcToIST(dateTimeString) {
    try {
        const parsed = parseDateTime(dateTimeString);
        if (!parsed) return null;
        
        // Create date in UTC
        const utcDate = new Date(Date.UTC(parsed.year, parsed.month, parsed.day, parsed.hours, parsed.minutes, parsed.seconds));
        // Add IST offset
        const istDate = new Date(utcDate.getTime() + IST_OFFSET_MS);
        return formatDateTime(istDate);
    } catch (e) {
        return null;
    }
}

// Update UTC pickers from IST
function updateUTCFromIST() {
    if (isUpdating) return;
    
    const istDateTime = getISTDateTime();
    if (!istDateTime) return;
    
    isUpdating = true;
    
    const utcDateTime = istToUTC(istDateTime);
    if (utcDateTime) {
        const parsed = parseDateTime(utcDateTime);
        if (parsed) {
            const year = parsed.year;
            const month = String(parsed.month + 1).padStart(2, '0');
            const day = String(parsed.day).padStart(2, '0');
            utcDatePicker.value = `${year}-${month}-${day}`;
            
            const hours = String(parsed.hours).padStart(2, '0');
            const minutes = String(parsed.minutes).padStart(2, '0');
            // Only set hours and minutes, no seconds
            utcTimePicker.value = `${hours}:${minutes}`;
        }
    }
    
    isUpdating = false;
}

// Update IST pickers from UTC
function updateISTFromUTC() {
    if (isUpdating) return;
    
    const utcDateTime = getUTCDateTime();
    if (!utcDateTime) return;
    
    isUpdating = true;
    
    const istDateTime = utcToIST(utcDateTime);
    if (istDateTime) {
        const parsed = parseDateTime(istDateTime);
        if (parsed) {
            const year = parsed.year;
            const month = String(parsed.month + 1).padStart(2, '0');
            const day = String(parsed.day).padStart(2, '0');
            istDatePicker.value = `${year}-${month}-${day}`;
            
            const hours = String(parsed.hours).padStart(2, '0');
            const minutes = String(parsed.minutes).padStart(2, '0');
            // Only set hours and minutes, no seconds
            istTimePicker.value = `${hours}:${minutes}`;
        }
    }
    
    isUpdating = false;
}

// Event listeners for IST pickers
istDatePicker.addEventListener('change', function() {
    updateUTCFromIST();
});

istTimePicker.addEventListener('change', function() {
    updateUTCFromIST();
});

istDatePicker.addEventListener('input', function() {
    updateUTCFromIST();
});

istTimePicker.addEventListener('input', function() {
    updateUTCFromIST();
});

// Event listeners for UTC pickers
utcDatePicker.addEventListener('change', function() {
    updateISTFromUTC();
});

utcTimePicker.addEventListener('change', function() {
    updateISTFromUTC();
});

utcDatePicker.addEventListener('input', function() {
    updateISTFromUTC();
});

utcTimePicker.addEventListener('input', function() {
    updateISTFromUTC();
});

// Current time button - set to current IST time
currentTimeBtn.addEventListener('click', function(e) {
    e.preventDefault();
    isUpdating = true;
    
    // Get current time and convert to IST
    // Since we want to show current IST time, we get local time and treat it as IST
    const now = new Date();
    
    // Set IST pickers
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    istDatePicker.value = `${year}-${month}-${day}`;
    
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    // Only set hours and minutes, no seconds
    istTimePicker.value = `${hours}:${minutes}`;
    
    // Update UTC from IST
    isUpdating = false;
    updateUTCFromIST();
});

// Initialize with current time on page load
window.addEventListener('DOMContentLoaded', function() {
    isUpdating = true;
    
    const now = new Date();
    
    // Set IST pickers to current time
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    istDatePicker.value = `${year}-${month}-${day}`;
    
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    // Only set hours and minutes, no seconds
    istTimePicker.value = `${hours}:${minutes}`;
    
    isUpdating = false;
    updateUTCFromIST();
});
