const carousel = document.querySelector(".carousel-secondary");
const arrowBtns = document.querySelectorAll(".wrapper-carousel i");
let carouselChildren = [...carousel.children];
const cardCount = carouselChildren.length;

let isDragging = false, startX, startScrollLeft;

function getFirstCardWidth() {
    return carousel.querySelector("ul > li.card-secondary").offsetWidth; // 1st secondary-card
}

function getCardPerView() {
    return Math.round(carousel.offsetWidth / getFirstCardWidth());
}

// Add event listeners for the arrow buttons to scroll the carousel left and right
function addArrowButtonListeners() {
    arrowBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            let firstCardWidth = getFirstCardWidth();
            carousel.scrollLeft += btn.id === "left" ? -firstCardWidth : firstCardWidth;

            if (btn.id === "left") {
                // Remove the last card and add it to the beginning
                let lastCard = carouselChildren.pop();
                carouselChildren.unshift(lastCard);
                carousel.insertBefore(lastCard, carousel.firstChild);
            } else {
                // Remove the first card and add it to the end
                let firstCard = carouselChildren.shift();
                carouselChildren.push(firstCard);
                carousel.removeChild(firstCard);
                carousel.appendChild(firstCard);
            }
        });
    });
}

function checkArrowVisibility() {
    let cardPerView = getCardPerView();
    if (cardCount >= cardPerView) {
        arrowBtns.forEach(btn => btn.style.display = "block");
    } else {
        arrowBtns.forEach(btn => btn.style.display = "none");
    }
}

const dragStart = (e) => {
    isDragging = true;
    carousel.classList.add("dragging");
    startX = e.pageX;
    startScrollLeft = carousel.scrollLeft;
}

const dragging = (e) => {
    if(!isDragging) return;
    carousel.scrollLeft = startScrollLeft - (e.pageX - startX);
}

const dragStop = () => {
    isDragging = false;
    carousel.classList.remove("dragging");
}

addArrowButtonListeners();
window.addEventListener("load", checkArrowVisibility);
window.addEventListener("resize", checkArrowVisibility);
carousel.addEventListener("mousedown", dragStart);
carousel.addEventListener("mousemove", dragging);
document.addEventListener("mouseup", dragStop);