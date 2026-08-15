function addItem() {
    const list = document.querySelector('.my_list');
    list.insertAdjacentHTML('beforeend', '<li>Item</li>');
}

const add_item = document.querySelector('#add_item');
add_item.addEventListener('click', addItem);