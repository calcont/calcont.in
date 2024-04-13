// function readCookie(name) {
//     var nameEQ = name + '='
//     var ca = document.cookie.split(';')
//     for (var i = 0; i < ca.length; i++) {
//         var c = ca[i]
//         while (c.charAt(0) == ' ') c = c.substring(1, c.length)
//         if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length)
//     }
// }
//
// function setexpire() {
//     var date1 = new Date()
//
//     date1.setTime(new Date(date1.getFullYear(), date1.getMonth(), date1.getDate(), date1.getHours() + 48))
//
//     var x = Math.floor(Math.random() * 1000 + 1)
//
//     document.cookie = 'PopCookie' + '=' + x + '; ' + 'expires=' + date1.toUTCString() + ';path=/'
// }
//
// function setexpire_1Month() {
//     var date1 = new Date()
//
//     date1.setTime(new Date(date1.getFullYear(), date1.getMonth() + 1, date1.getDate(), date1.getHours(), date1.getMinutes()))
//
//     var x = Math.floor(Math.random() * 1000 + 1)
//
//     document.cookie = 'PopCookie' + '=' + x + '; ' + 'expires=' + date1.toUTCString() + ';path=/'
// }
//
// var myCookie = readCookie('PopCookie')
//
// if (myCookie == undefined) {
//     // code to show modal here
//     setTimeout(function () {
//         $('#DoLogin').modal('show')
//     }, 50000)
// }
// $('#mbdy').click(function (e) {
//     window.open('https://draw.calcont.in/')
//     setexpire_1Month()
//     $('#DoLogin').modal('hide')
// })
// $('#closeP').click(function (e) {
//     setexpire_1Month()
//     $('#DoLogin').modal('hide')
// })
// $('.signin').click(function (e) {
//     setexpire_1Month()
//     $('#DoLogin').modal('hide')
// })