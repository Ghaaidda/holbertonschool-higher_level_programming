document.addEventListener('DOMContentLoaded', () => { // To ensure the DOM is loaded before fetching
fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
    .then(response => response.json())
    .then(data => {
        const hello = document.querySelector("#hello");
        hello.textContent = data.hello;
    })
    .catch(error => {
        console.error('Error fetching greeting:', error);
    });
});