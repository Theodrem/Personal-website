const nav = document.querySelector('nav');
const title = document.querySelector('#title');
const head = document.querySelector('#head');
const logo = document.querySelector('#theo');


window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            nav.classList.add('scroll');
            title.classList.add('disparition');
            head.classList.add('disparition')
            logo.classList.add('color');
        }

        else if (window.scrollY < 250) {
            nav.classList.remove('scroll');
            title.classList.remove('disparition');
            head.classList.remove('disparition');
            logo.classList.remove('color');

        }
});