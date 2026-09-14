document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("navToggle") || document.querySelector(".nav-toggle");
  const links = document.getElementById("navMenu") || document.querySelector(".nav-links");
  const body = document.body;

  if (!toggle || !links) return;

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

  toggle.addEventListener("click", function () {
    const isOpen = links.classList.contains("show");
    isOpen ? closeMenu() : openMenu();
  });

  links.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("click", function (event) {
    if (!toggle.contains(event.target) && !links.contains(event.target)) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeMenu();
    }
  });
});
