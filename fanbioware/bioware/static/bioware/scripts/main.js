// Header handler
(function (){
    const header = document.querySelector('.header');
    var lastScroll = 0;
    window.onscroll = () => {
        let currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
        if (currentScroll == 0) {
            header.classList.remove('header_active', 'header_hidden');
        } else if (currentScroll > 0 && lastScroll <= currentScroll){
            lastScroll = currentScroll;
            header.classList.remove('header_active');
            header.classList.add('header_hidden');
        } else {
            lastScroll = currentScroll;
            header.classList.remove('header_hidden');
            header.classList.add('header_active');
        }
    }
}());

// Burger handler
(function (){
    const burgerItem = document.querySelector('.header__burger');
    const menu = document.querySelector('.header__nav');
    burgerItem.addEventListener('click', () => {
        if (menu.classList.contains('header__nav_active')) {
            menu.classList.remove('header__nav_active');
            burgerItem.innerHTML = 'Menu'
        } else {
            menu.classList.add('header__nav_active');
            burgerItem.innerHTML = 'Close'
        }
    },
    {passive: true});
}());
