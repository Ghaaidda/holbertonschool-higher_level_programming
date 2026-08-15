const ele = document.querySelector('#update_header');
ele.addEventListener('click', function () {
    const header = document.querySelector('header');
    header.textContent = 'New Header!!!';
});