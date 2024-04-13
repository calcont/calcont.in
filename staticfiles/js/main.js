const modalCookieName = "modalCookie";
const defaultExpireTime = 1000 * 60 * 60 * 24 * 7; // 7 days
const testExpireTime = 1000 * 60 * 1; // 1 minute
const modalShowTime = 5000; // 50 seconds
const cookieValue = readCookie(modalCookieName);
const modalBody = document.getElementById("ad-body");
const modalClose = document.getElementById("ad-close-btn");
const modalLink = document.getElementById("ad-link");

function modalShow() {
    if (cookieValue === "") {
        setTimeout(function () {
            $('#self-ad').modal('show');
        }, modalShowTime)
    }
}

function addListeners() {
    modalClose.addEventListener('click', handleClose);
    modalBody.addEventListener('click', () => {
        handleClose(modalLink.getAttribute('href'));
    });
}

function handleClose(link) {
    if (typeof link === "string") {
        window.open(link, "_blank");
    }
    $('#self-ad').modal('hide');
    createCookie();
}

function readCookie(name) {
    const allCookies = document.cookie;
    const regex = '(^|;)\\s*' + name + '\\s*=\\s*([^;]+)';
    return allCookies.match(regex) || "";
}


function createCookie(expireTime) {
    const date = new Date();
    expireTime = expireTime || defaultExpireTime;
    date.setTime(date.getTime() + expireTime);
    document.cookie = modalCookieName + "=true; expires=" + date.toUTCString() + "; path=/";
}

function init() {
    modalShow();
    addListeners();
}

// init();