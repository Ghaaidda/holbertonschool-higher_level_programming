function red_header() {
    const header = document.querySelector("header")
    header.style.color = "#FF0000"
}

const id = document.querySelector("#red_header") //css ID selector
id.addEventListener("click", red_header)