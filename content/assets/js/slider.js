const slider = document.querySelector('#slider')
const line = slider.querySelector('.slider__line')
line.style.left = '10px'

console.dir(line)

const nextBtn = document.querySelector('#next')
const backBtn = document.querySelector('#back')

const step = slider.querySelector('.slider__item').clientWidth + 20
const sum = slider.querySelectorAll('.slider__item').length - Math.floor(slider.clientWidth/step)
console.log(sum);
let counter = 0

function next() {  
    if(counter < sum) {
        line.style.left = (parseInt(line.style.left.replace('px', '')) - step) +'px'
        counter++
    } 
}

function back() {  
    if(counter > 0) {
        line.style.left = (parseInt(line.style.left.replace('px', '')) + step) +'px'
        counter--
    } 
}

nextBtn.addEventListener('click', next)
backBtn.addEventListener('click', back)

