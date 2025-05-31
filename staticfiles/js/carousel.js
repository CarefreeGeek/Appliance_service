const carousel = document.querySelector('.carousel');
const items = document.querySelectorAll('.carousel-item');
const prev = document.getElementById('prev');
const next = document.getElementById('next');
let index = 0;

function updateCarousel() {
    carousel.style.transform = `translateX(${-index * 100}%)`;
}

prev.addEventListener('click', () => {
    index = (index > 0) ? index - 1 : items.length - 1;
    updateCarousel();
});

next.addEventListener('click', () => {
    index = (index < items.length - 1) ? index + 1 : 0;
    updateCarousel();
});
