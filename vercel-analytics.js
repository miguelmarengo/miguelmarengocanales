/* Vercel Web Analytics loader (plain HTML). Requires Web Analytics enabled on the Vercel project. */
window.va =
  window.va ||
  function () {
    (window.vaq = window.vaq || []).push(arguments);
  };
(function () {
  var s = document.createElement("script");
  s.defer = true;
  s.src = "/_vercel/insights/script.js";
  document.head.appendChild(s);
})();
