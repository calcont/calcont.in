$('.cal').click(function (e) {
    e.preventDefault();
    var nos = document.getElementById("numbers").value.split(",");
    document.getElementById("hcf").value = getHcf(nos);
    document.getElementById("lcm").value = getLcm(nos);
    function getHcf(arr) {
        if (arr.length == 1) {
            return arr[0]
        }
        var g = getGcd(arr[0], arr[1]);
        if (arr.length == 2) {
            return g
        }
        for (let i = 1; i < arr.length; i++) {
            g = getGcd(g, arr[i + 1]);
            if (g == 1) {
                return 1;
            }

        }
        return g
    }
    function getLcm(arr) {
        let ans = arr[0];
        for (let i = 1; i < arr.length; i++)
            ans = (((arr[i] * ans))/(getGcd(arr[i], ans)));

        return ans;
    }

});

function getGcd(x, y) {
    x = Math.abs(x);
    y = Math.abs(y);
    while (y) {
        var t = y;
        y = x % y;
        x = t;
    }
    return x;
}