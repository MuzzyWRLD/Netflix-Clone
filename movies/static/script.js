let navbar = document.querySelector('.obere-leiste');
window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
        navbar.classList.add('nav-schwarz');
    } else {
        navbar.classList.remove('nav-schwarz');
    }
});

let filmRegal = document.querySelector('.filme-reihe');
filmRegal.addEventListener('wheel', function(ereignis) {
    ereignis.preventDefault();
    filmRegal.scrollLeft = filmRegal.scrollLeft + ereignis.deltaY;
});
