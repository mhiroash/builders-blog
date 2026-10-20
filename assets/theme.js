(function () {
  var root = document.documentElement;
  var saved = null;
  try { saved = localStorage.getItem("blog-theme"); } catch (e) {}
  if (saved) root.setAttribute("data-theme", saved);
  var btn = document.querySelector(".blog-theme-toggle");
  if (btn) btn.addEventListener("click", function () {
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("blog-theme", next); } catch (e) {}
  });
})();
