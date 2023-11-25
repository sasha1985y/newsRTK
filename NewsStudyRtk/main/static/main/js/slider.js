const upBtn = document.querySelector('.rs-up-button');
const downBtn = document.querySelector('.rs-down-button');
const sidebar = document.querySelector('.rs-sidebar');
const container = document.querySelector('.rs-container');

const mainSlide = document.querySelector('.rs-main-slide')
const slidesCount = mainSlide.querySelectorAll('div').length;

let activeSlideIndex = 0;

sidebar.style.top = `-${(slidesCount - 1) * 100}vh`;

upBtn.addEventListener('click', () => {
    changeSlide('up');
})

downBtn.addEventListener('click', () => {
    changeSlide('down');
})

document.addEventListener('keydown', evt => {
    if (evt.key === 'RsArrowUp') {
        changeSlide('up');
    } else if (evt.key === 'RsArrowDown') {
        changeSlide('down');
    }
})

function changeSlide(direction) {
    if (direction === 'up') {
        activeSlideIndex++;
        if (activeSlideIndex === slidesCount) {
            {
                activeSlideIndex = 0;
            }
        }
    } else if (direction === 'down') {
      activeSlideIndex--;
      if (activeSlideIndex < 0) {
        activeSlideIndex = slidesCount - 1;
      }
    }

    const height = container.clientHeight;

    mainSlide.style.transform = `translateY(-${activeSlideIndex * height}px)`;

    sidebar.style.transform = `translateY(${activeSlideIndex * height}px)`;
}