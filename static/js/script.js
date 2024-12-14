document.addEventListener("DOMContentLoaded", () => {
    document.oncontextmenu = function () {
        alert("Function Disabled!");
        return false;
    };
});
