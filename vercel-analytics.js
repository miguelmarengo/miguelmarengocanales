/* Vercel Web Analytics loader (plain HTML). 
 * Official implementation using CDN as per Vercel docs.
 * See: https://vercel.com/docs/analytics/package
 */
window.va = window.va || function () {
  (window.vaq = window.vaq || []).push(arguments);
};

(function () {
  var script = document.createElement('script');
  script.defer = true;
  script.src = 'https://cdn.vercel-insights.com/v1/script.js';
  document.head.appendChild(script);
})();
