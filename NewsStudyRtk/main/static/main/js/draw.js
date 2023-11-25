const items = document.querySelectorAll('.rs-draw-item');
const placeholders = document.querySelectorAll('.rs-draw-placeholder');

for (const item of items) {
    item.addEventListener('dragstart', dragStart);
    item.addEventListener('dragend', dragEnd);
}

for (const placeholder of placeholders) {
    placeholder.addEventListener('dragover', dragOver);
    placeholder.addEventListener('dragenter', dragEnter);
    placeholder.addEventListener('dragleave', dragLeave);
    placeholder.addEventListener('drop', dragDrop);
}

function dragStart(evt) {
    for (const item of items) {
        if (evt.target === item) {
            item.classList.add('rs-draw-hold');
            setTimeout(() => item.classList.add('rs-draw-hide'), 0);
        }
    }
}

function dragEnd(evt) {
    for (const item of items) {
        if (evt.target === item) {
            item.className = 'rs-draw-item';
        }
    }
}

function dragOver(evt) {
    evt.preventDefault();
}

function dragEnter(evt) {
    evt.target.classList.add('rs-draw-hovered');
}

function dragLeave(evt) {
    evt.target.classList.remove('rs-draw-hovered');
}

function dragDrop(evt) {
    evt.preventDefault();
    const draggedItem = document.querySelector('.rs-draw-hold');
    for (const placeholder of placeholders) {
        if (placeholder.classList.contains('rs-draw-hovered')) {
            placeholder.appendChild(draggedItem);
            placeholder.classList.remove('rs-draw-hovered');
            draggedItem.classList.remove('rs-draw-hide');
            break;
        }
    }
}