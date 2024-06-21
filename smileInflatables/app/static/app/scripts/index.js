const navLinks = document.querySelector(".nav-links");
const menuButton = document.querySelector(".menu-button");
menuButton.addEventListener("click", (event) => {
  navLinks.classList.toggle("translate-x-[0vw]");
  menuButton.classList.toggle("activate-close");
});
