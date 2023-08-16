document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("user-search");
  const userCards = document.querySelectorAll(".user-card");
  const originalDisplayStyles = Array.from(userCards).map(card => card.style.display);

  searchInput.addEventListener("input", function () {
    const searchText = searchInput.value.toLowerCase();
    userCards.forEach((userCard, index) => {
      const userName = userCard.querySelector(".user-info h3").textContent.toLowerCase();
      if (userName.includes(searchText)) {
        userCard.style.display = originalDisplayStyles[index]; // Restore original display style
      } else {
        userCard.style.display = "none";
      }
    });
  });
});