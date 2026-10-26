/* AATTRL — main.js. Vanilla, no dependencies. The site works without it:
   this adds the mobile menu and light form checks before a Netlify form submits. */
(function () {
  'use strict';
  var doc = document;

  // Mobile menu
  var toggle = doc.querySelector('.menu-toggle');
  var panel = doc.getElementById('mobile-nav');
  if (toggle && panel) {
    toggle.addEventListener('click', function () {
      var open = panel.getAttribute('data-open') === 'true';
      panel.setAttribute('data-open', String(!open));
      toggle.setAttribute('aria-expanded', String(!open));
      toggle.textContent = open ? 'Menu' : 'Close';
    });
  }

  // Forms: mark required fields that are empty, and ignore very fast submissions.
  doc.querySelectorAll('form.form').forEach(function (form) {
    var started = Date.now();
    form.addEventListener('submit', function (e) {
      var bad = false;
      form.querySelectorAll('[required]').forEach(function (el) {
        var field = el.closest('.field');
        var ok = el.type === 'checkbox' ? el.checked : el.value.trim().length > 0;
        if (ok && el.type === 'email') ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim());
        if (field) field.setAttribute('data-invalid', ok ? 'false' : 'true');
        if (!ok && !bad) { bad = true; el.focus(); }
      });
      if (bad || Date.now() - started < 2500) { e.preventDefault(); }
    });
  });
})();
