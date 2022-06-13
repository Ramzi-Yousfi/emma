const btn = document.querySelector('.menu-humberger');
const nav_links = document.querySelector('.nav_links');
const  i1 = document.querySelector('.menu1');
const  i2 = document.querySelector('.menu2');

btn.addEventListener('click', () => {
    nav_links.classList.toggle('open');
    i1.classList.toggle('hide');
    i2.classList.toggle('show');
});

const sub_menu = document.querySelector('.sub') ;
const sub_btn  = document.querySelector('.sub_btn');

sub_btn.addEventListener('click', () => {
    console.log('clicked');
    sub_menu.classList.toggle('showing');
});
