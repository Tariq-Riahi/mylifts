document.addEventListener("DOMContentLoaded", function () {
  const searchBar = document.querySelector("input[type='search']");
  const toggleButton = document.querySelector(".navbar-toggler");

  searchBar.addEventListener("focus", function () {
    searchBar.parentElement.classList.add("active");
  });

  searchBar.addEventListener("blur", function () {
    searchBar.parentElement.classList.remove("active");
  });

  toggleButton.addEventListener("click", function () {
    if (searchBar === document.activeElement) {
      searchBar.blur();
    } else {
      searchBar.focus();
    }
  });
});
