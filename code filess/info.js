const navbar = document.querySelector('.navbar');
window.onscroll = () => {
    if (window.scrolly > 300) {
        navbar.classList.add('nav-active');
    } else {
        navbar.classList.remove('nav-active');
    }
}