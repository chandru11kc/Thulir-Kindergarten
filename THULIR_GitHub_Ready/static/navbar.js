document.addEventListener('DOMContentLoaded', function () {
    var navbar = document.querySelector('.main-navbar');
    var hamburger = document.querySelector('.hamburger');
    var navLinks = document.querySelector('.nav-links');
    var overlay = document.querySelector('.nav-overlay');

    /* ---------- Scrolled state ---------- */
    function updateScrolled() {
        if (!navbar) return;
        if (window.scrollY > 10) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }

    updateScrolled();
    window.addEventListener('scroll', updateScrolled, { passive: true });

    /* ---------- Mobile menu toggle ---------- */
    function openMenu() {
        hamburger.classList.add('open');
        navLinks.classList.add('open');
        if (overlay) overlay.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
        hamburger.classList.remove('open');
        navLinks.classList.remove('open');
        if (overlay) overlay.classList.remove('open');
        document.body.style.overflow = '';
    }

    function toggleMenu() {
        if (navLinks.classList.contains('open')) {
            closeMenu();
        } else {
            openMenu();
        }
    }

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', toggleMenu);
    }

    if (overlay) {
        overlay.addEventListener('click', closeMenu);
    }

    /* Close the menu when a nav link is tapped */
    if (navLinks) {
        navLinks.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', closeMenu);
        });
    }

    /* Reset menu state if the viewport grows back to desktop width */
    window.addEventListener('resize', function () {
        if (window.innerWidth > 900) {
            closeMenu();
        }
    });

    /* Close on Escape key */
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeMenu();
    });
});

/* ============================================
   Scroll-Reveal
   Adds `.visible` to any `.section.reveal`,
   `.cta.reveal`, or card inside `.cards` once
   it enters the viewport. Without this script,
   those elements stay permanently invisible
   (opacity: 0 is their default state in CSS).
   ============================================ */
document.addEventListener('DOMContentLoaded', function () {
    var revealTargets = document.querySelectorAll('.section.reveal, .cta.reveal, .cards .card');

    if (!revealTargets.length) return;

    if (!('IntersectionObserver' in window)) {
        // Fallback for very old browsers — just show everything immediately.
        revealTargets.forEach(function (el) { el.classList.add('visible'); });
        return;
    }

    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

    revealTargets.forEach(function (el) { observer.observe(el); });
});