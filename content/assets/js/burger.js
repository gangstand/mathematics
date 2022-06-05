const burger = document.querySelector('#burger')
const symbol = burger.querySelector('.menu')
const navbar = document.querySelector('#navbar')

const main = document.querySelector('main')
const footer = document.querySelector('footer')

function setMenu() {
    const isOpen = !navbar.classList.contains('none')

    if(isOpen) {
        symbol.classList.remove('cross')
        navbar.classList.add('none')
        

        main.classList.remove('none')
        footer.classList.remove('none')
    } else {
        symbol.classList.add('cross')
        navbar.classList.remove('none')

        main.classList.add('none')
        footer.classList.add('none')
    }
}

burger.addEventListener('click', setMenu)