const open_model = document.getElementById('btn');
const close = document.getElementById('close');
const modal = document.getElementById('modal-okno');

open_model.addEventListener('click', function(){
    modal.classList.add('active');
})

close.addEventListener('click', ()=>{
    modal.classList.remove('active');
})

const open_model1 = document.getElementById('btn1');
const close1 = document.getElementById('close1');
const modal1 = document.getElementById('modal-okno1');

open_model1.addEventListener('click', function(){
    modal1.classList.add('active');
})

close1.addEventListener('click', ()=>{
    modal1.classList.remove('active');
})

const open_model2 = document.getElementById('btn2');
const close2 = document.getElementById('close2');
const modal2 = document.getElementById('modal-okno2');

open_model2.addEventListener('click', function(){
    modal2.classList.add('active');
})

close2.addEventListener('click', ()=>{
    modal2.classList.remove('active');
})

const open_model3 = document.getElementById('btn3');
const close3 = document.getElementById('close3');
const modal3 = document.getElementById('modal-okno3');

open_model3.addEventListener('click', function(){
    modal3.classList.add('active');
})

close3.addEventListener('click', ()=>{
    modal3.classList.remove('active');
})

const open_model4 = document.getElementById('btn4');
const close4 = document.getElementById('close4');
const modal4 = document.getElementById('modal-okno4');

open_model4.addEventListener('click', function(){
    modal4.classList.add('active');
})

close4.addEventListener('click', ()=>{
    modal4.classList.remove('active');
})

let  counter = 1;
setInterval(function(){
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if(counter > 3){
        counter = 1
    }
}, 6000)

document.querySelector('#btn4').setAttribute("disabled", "true")

