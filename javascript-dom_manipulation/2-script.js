function red_class() {
    const header = document.querySelector("header")
    header.classList.add("red")
}

const id = document.querySelector("#red_header") //css ID selector
id.addEventListener("click", red_class)