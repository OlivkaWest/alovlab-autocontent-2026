/* =========================================================
   AlovLab · Автоконтент 2026 — интерактив лендинга
   ========================================================= */
(function () {
  "use strict";

  /* =======================================================
     НАСТРОЙКИ ВЛАДЕЛЬЦА ПРОЕКТА
     Заполните перед публикацией. Пока значения пустые —
     кнопки регистрации ведут к форме на странице, а форма
     честно сообщает, что endpoint не подключён.
     ======================================================= */
  var CONFIG = {
    // Внешняя ссылка на регистрацию (лендинг GetCourse / форма и т.п.).
    // Если заполнено — все кнопки «Записаться» ведут сюда (новая вкладка).
    // Если пусто — кнопки плавно скроллят к форме внизу страницы.
    REGISTRATION_URL: "", // [ВСТАВИТЬ ССЫЛКУ НА РЕГИСТРАЦИЮ]

    // Endpoint приёма данных формы: webhook (Make/n8n), Telegram-бот,
    // CRM или email-сервис. Ожидает POST с JSON { name, contact, telegram }.
    // Если пусто — форма не отправляет данные и покажет техническое сообщение.
    FORM_ENDPOINT: "", // [ВСТАВИТЬ WEBHOOK / ENDPOINT]

    // Ссылка на политику конфиденциальности (PDF или страница).
    PRIVACY_URL: "" // [ВСТАВИТЬ ССЫЛКУ НА ПОЛИТИКУ]
  };

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Аналитика: единая точка отправки событий ----------
     Подключите Яндекс.Метрику / VK Pixel и раскомментируйте нужные
     строки. Здесь события только собираются в один поток. */
  function track(event, params) {
    params = params || {};
    // Яндекс.Метрика:  window.ym && ym(XXXXXX, 'reachGoal', event, params);
    // VK Pixel:        window.VK && VK.Goal && VK.Goal(event, params);
    // Google Analytics:window.gtag && gtag('event', event, params);
    if (window.dataLayer) window.dataLayer.push(Object.assign({ event: event }, params));
    // Отладка (можно убрать): console.debug('[track]', event, params);
  }

  document.addEventListener("DOMContentLoaded", function () {
    var doc = document;

    /* ---------- Год в подвале ---------- */
    var yearEl = doc.getElementById("year");
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    /* ---------- Тост ---------- */
    var toastEl = doc.getElementById("toast");
    var toastTimer;
    function toast(html, ms) {
      if (!toastEl) return;
      toastEl.innerHTML = html;
      toastEl.classList.add("show");
      clearTimeout(toastTimer);
      toastTimer = setTimeout(function () { toastEl.classList.remove("show"); }, ms || 4200);
    }

    /* ---------- Шапка: непрозрачность при скролле ---------- */
    var header = doc.getElementById("siteHeader");
    var toTop = doc.getElementById("toTop");
    var mobileCta = doc.getElementById("mobileCta");
    var lastY = 0;

    function onScroll() {
      var y = window.pageYOffset;
      if (header) header.classList.toggle("scrolled", y > 12);
      if (toTop) toTop.classList.toggle("show", y > 600);
      // мобильная CTA появляется после первого экрана
      if (mobileCta) mobileCta.classList.toggle("show", y > window.innerHeight * 0.6);
      lastY = y;
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    /* ---------- Мобильное меню ---------- */
    var navToggle = doc.getElementById("navToggle");
    var nav = doc.getElementById("primaryNav");
    function closeMenu() {
      if (!nav) return;
      nav.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
      navToggle.setAttribute("aria-label", "Открыть меню");
    }
    if (navToggle && nav) {
      navToggle.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        navToggle.setAttribute("aria-expanded", String(open));
        navToggle.setAttribute("aria-label", open ? "Закрыть меню" : "Открыть меню");
      });
      nav.addEventListener("click", function (e) {
        if (e.target.tagName === "A") closeMenu();
      });
      doc.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });
    }

    /* ---------- Плавный скролл по якорям с учётом шапки ---------- */
    function scrollToHash(hash, focusEl) {
      var target = doc.querySelector(hash);
      if (!target) return;
      var headerH = header ? header.offsetHeight : 68;
      var top = target.getBoundingClientRect().top + window.pageYOffset - headerH - 12;
      window.scrollTo({ top: top, behavior: reduceMotion ? "auto" : "smooth" });
      if (focusEl) setTimeout(function () { focusEl.focus({ preventScroll: true }); }, reduceMotion ? 0 : 500);
    }

    /* ---------- Регистрация: кнопки ---------- */
    function goRegister(source) {
      track("register_click", { source: source });
      if (CONFIG.REGISTRATION_URL) {
        window.open(CONFIG.REGISTRATION_URL, "_blank", "noopener");
      } else {
        var firstField = doc.getElementById("regName");
        scrollToHash("#register", firstField);
      }
    }

    doc.querySelectorAll(".js-register").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        closeMenu();
        goRegister(btn.getAttribute("data-cta") || "unknown");
      });
    });

    /* ---------- Скачивание материалов ---------- */
    doc.querySelectorAll(".js-download").forEach(function (btn) {
      btn.addEventListener("click", function () {
        track("download_guide", { source: btn.getAttribute("data-cta"), file: btn.getAttribute("href") });
      });
    });

    /* ---------- Соцсети ---------- */
    doc.querySelectorAll(".js-social").forEach(function (btn) {
      btn.addEventListener("click", function () {
        track("social_click", { source: btn.getAttribute("data-cta"), url: btn.getAttribute("href") });
      });
    });

    /* ---------- Политика конфиденциальности ---------- */
    doc.querySelectorAll(".js-privacy").forEach(function (a) {
      a.addEventListener("click", function (e) {
        if (CONFIG.PRIVACY_URL) {
          a.setAttribute("href", CONFIG.PRIVACY_URL);
          a.setAttribute("target", "_blank");
          a.setAttribute("rel", "noopener");
          return; // переходим по реальной ссылке
        }
        e.preventDefault();
        toast("Ссылка на <strong>политику конфиденциальности</strong> добавляется владельцем проекта (CONFIG.PRIVACY_URL).");
      });
    });

    /* ---------- Внутренние якоря навигации ---------- */
    doc.querySelectorAll('a[href^="#"]:not(.js-register):not(.js-privacy)').forEach(function (a) {
      a.addEventListener("click", function (e) {
        var hash = a.getAttribute("href");
        if (hash.length < 2) return;
        var target = doc.querySelector(hash);
        if (!target) return;
        e.preventDefault();
        closeMenu();
        scrollToHash(hash);
        history.replaceState(null, "", hash);
      });
    });

    /* ---------- Пайплайн: раскрытие этапа ---------- */
    var stages = Array.prototype.slice.call(doc.querySelectorAll(".stage"));
    var dTitle = doc.getElementById("stageDetailTitle");
    var dDesc = doc.getElementById("stageDetailDesc");
    function selectStage(stage) {
      stages.forEach(function (s) { s.classList.remove("active"); });
      stage.classList.add("active");
      if (dTitle) dTitle.textContent = stage.getAttribute("data-title");
      if (dDesc) dDesc.textContent = stage.getAttribute("data-desc");
      track("pipeline_stage", { stage: stage.getAttribute("data-title") });
    }
    stages.forEach(function (stage, i) {
      stage.setAttribute("tabindex", "0");
      stage.setAttribute("role", "button");
      stage.addEventListener("click", function () { selectStage(stage); });
      stage.addEventListener("mouseenter", function () { if (!reduceMotion) selectStage(stage); });
      stage.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); selectStage(stage); }
        if (e.key === "ArrowRight" && stages[i + 1]) stages[i + 1].focus();
        if (e.key === "ArrowLeft" && stages[i - 1]) stages[i - 1].focus();
      });
    });
    if (stages[0]) stages[0].classList.add("active");

    /* ---------- Программа: раскрытие карточек дней ---------- */
    doc.querySelectorAll(".day-toggle").forEach(function (btn) {
      var body = btn.nextElementSibling;
      if (!body) return;
      btn.addEventListener("click", function () {
        var open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", String(!open));
        if (open) {
          body.hidden = true;
          btn.textContent = "Посмотреть программу";
        } else {
          body.hidden = false;
          btn.textContent = "Свернуть";
          track("program_open", { day: (btn.closest(".day-card").querySelector(".day-label") || {}).textContent });
        }
      });
    });

    /* ---------- Анимация цепочки в hero ---------- */
    var chainNodes = Array.prototype.slice.call(doc.querySelectorAll("#signalChain .chain-node"));
    if (chainNodes.length && !reduceMotion) {
      var idx = 0;
      setInterval(function () {
        chainNodes.forEach(function (n) { n.classList.remove("lit"); });
        chainNodes[idx].classList.add("lit");
        idx = (idx + 1) % chainNodes.length;
      }, 1100);
    } else if (chainNodes.length) {
      chainNodes[0].classList.add("lit");
    }

    /* ---------- Появление при скролле (IntersectionObserver) ---------- */
    var reveals = Array.prototype.slice.call(doc.querySelectorAll(".reveal"));
    if ("IntersectionObserver" in window && !reduceMotion) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add("in"); });
    }

    /* ---------- Активный пункт навигации ---------- */
    var navLinks = Array.prototype.slice.call(doc.querySelectorAll(".nav a"));
    var sectionMap = navLinks.map(function (a) {
      return { link: a, sec: doc.querySelector(a.getAttribute("href")) };
    }).filter(function (x) { return x.sec; });
    if ("IntersectionObserver" in window && sectionMap.length) {
      var sio = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            navLinks.forEach(function (l) { l.classList.remove("active"); });
            var m = sectionMap.find(function (x) { return x.sec === en.target; });
            if (m) m.link.classList.add("active");
          }
        });
      }, { threshold: 0.4, rootMargin: "-20% 0px -60% 0px" });
      sectionMap.forEach(function (x) { sio.observe(x.sec); });
    }

    /* ---------- Кнопка «Наверх» ---------- */
    if (toTop) {
      toTop.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
        track("to_top", {});
      });
    }

    /* ---------- Форма регистрации ---------- */
    var form = doc.getElementById("regForm");
    var statusEl = doc.getElementById("formStatus");
    function setStatus(msg, cls) {
      if (!statusEl) return;
      statusEl.textContent = "";
      statusEl.innerHTML = msg;
      statusEl.className = "form-status " + (cls || "");
    }
    function markInvalid(el, bad) { if (el) el.classList.toggle("invalid", !!bad); }

    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var name = doc.getElementById("regName");
        var contact = doc.getElementById("regContact");
        var tg = doc.getElementById("regTg");
        var consent = doc.getElementById("regConsent");

        var badName = !name.value.trim();
        var badContact = !contact.value.trim();
        markInvalid(name, badName);
        markInvalid(contact, badContact);
        markInvalid(consent, !consent.checked);

        if (badName || badContact) {
          setStatus("Заполните имя и контакт для связи.", "err");
          (badName ? name : contact).focus();
          return;
        }
        if (!consent.checked) {
          setStatus("Отметьте согласие на обработку данных.", "err");
          consent.focus();
          return;
        }

        var payload = {
          name: name.value.trim(),
          contact: contact.value.trim(),
          telegram: tg.value.trim(),
          source: "avtokontent-2026-landing"
        };
        track("form_submit", { has_telegram: !!payload.telegram });

        // Если задан внешний адрес регистрации — уводим туда.
        if (CONFIG.REGISTRATION_URL) {
          setStatus("Переходим к регистрации…", "info");
          window.open(CONFIG.REGISTRATION_URL, "_blank", "noopener");
          return;
        }

        // Если endpoint не подключён — честно сообщаем.
        if (!CONFIG.FORM_ENDPOINT) {
          setStatus(
            "Форма собрана, но приём заявок ещё не подключён. " +
            "Владельцу проекта: укажите <strong>CONFIG.FORM_ENDPOINT</strong> " +
            "(webhook / Telegram-бот / CRM) или <strong>CONFIG.REGISTRATION_URL</strong> в js/main.js.",
            "info"
          );
          return;
        }

        // Реальная отправка на webhook / CRM.
        setStatus("Отправляем…", "info");
        var btn = form.querySelector('button[type="submit"]');
        if (btn) btn.disabled = true;
        fetch(CONFIG.FORM_ENDPOINT, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        }).then(function (r) {
          if (!r.ok) throw new Error("HTTP " + r.status);
          form.reset();
          setStatus("Готово! Мы получили заявку и пришлём материалы на указанный контакт.", "ok");
          track("form_success", {});
        }).catch(function () {
          setStatus("Не удалось отправить. Попробуйте ещё раз или напишите нам в Telegram: t.me/AlovLab.", "err");
          track("form_error", {});
        }).finally(function () {
          if (btn) btn.disabled = false;
        });
      });
    }

    // экспонируем конфиг для быстрой проверки в консоли
    window.ALOVLAB = { config: CONFIG, track: track };
  });
})();
