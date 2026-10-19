/* AATTRL Global Expert Advisory - main.js
   Vanilla JavaScript, no dependencies. Core content never depends on this file:
   it adds the mobile menu, service finder, insight filters, form validation and
   (optionally) analytics. */
(function () {
  'use strict';

  /* 1. Configuration --------------------------------------------------------
     Analytics stay OFF until you add your IDs. Before switching them on, put a
     consent approach in place that suits where your visitors are (for example
     GDPR / UK GDPR for Europe, the DPDP Act for India). See README.md. */
  var SITE_CONFIG = {
    ga4MeasurementId: '',   // Google Analytics 4, e.g. 'G-XXXXXXXXXX'
    clarityProjectId: '',   // Microsoft Clarity project ID
    throttleSeconds: 60,    // minimum gap between two submissions from one browser
    minFillSeconds: 3       // forms sent faster than this are treated as automated
  };

  var doc = document;
  var script = doc.currentScript || doc.querySelector('script[src*="assets/js/main.js"]');
  var ROOT = script ? script.src.replace(/assets\/js\/main\.js.*$/, '') : '/';
  var IS_FILE = location.protocol === 'file:';

  // Site-root path ("services/hazop/") -> absolute URL that also works from file://
  function resolve(path) {
    var u = ROOT + path;
    return IS_FILE ? u.replace(/\/(#|\?|$)/, '/index.html$1') : u;
  }

  /* 2. Local preview: folder links -> index.html when opened from disk ------ */
  if (IS_FILE) {
    doc.querySelectorAll('a[href]').forEach(function (a) {
      var h = a.getAttribute('href');
      if (/^([a-z]+:|#|\/\/)/i.test(h)) return;
      var i = h.search(/[?#]/), p = i < 0 ? h : h.slice(0, i), rest = i < 0 ? '' : h.slice(i);
      if (p && /\/$/.test(p)) a.setAttribute('href', p + 'index.html' + rest);
    });
  }

  /* 3. Analytics (only when IDs are set) ------------------------------------ */
  function loadScript(src) { var s = doc.createElement('script'); s.async = true; s.src = src; doc.head.appendChild(s); }
  if (SITE_CONFIG.ga4MeasurementId) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', SITE_CONFIG.ga4MeasurementId);
    loadScript('https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(SITE_CONFIG.ga4MeasurementId));
  }
  if (SITE_CONFIG.clarityProjectId) {
    window.clarity = window.clarity || function () { (window.clarity.q = window.clarity.q || []).push(arguments); };
    loadScript('https://www.clarity.ms/tag/' + encodeURIComponent(SITE_CONFIG.clarityProjectId));
  }
  function track(name, params) { if (typeof window.gtag === 'function') window.gtag('event', name, params || {}); }
  doc.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('[data-track]') : null;
    if (a) track('contact_click', { method: a.getAttribute('data-track'), link_url: a.href });
  });

  /* 4. Navigation ------------------------------------------------------------ */
  var header = doc.querySelector('.site-header');
  var toggle = doc.querySelector('.nav-toggle');
  var desktop = window.matchMedia('(min-width: 68em)');
  function setNav(open) {
    if (!header || !toggle) return;
    header.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.querySelector('span').textContent = open ? 'Close' : 'Menu';
    doc.body.classList.toggle('nav-locked', open && !desktop.matches);
  }
  function closeSubs(except) {
    doc.querySelectorAll('.has-sub.sub-open').forEach(function (li) {
      if (li === except) return;
      li.classList.remove('sub-open');
      li.querySelector('.sub-toggle').setAttribute('aria-expanded', 'false');
    });
  }
  if (toggle) toggle.addEventListener('click', function () { setNav(!header.classList.contains('nav-open')); });
  doc.querySelectorAll('.sub-toggle').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var li = btn.closest('.has-sub'), open = !li.classList.contains('sub-open');
      closeSubs(li);
      li.classList.toggle('sub-open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
  });
  doc.addEventListener('click', function (e) { if (desktop.matches && !e.target.closest('.has-sub')) closeSubs(); });
  doc.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    var open = doc.querySelector('.has-sub.sub-open');
    if (open) { closeSubs(); open.querySelector('.sub-toggle').focus(); return; }
    if (header && header.classList.contains('nav-open')) { setNav(false); toggle.focus(); }
  });
  var onBreakpoint = function () { setNav(false); closeSubs(); };
  if (desktop.addEventListener) desktop.addEventListener('change', onBreakpoint); else if (desktop.addListener) desktop.addListener(onBreakpoint);

  /* 5. Service finder (homepage and 404) ------------------------------------ */
  var finder = doc.querySelector('[data-finder]');
  var finderData = doc.getElementById('finder-data');
  if (finder && finderData) {
    var items = [];
    try { items = JSON.parse(finderData.textContent); } catch (err) { items = []; }
    var input = finder.querySelector('input[type="search"]');
    var list = doc.getElementById('finder-list');
    var empty = finder.querySelector('.finder-empty');
    var results = [], active = -1;
    var norm = function (s) { return (s || '').toLowerCase().replace(/&/g, ' and ').replace(/[^a-z0-9]+/g, ' ').trim(); };
    items.forEach(function (it) { it._n = norm(it.n); it._k = ' ' + norm(it.k + ' ' + it.g); });
    var score = function (it, q, terms) {
      var s = it._n === q ? 100 : it._n.indexOf(q) === 0 ? 60 : it._n.indexOf(q) > -1 ? 40 : 0;
      for (var i = 0; i < terms.length; i++) {
        var t = terms[i];
        if ((' ' + it._n).indexOf(' ' + t) > -1) s += 14;
        else if (it._n.indexOf(t) > -1) s += 8;
        else if (it._k.indexOf(' ' + t) > -1) s += 6;
        else return 0;
      }
      return s + (it.p ? 5 : 0);
    };
    var hideList = function () { list.hidden = true; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant'); active = -1; };
    var render = function (q) {
      var nq = norm(q);
      list.innerHTML = '';
      empty.hidden = true;
      if (!nq) { results = []; hideList(); return; }
      var terms = nq.split(' ');
      results = items.map(function (it) { return { it: it, s: score(it, nq, terms) }; })
        .filter(function (r) { return r.s > 0; })
        .sort(function (a, b) { return b.s - a.s || a.it.n.length - b.it.n.length; })
        .slice(0, 8).map(function (r) { return r.it; });
      results.forEach(function (it, i) {
        var li = doc.createElement('li'), a = doc.createElement('a'), n = doc.createElement('span'), g = doc.createElement('span');
        li.className = 'finder-opt'; li.id = 'finder-opt-' + i; li.setAttribute('role', 'option'); li.setAttribute('aria-selected', 'false');
        a.href = resolve(it.u); a.tabIndex = -1;
        n.className = 'fo-n'; n.textContent = it.n; g.className = 'fo-g'; g.textContent = it.g;
        a.appendChild(n); a.appendChild(g); li.appendChild(a); list.appendChild(li);
      });
      active = -1;
      if (results.length) { list.hidden = false; input.setAttribute('aria-expanded', 'true'); }
      else {
        hideList();
        empty.textContent = 'No page matches \u201C' + q.trim() + '\u201D yet. ';
        var link = doc.createElement('a');
        link.href = resolve('request-expert/') + '?q=' + encodeURIComponent(q.trim());
        link.textContent = 'Describe the expertise you need';
        empty.appendChild(link);
        empty.appendChild(doc.createTextNode(' and we will find the right specialist.'));
        empty.hidden = false;
      }
    };
    var setActive = function (i) {
      var opts = list.querySelectorAll('.finder-opt');
      if (!opts.length) return;
      active = (i + opts.length) % opts.length;
      opts.forEach(function (o, k) { o.classList.toggle('is-active', k === active); o.setAttribute('aria-selected', String(k === active)); });
      input.setAttribute('aria-activedescendant', opts[active].id);
      opts[active].scrollIntoView({ block: 'nearest' });
    };
    input.addEventListener('input', function () { render(input.value); });
    input.addEventListener('focus', function () { if (input.value) render(input.value); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); if (list.hidden) render(input.value); setActive(active + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(active - 1); }
      else if (e.key === 'Escape' && !list.hidden) { e.stopPropagation(); hideList(); }
    });
    finder.addEventListener('submit', function (e) {
      var q = input.value.trim();
      e.preventDefault();
      if (!q) { input.focus(); return; }
      if (!results.length) render(q);
      var target = results[active > -1 ? active : 0];
      location.href = target ? resolve(target.u) : resolve('request-expert/') + '?q=' + encodeURIComponent(q);
    });
    doc.addEventListener('click', function (e) { if (!finder.contains(e.target)) hideList(); });
  }

  /* 6. Insights category filter --------------------------------------------- */
  var bar = doc.querySelector('[data-filter-bar]');
  if (bar) {
    var lists = doc.querySelectorAll('[data-filter-list]');
    var emptyMsg = doc.querySelector('.filter-empty');
    var apply = function (cat) {
      var shown = 0;
      bar.querySelectorAll('.filter-btn').forEach(function (b) {
        var on = b.getAttribute('data-filter') === cat;
        b.classList.toggle('is-on', on); b.setAttribute('aria-pressed', String(on));
      });
      lists.forEach(function (ul, idx) {
        ul.querySelectorAll('[data-cat]').forEach(function (li) {
          var ok = cat === 'all' || li.getAttribute('data-cat') === cat;
          li.hidden = !ok;
          if (ok && idx === 0) shown++;
        });
      });
      if (emptyMsg) emptyMsg.hidden = shown > 0;
    };
    bar.addEventListener('click', function (e) {
      var b = e.target.closest('.filter-btn');
      if (!b) return;
      var cat = b.getAttribute('data-filter');
      apply(cat);
      if (history.replaceState) history.replaceState(null, '', cat === 'all' ? location.pathname : '#cat-' + cat);
    });
    var m = location.hash.match(/^#cat-([a-z0-9-]+)$/);
    if (m && bar.querySelector('[data-filter="' + m[1] + '"]')) apply(m[1]);
  }

  /* 7. Forms: validation, anti-spam, delivery -------------------------------
     Delivery: set data-endpoint on the <form> (Formspree, Basin, your own API
     or a serverless function that forwards to HubSpot / Zoho / Salesforce).
     With no endpoint the visitor's email app opens with the request filled in.
     EmailJS alternative: load their SDK and call emailjs.sendForm(...) where
     marked below. Never put secret API keys in this file. */
  var THROTTLE_KEY = 'aattrl_last_submit';
  var store = function (k, v) {
    try { if (v === undefined) return window.localStorage.getItem(k); window.localStorage.setItem(k, v); } catch (err) { return null; }
    return null;
  };

  doc.querySelectorAll('form[data-form]').forEach(function (form) {
    var started = Date.now();
    var status = form.querySelector('.form-status');
    var email = form.getAttribute('data-email');
    var pageField = form.querySelector('[name="page_url"]');
    if (pageField) pageField.value = location.href;

    // Prefill from links such as /request-expert/#service=hazop or ?q=reliability
    var params = new URLSearchParams(location.search);
    var hm = location.hash.match(/service=([a-z0-9-]+)/);
    var slug = (hm && hm[1]) || params.get('service');
    if (slug) {
      var opt = form.querySelector('select[name="service"] option[data-slug="' + slug.replace(/[^a-z0-9-]/g, '') + '"]');
      if (opt) opt.selected = true;
    }
    var q = params.get('q'), rx = form.querySelector('[name="required_expertise"]');
    if (q && rx && !rx.value) rx.value = q.slice(0, 200);

    var setStatus = function (msg, type) {
      if (!status) return;
      status.textContent = msg;
      status.classList.toggle('is-error', type === 'error');
      status.classList.toggle('is-ok', type === 'ok');
    };
    var describe = function (el, id, add) {
      var d = (el.getAttribute('aria-describedby') || '').split(' ').filter(function (x) { return x && x !== id; });
      if (add) d.push(id);
      if (d.length) el.setAttribute('aria-describedby', d.join(' ')); else el.removeAttribute('aria-describedby');
    };
    var setError = function (wrap, targets, key, msg) {
      if (!wrap) return;
      var id = form.id + '-' + key + '-err', p = wrap.querySelector('.field-error');
      if (msg) {
        if (!p) { p = doc.createElement('p'); p.className = 'field-error'; p.id = id; wrap.appendChild(p); }
        p.textContent = msg;
        targets.forEach(function (t) { t.setAttribute('aria-invalid', 'true'); describe(t, id, true); });
      } else {
        if (p) p.parentNode.removeChild(p);
        targets.forEach(function (t) { t.removeAttribute('aria-invalid'); describe(t, id, false); });
      }
    };
    var validate = function (el) {
      if (el.disabled || el.type === 'hidden' || el.name === '_gotcha' || !el.name) return true;
      var msg = '', wrap = el.closest('.field');
      if (el.type === 'radio') {
        var group = Array.prototype.slice.call(form.querySelectorAll('input[name="' + el.name + '"]'));
        var needed = group.some(function (r) { return r.required; });
        if (needed && !group.some(function (r) { return r.checked; })) msg = group[0].getAttribute('data-err') || 'Select an option.';
        setError(wrap, group, el.name, msg);
        return !msg;
      }
      if (el.type === 'checkbox') {
        if (el.required && !el.checked) msg = el.getAttribute('data-err') || 'Tick this box to continue.';
      } else if (el.type === 'file') {
        var f = el.files && el.files[0], max = +(el.getAttribute('data-max-mb') || 10);
        if (f && f.size > max * 1048576) msg = 'The file is larger than ' + max + ' MB. Attach a smaller file, or send it by email after submitting.';
      } else {
        var v = (el.value || '').trim();
        if (el.required && !v) msg = el.getAttribute('data-err') || 'Complete this field.';
        else if (v && el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) msg = el.getAttribute('data-err') || 'Enter a valid email address.';
        else if (v && el.type === 'url' && !/^https?:\/\/\S+\.\S+/.test(v)) msg = el.getAttribute('data-err') || 'Enter the full link, starting with https://.';
        else if (v && el.type === 'tel' && !/^[+()\d\s.\-]{6,}$/.test(v)) msg = 'Enter the phone number using digits, spaces and an optional +.';
      }
      setError(wrap, [el], el.name, msg);
      return !msg;
    };
    var revalidate = function (e) { var t = e.target; if (t.getAttribute('aria-invalid') === 'true' || (t.type === 'radio' && t.closest('.field').querySelector('.field-error'))) validate(t); };
    form.addEventListener('input', revalidate);
    form.addEventListener('change', revalidate);

    var labelFor = function (el) {
      if (el.type === 'checkbox') return el.name.replace(/_/g, ' ');
      var wrap = el.closest('.field'), l = wrap && (wrap.querySelector('legend') || wrap.querySelector('label'));
      return l ? l.textContent.replace(/\*/g, '').trim() : el.name;
    };
    var mailtoFallback = function () {
      var lines = [], hasFile = false;
      form.querySelectorAll('input, select, textarea').forEach(function (el) {
        if (!el.name || el.type === 'hidden' || el.name === '_gotcha') return;
        if ((el.type === 'radio' || el.type === 'checkbox') && !el.checked) return;
        if (el.type === 'file') { if (el.files && el.files.length) hasFile = true; return; }
        var v = (el.value || '').trim();
        if (v) lines.push(labelFor(el) + ': ' + v);
      });
      if (hasFile) lines.push('', '[Please attach your file to this email before sending.]');
      lines.push('', 'Sent from: ' + location.href);
      var body = lines.join('\n');
      if (body.length > 1500) body = body.slice(0, 1500) + '\n[Text shortened: please complete it here.]';
      var who = form.querySelector('[name="company"], [name="organization"], [name="name"]');
      var subject = form.getAttribute('data-subject') + (who && who.value ? ' - ' + who.value.trim() : '');
      store(THROTTLE_KEY, String(Date.now()));
      location.href = 'mailto:' + email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      setStatus('Your email app should now open with the request filled in. Press send to complete it' +
        (hasFile ? ', after attaching your file' : '') + '. If nothing opens, email ' + email + ' directly.', 'ok');
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      setStatus('');
      var firstBad = null;
      form.querySelectorAll('input, select, textarea').forEach(function (el) { if (!validate(el) && !firstBad) firstBad = el; });
      if (firstBad) { setStatus('Check the highlighted fields, then send again.', 'error'); firstBad.focus(); return; }
      var trap = form.querySelector('[name="_gotcha"]');
      if (trap && trap.value) { form.reset(); setStatus('Thank you. Your request has been received.', 'ok'); return; }
      if ((Date.now() - started) / 1000 < SITE_CONFIG.minFillSeconds) {
        started = 0;
        setStatus('Please check your details, then press the button again to send.', 'error');
        return;
      }
      var last = +(store(THROTTLE_KEY) || 0);
      if (Date.now() - last < SITE_CONFIG.throttleSeconds * 1000) {
        setStatus('A request was sent from this browser less than a minute ago. Wait a moment before sending another, or email ' + email + '.', 'error');
        return;
      }
      var endpoint = form.getAttribute('data-endpoint');
      if (!endpoint) { mailtoFallback(); return; }
      // EmailJS alternative: replace the fetch below with emailjs.sendForm('SERVICE_ID', 'TEMPLATE_ID', form)
      var btn = form.querySelector('[type="submit"]');
      btn.disabled = true; form.setAttribute('aria-busy', 'true');
      setStatus('Sending\u2026');
      fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error('HTTP ' + r.status);
          store(THROTTLE_KEY, String(Date.now()));
          track('generate_lead', { form_name: form.getAttribute('data-form') });
          location.href = resolve(form.getAttribute('data-success') || 'thank-you/');
        })
        .catch(function () {
          btn.disabled = false; form.removeAttribute('aria-busy');
          setStatus('The request could not be sent. Check your connection and try again, or email ' + email + ' directly.', 'error');
        });
    });
  });
})();
