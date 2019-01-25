

let buttons = document.querySelectorAll('.flavor');

// buttons.forEach(function(button){
//     console.log('button', button)
// });

buttons.forEach(churnDate);

function churnDate(button) {
    button.addEventListener('click', toggleClass);
}

function toggleClass(event) {
    let button = event.target;
    button.addEventListener('click', button.classList.add('hidden'));
}
//////////////////////////////////////////
//
// document.getElementById('demo').onclick = function () {myFunction()
//
// };
//
// function myFunction() {
//     document.getElementById('demo').innerHTML = 'SO FRESH'
//
// }
//
// /////////////////////////////////////
//
// {{flavor.date_churned}}


///////////////////////////FROM CLOCK CODE. HERE AS A REFERENCE////////////////
//
// document.getElementById('time').onmouseover = function () {mouseOver()};
// document.getElementById('time').onmouseout = function() {mouseOut()};
//
// function mouseOver(){
//     document.getElementById('time').toString(num);
//     //some sort of function to change value to hex
// }
//
// function mouseOut() {
//     document.getElementById('time').toString(num);
// }
////////////////////////////////////////////////////////////////////////////////