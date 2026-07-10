/* Rives Intérieures — interactions */
(function () {
  "use strict";

  /* Marqueur JS actif (les animations .rvl ne masquent rien sans lui) */
  document.documentElement.classList.add("js");
  if (window.location.search.indexOf("noanim") !== -1) {
    document.documentElement.classList.add("no-anim");
  }

  /* Header : état scrollé */
  var header = document.querySelector(".header");
  var onScroll = function () {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 10);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Navigation mobile */
  var burger = document.querySelector(".burger");
  if (burger) {
    burger.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".nav a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("nav-open");
        burger.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* Révélation au scroll */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("est-visible");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    document.querySelectorAll(".rvl").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".rvl").forEach(function (el) { el.classList.add("est-visible"); });
  }

  /* Curseurs avant / après */
  document.querySelectorAll(".ba").forEach(function (ba) {
    var range = ba.querySelector(".ba__range");
    if (!range) return;
    var setPos = function (v) { ba.style.setProperty("--pos", v + "%"); };
    range.addEventListener("input", function () { setPos(range.value); });
    setPos(range.value || 50);
  });
})();
