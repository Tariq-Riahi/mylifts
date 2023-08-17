document.addEventListener("DOMContentLoaded", function () {
    const toggleButtons = document.querySelectorAll(".toggle-button");
    const sections = document.querySelectorAll(".section");

    toggleButtons.forEach(button => {
        button.addEventListener("click", () => {
            toggleButtons.forEach(btn => btn.classList.remove("active"));
            button.classList.add("active");

            const target = button.getAttribute("data-target");

            sections.forEach(section => {
                section.style.opacity = 0;
                section.style.transform = "scale(0.95)";
                setTimeout(() => {
                    section.style.display = "none";
                }, 300);
            });

            const targetSection = document.querySelector(`#${target}-section`);
            setTimeout(() => {
                targetSection.style.display = "block";
                setTimeout(() => {
                    targetSection.style.opacity = 1;
                    targetSection.style.transform = "scale(1)";
                }, 50);
            }, 300);
        });
    });

    toggleButtons[0].click();
});
