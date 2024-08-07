// script that updates the text color of the <header> element to red
document.addEventListener("DOMContentLoaded", function() {
    var header = document.querySelector("header");
    if (header) {
        header.style.color = "#FF0000";
    }
});
