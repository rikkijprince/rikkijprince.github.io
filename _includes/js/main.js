document.addEventListener("DOMContentLoaded", function() {

  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  const body = document.body;

  function closeMenu() {
    links.classList.remove("show");
    toggle.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
    body.classList.remove("menu-open");
  }

  function openMenu() {
    links.classList.add("show");
    toggle.classList.add("open");
    toggle.setAttribute("aria-expanded", "true");
    body.classList.add("menu-open");
  }

  toggle.addEventListener("click", () => {
    const isOpen = links.classList.contains("show");
    isOpen ? closeMenu() : openMenu();
  });

  links.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("click", (e) => {
    if (!toggle.contains(e.target) && !links.contains(e.target)) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeMenu();
    }
  });

});
