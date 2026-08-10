function toggle() {
    const header = document.querySelector("header")
    if (header.classList.contains("red")) {
        header.classList.remove("red")
        header.classList.add("green")
    } else {
        header.classList.add("red")
        header.classList.remove("green")
    }
}

const toggle_header = document.querySelector("#toggle_header") //css ID selector

toggle_header.addEventListener("click", toggle)