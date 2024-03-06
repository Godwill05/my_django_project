document.addEventListener("DOMContentLoaded", function() {
    var inputs = document.querySelectorAll("#container input");
    inputs.forEach(function(input, index) {
        if ((index + 1) % 2 === 0) {
            input.style.float = "right";
        } else {
            input.style.float = "left";
        }
    });
});
