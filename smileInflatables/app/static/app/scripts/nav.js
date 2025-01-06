navLinks = document.querySelector(".nav-links");
menuButton = document.querySelector(".menu-button");
menuButton.addEventListener("click", (event) => {
  navLinks.classList.toggle("translate-x-[-100vw]");
  menuButton.classList.toggle("activate-close");
});

productsButton = document.querySelector("#products-button");
productsButton.addEventListener("click", (event) => {
  navLinks.classList.toggle("translate-x-[-100vw]");
  menuButton.classList.toggle("activate-close");
});
