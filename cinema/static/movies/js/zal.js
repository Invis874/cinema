var reply_click = function()
{
    document.write('1')
}
const btn1 = document.getElementById('1').onclick = reply_click;
const btn2 = document.getElementById('2').onclick = reply_click;
const btn3 = document.getElementById('3').onclick = reply_click;

export { btn1 };