
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#173d2a">
<meta name="description" content="Explore a beautiful natural garden filled with flowers, trees, butterflies, ponds, and peaceful green landscapes.">
<title>Nature's Garden | Explore the Beauty of Nature</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
:root {
  --green: #285c3d;
  --green-dark: #173d2a;
  --green-light: #dcebd8;
  --cream: #f7f7ed;
  --yellow: #e6c86a;
  --text: #23372a;
  --muted: #6c7a6c;
  --card: #ffffff;
  --shadow: 0 15px 45px rgba(24, 57, 35, .10);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; scroll-padding-top: 85px; }

body {
  font-family: 'DM Sans', sans-serif;
  background: var(--cream);
  color: var(--text);
  line-height: 1.7;
  overflow-x: hidden;
  transition: background .35s, color .35s;
}

body.night {
  --cream: #101c16;
  --text: #e4eee5;
  --muted: #b0c0b3;
  --card: #1b2b21;
  --green-light: #263d2d;
  --shadow: 0 15px 45px rgba(0,0,0,.22);
}

img { display: block; width: 100%; object-fit: cover; }
a { color: inherit; text-decoration: none; }
button { font: inherit; cursor: pointer; }
button:focus-visible, a:focus-visible { outline: 3px solid var(--yellow); outline-offset: 4px; }

.container { width: min(1160px, 90%); margin: auto; }
.section { padding: 95px 0; }
.section-heading { text-align: center; max-width: 700px; margin: 0 auto 45px; }
.eyebrow { color: var(--green); font-weight: 700; text-transform: uppercase; letter-spacing: 3px; font-size: .76rem; }
.night .eyebrow { color: #a9d5a8; }

h1, h2, h3 { font-family: 'Playfair Display', Georgia, serif; line-height: 1.2; }
h2 { font-size: clamp(2rem, 4vw, 3.1rem); margin: 12px 0 16px; }
.section-heading p { color: var(--muted); }

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border: 1px solid transparent;
  padding: 13px 23px;
  border-radius: 50px;
  background: var(--green);
  color: white;
  font-weight: 600;
  transition: transform .25s, background .25s;
}
.btn:hover { transform: translateY(-3px); background: #1b472e; }
.btn-outline { background: transparent; border-color: white; color: white; }
.btn-outline:hover { background: white; color: var(--green-dark); }
.btn-small { padding: 9px 17px; font-size: .9rem; }

/* Navigation */
.navbar {
  position: fixed;
  z-index: 100;
  top: 12px;
  left: 50%;
  transform: translateX(-50%);
  width: min(1220px, 96%);
  min-height: 68px;
  padding: 12px 22px;
  border: 1px solid rgba(255,255,255,.35);
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
  background: rgba(247,247,237,.91);
  backdrop-filter: blur(16px);
  box-shadow: 0 6px 25px rgba(0,0,0,.08);
}
.logo { font-family: 'Playfair Display', serif; font-size: 1.35rem; font-weight: 700; color: var(--green-dark); white-space: nowrap; }
.logo span { color: #8aab68; }
.nav-links { display: flex; align-items: center; gap: 23px; list-style: none; }
.nav-links a { font-size: .88rem; font-weight: 600; color: #294331; }
.nav-links a:hover { color: #7c9c53; }
.nav-actions { display: flex; gap: 8px; align-items: center; }
.icon-btn {
  width: 40px; height: 40px; border: 0; border-radius: 50%;
  background: var(--green-light); color: var(--green-dark);
  display: grid; place-items: center; font-size: 1.1rem;
}
.menu-btn { display: none; }

/* Hero */
.hero {
  min-height: 100svh;
  position: relative;
  display: flex;
  align-items: center;
  color: white;
  background:
    linear-gradient(90deg, rgba(9,32,18,.76), rgba(13,38,21,.39) 55%, rgba(13,38,21,.10)),
    linear-gradient(0deg, rgba(9,32,18,.28), transparent 60%),
    url('https://images.unsplash.com/photo-1416879595882-3373a0480b5b?auto=format&fit=crop&w=2200&q=85') center 55% / cover;
  overflow: hidden;
}
.hero::before {
  content: "";
  position: absolute;
  width: 500px; height: 500px;
  border-radius: 50%;
  right: -120px; top: -180px;
  background: rgba(255,231,160,.16);
  filter: blur(70px);
  pointer-events: none;
}
.hero-content { position: relative; z-index: 2; padding-top: 80px; max-width: 760px; }
.hero .eyebrow { color: #f2d987; }
.hero h1 { font-size: clamp(3rem, 8vw, 6.4rem); margin: 23px 0; letter-spacing: -2px; }
.hero h1 span { color: #e7d68e; }
.hero p { max-width: 570px; font-size: clamp(1rem, 2vw, 1.2rem); color: #f0f4ed; margin-bottom: 30px; }
.hero-buttons { display: flex; flex-wrap: wrap; gap: 13px; }
.hero .btn { background: #d8c56f; color: #203a27; }
.hero .btn:hover { background: #f1df8b; }
.hero .btn-outline { background: rgba(255,255,255,.10); border-color: rgba(255,255,255,.8); color: white; }
.hero .btn-outline:hover { background: white; color: var(--green-dark); }

.hero-note {
  position: absolute; bottom: 35px; right: 5%;
  padding: 13px 19px; border-radius: 15px;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.3);
  backdrop-filter: blur(12px);
  font-size: .85rem;
}
.scroll-indicator { margin-top: 55px; font-size: .8rem; letter-spacing: 2px; }

/* Gentle leaves */
.leaf {
  position: absolute; z-index: 1; top: -40px;
  color: #dce8a0; opacity: .65; pointer-events: none;
  animation: fall 12s linear infinite;
}
.leaf:nth-child(2) { left: 20%; animation-delay: 2s; }
.leaf:nth-child(3) { left: 60%; animation-delay: 5s; }
.leaf:nth-child(4) { left: 82%; animation-delay: 8s; }
@keyframes fall {
  0% { transform: translateY(-40px) rotate(0deg); }
  50% { transform: translate(50px, 50vh) rotate(170deg); }
  100% { transform: translate(-30px, 110vh) rotate(350deg); }
}

/* Intro strip */
.intro-strip { background: var(--green-dark); color: white; padding: 24px 0; }
.strip-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; text-align: center; }
.strip-grid strong { display: block; color: #e6d486; font-family: 'Playfair Display', serif; font-size: 1.6rem; }
.strip-grid span { font-size: .84rem; color: #d4e0d4; }

/* Cards */
.card-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.card {
  background: var(--card); border-radius: 20px; overflow: hidden;
  box-shadow: var(--shadow); transition: transform .3s, box-shadow .3s;
}
.card:hover { transform: translateY(-7px); box-shadow: 0 20px 45px rgba(25,65,37,.16); }
.card img { height: 235px; transition: transform .6s; }
.card:hover img { transform: scale(1.045); }
.card-image { overflow: hidden; position: relative; }
.card-body { padding: 23px; }
.card h3 { font-size: 1.45rem; margin-bottom: 8px; }
.card p { color: var(--muted); font-size: .94rem; }
.card .btn { margin-top: 17px; }
.tag { display: inline-block; background: var(--green-light); color: var(--green); padding: 5px 10px; border-radius: 30px; font-size: .74rem; font-weight: 700; margin-bottom: 12px; }
.scientific { color: var(--muted); font-size: .85rem; font-style: italic; margin: -2px 0 12px; }
.care { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 15px; }
.care span { background: var(--green-light); padding: 5px 9px; border-radius: 8px; font-size: .77rem; }

/* Garden experience */
.explore-section { background: var(--green-light); }
.night .explore-section { background: #17271d; }

/* Flower cards */
.flower-card img { height: 210px; }
.flower-card .card-body { padding: 20px; }

/* Facts */
.fact-panel {
  background: var(--green-dark); color: white;
  border-radius: 24px; padding: 45px;
  display: grid; grid-template-columns: 1.1fr 1fr; gap: 30px; align-items: center;
}
.fact-panel h2 { color: white; }
.fact-panel p { color: #d9e4d8; }
.fact-box {
  background: rgba(255,255,255,.09); border: 1px solid rgba(255,255,255,.17);
  padding: 25px; border-radius: 18px; min-height: 155px;
}
.fact-box p { font-size: 1.1rem; }

/* Gallery */
.filters { display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin-bottom: 28px; }
.filter-btn { padding: 9px 18px; border: 1px solid #a7b7a4; background: transparent; color: var(--text); border-radius: 30px; }
.filter-btn.active, .filter-btn:hover { background: var(--green); color: white; border-color: var(--green); }
.gallery-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }
.gallery-item {
  border: 0; padding: 0; border-radius: 16px; overflow: hidden;
  position: relative; background: #ddd; min-height: 230px;
}
.gallery-item img { height: 100%; min-height: 230px; position: absolute; inset: 0; transition: transform .45s; }
.gallery-item:hover img { transform: scale(1.07); }
.gallery-item span {
  position: absolute; left: 12px; bottom: 12px; z-index: 2;
  background: rgba(13,36,22,.75); color: white;
  padding: 6px 12px; border-radius: 30px; font-size: .8rem;
}
.gallery-item[hidden] { display: none; }

/* About */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; align-items: center; gap: 55px; }
.about-image { position: relative; }
.about-image img { height: 490px; border-radius: 24px; box-shadow: var(--shadow); }
.about-image::after { content: ""; position: absolute; inset: 18px -18px -18px 18px; border: 2px solid #a3b98c; border-radius: 24px; z-index: -1; }
.about-copy p { color: var(--muted); margin: 18px 0; }
.benefit-list { display: grid; grid-template-columns: 1fr 1fr; gap: 13px; margin-top: 25px; }
.benefit { padding: 13px; background: var(--card); border-radius: 12px; box-shadow: var(--shadow); font-size: .9rem; }

/* Quiz */
.quiz-card { max-width: 700px; margin: auto; background: var(--card); padding: 35px; border-radius: 22px; box-shadow: var(--shadow); }
.quiz-card h3 { font-size: 1.5rem; margin-bottom: 20px; }
.quiz-options { display: grid; gap: 10px; }
.quiz-option { padding: 13px 16px; border: 1px solid #c4d0c0; color: var(--text); background: transparent; border-radius: 12px; text-align: left; }
.quiz-option:hover { background: var(--green-light); }
.quiz-option:disabled { cursor: default; opacity: .85; }
.quiz-option.correct { border-color: #3d9858; background: #d7f1d9; color: #173d2a; }
.quiz-option.wrong { border-color: #c66c5c; background: #f9ded8; color: #65291f; }
.quiz-status { color: var(--muted); margin: 15px 0; }

/* Sound */
.sound-panel {
  display: flex; align-items: center; justify-content: space-between; gap: 20px;
  padding: 28px 32px; background: var(--green-light); border-radius: 20px;
}
.sound-panel p { color: var(--muted); font-size: .9rem; }
.sound-status { font-size: .85rem; margin-top: 5px; }

/* Footer */
footer { background: #102b1c; color: white; padding: 55px 0 25px; }
.footer-grid { display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 35px; }
footer h3 { font-size: 1.3rem; margin-bottom: 15px; }
footer p, footer a { color: #cfddcf; font-size: .9rem; }
footer ul { list-style: none; display: grid; gap: 8px; }
footer a:hover { color: #e6d486; }
.footer-quote { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-style: italic; margin-top: 16px; color: #e6d486; }
.copyright { border-top: 1px solid #365442; margin-top: 35px; padding-top: 20px; text-align: center; font-size: .82rem; color: #bacaba; }

/* Modal */
.modal {
  position: fixed; z-index: 300; inset: 0; background: rgba(5,15,8,.94);
  display: none; align-items: center; justify-content: center; padding: 25px;
}
.modal.open { display: flex; }
.modal img { max-width: 100%; max-height: 80vh; width: auto; border-radius: 12px; }
.modal-close {
  position: absolute; top: 20px; right: 25px; width: 45px; height: 45px;
  border: 0; border-radius: 50%; background: white; color: #163322; font-size: 1.5rem;
}
.modal-caption { position: absolute; bottom: 20px; color: white; text-align: center; left: 10px; right: 10px; }
.top-btn {
  position: fixed; z-index: 90; bottom: 22px; right: 22px;
  width: 46px; height: 46px; border: 0; border-radius: 50%;
  background: var(--green); color: white; font-size: 1.25rem;
  box-shadow: var(--shadow); display: none;
}
.top-btn.show { display: block; }
.reveal { opacity: 0; transform: translateY(22px); transition: opacity .7s, transform .7s; }
.reveal.visible { opacity: 1; transform: translateY(0); }
[hidden] { display: none !important; }

@media (max-width: 950px) {
  .nav-links { gap: 12px; }
  .nav-links a { font-size: .8rem; }
  .card-grid { grid-template-columns: repeat(2, 1fr); }
  .about-grid { gap: 35px; }
  .gallery-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 720px) {
  .navbar { padding: 10px 14px; min-height: 60px; }
  .logo { font-size: 1.15rem; }
  .menu-btn { display: grid; }
  .nav-links {
    display: none; position: absolute; top: calc(100% + 9px); left: 0; right: 0;
    padding: 18px; border-radius: 17px; background: #f7f7ed;
    box-shadow: var(--shadow); align-items: stretch; flex-direction: column; gap: 0;
  }
  .nav-links.open { display: flex; }
  .nav-links a { display: block; padding: 11px 8px; font-size: .95rem; }
  .nav-actions .btn { display: none; }
  .hero { min-height: 90svh; background-position: 58% center; }
  .hero h1 { letter-spacing: -1px; }
  .hero-note { display: none; }
  .section { padding: 70px 0; }
  .strip-grid { grid-template-columns: 1fr; gap: 15px; }
  .card-grid { grid-template-columns: 1fr; }
  .card img { height: 230px; }
  .fact-panel { grid-template-columns: 1fr; padding: 28px; }
  .gallery-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px; }
  .gallery-item, .gallery-item img { min-height: 155px; }
  .about-grid { grid-template-columns: 1fr; gap: 35px; }
  .about-image img { height: 330px; }
  .benefit-list { grid-template-columns: 1fr 1fr; }
  .quiz-card { padding: 23px; }
  .sound-panel { align-items: flex-start; flex-direction: column; padding: 24px; }
  .footer-grid { grid-template-columns: 1fr; gap: 27px; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
  }
  .reveal { opacity: 1; transform: none; }
}
</style>
</head>

<body>

<header class="navbar">
  <a class="logo" href="#home">Nature's<span>Garden</span> 🌿</a>

  <nav aria-label="Main navigation">
    <ul class="nav-links" id="navLinks">
      <li><a href="#home">Home</a></li>
      <li><a href="#explore">Explore Garden</a></li>
      <li><a href="#flowers">Flowers</a></li>
      <li><a href="#plants">Plants</a></li>
      <li><a href="#gallery">Gallery</a></li>
      <li><a href="#about">About</a></li>
    </ul>
  </nav>

  <div class="nav-actions">
    <button class="icon-btn" id="themeToggle" aria-label="Switch garden theme" title="Day/night mode">☾</button>
    <button class="icon-btn menu-btn" id="menuToggle" aria-label="Open navigation menu" aria-expanded="false">☰</button>
  </div>
</header>

<main>
<section class="hero" id="home">
  <span class="leaf" style="left:8%">🍃</span>
  <span class="leaf">🍃</span>
  <span class="leaf">🍃</span>
  <span class="leaf">🍃</span>

  <div class="container hero-content">
    <div class="eyebrow">Breathe in the beauty of nature</div>
    <h1>Welcome to the<br>World of <span>Nature</span></h1>
    <p>Discover the beauty, peace, and magic of a real garden. Wander through colorful flowers, listen to nature, and find your own peaceful corner of green.</p>

    <div class="hero-buttons">
      <a class="btn" href="#explore">🌱 Explore the Garden</a>
      <a class="btn btn-outline" href="#flowers">🌸 Discover Flowers</a>
    </div>
    <div class="scroll-indicator">SCROLL TO DISCOVER ↓</div>
  </div>

  <div class="hero-note">🌿 A little closer to nature</div>
</section>

<div class="intro-strip">
  <div class="container strip-grid">
    <div><strong><span class="counter" data-target="6">0</span>+</strong><span>Garden areas to explore</span></div>
    <div><strong><span class="counter" data-target="8">0</span>+</strong><span>Beautiful plant profiles</span></div>
    <div><strong><span class="counter" data-target="4">0</span></strong><span>Ways to explore the gallery</span></div>
  </div>
</div>

<section class="section" id="explore">
  <div class="container">
    <div class="section-heading reveal">
      <div class="eyebrow">Find your peaceful place</div>
      <h2>Explore the Garden</h2>
      <p>Every corner of a garden tells a different story. Choose an area and discover the little wonders living there.</p>
    </div>

    <div class="card-grid">
      <article class="card reveal">
        <div class="card-image"><img loading="lazy" src="https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=850&q=80" alt="Colorful flowers blooming in a garden"></div>
        <div class="card-body"><span class="tag">01 · Color</span><h3>Flower Garden</h3><p>Discover vibrant blossoms, delicate petals, and the beautiful colors of seasonal flowers.</p><a class="btn btn-small" href="#flowers">Explore Flowers →</a></div>
      </article>

      <article class="card reveal">
        <div class="card-image"><img loading="lazy" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=850&q=80" alt="Sunlight falling through a lush green forest"></div>
        <div class="card-body"><span class="tag">02 · Green</span><h3>Tree Sanctuary</h3><p>Walk beneath leafy branches and enjoy the shade, fresh air, and quiet beauty of trees.</p><a class="btn btn-small" href="#gallery">Explore Trees →</a></div>
      </article>

      <article class="card reveal">
        <div class="card-image"><img loading="lazy" src="https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=850&q=80" alt="Natural woodland habitat with rich vegetation"></div>
        <div class="card-body"><span class="tag">03 · Wildlife</span><h3>Butterfly Haven</h3><p>Learn how flowering plants support butterflies and other important pollinators.</p><a class="btn btn-small" href="#about">Explore Wildlife →</a></div>
      </article>

      <article class="card reveal">
        <div class="card-image"><img loading="lazy" src="https://images.unsplash.com/photo-1439066615861-d1af74d74000?auto=format&fit=crop&w=850&q=80" alt="Peaceful natural pond surrounded by greenery"></div>
        <div class="card-body"><span class="tag">04 · Water</span><h3>Garden Pond</h3><p>Enjoy the peaceful atmosphere of water, aquatic plants, and the life a pond can support.</p><a class="btn btn-small" href="#gallery">Explore Ponds →</a></div>
      </article>

      <article class="card reveal">
        <div class="card-image"><img loading="lazy" src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&w=850&q=80" alt="A peaceful green landscape in warm morning sunlight"></div>
        <div class="card-body"><span class="tag">05 · Peace</span><h3>Walking Paths</h3><p>Imagine a gentle morning walk along a garden path surrounded by natural beauty.</p><a class="btn btn-small" href="#gallery">Explore Landscapes →</a></div>
      </article>

      <article class="card reveal">
        <div class="card-image"><img loading="lazy" src="https://images.unsplash.com/photo-1416879595882-3373a0480b5b?auto=format&fit=crop&w=850&q=80" alt="Green plants growing in a garden"></div>
        <div class="card-body"><span class="tag">06 · Growth</span><h3>Herb & Vegetable Garden</h3><p>Discover how herbs, vegetables, soil, water, and sunlight work together to grow food.</p><a class="btn btn-small" href="#plants">Explore Plants →</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section explore-section" id="flowers">
  <div class="container">
    <div class="section-heading reveal">
      <div class="eyebrow">Nature's living colors</div>
      <h2>Meet the Flowers</h2>
      <p>Explore beautiful flowers and learn the basic care that helps them grow.</p>
    </div>

    <div class="card-grid">
      <article class="card flower-card reveal">
        <img loading="lazy" src="https://images.unsplash.com/photo-1494972308805-463bc619d34e?auto=format&fit=crop&w=750&q=80" alt="Beautiful pink rose in bloom">
        <div class="card-body"><h3>Rose</h3><div class="scientific">Rosa species</div><p>Beloved for its layered petals, fragrance, and wide range of colors.</p><div class="care"><span>☀️ 4–6+ hours of sun</span><span>💧 Water when needed</span></div></div>
      </article>

      <article class="card flower-card reveal">
        <img loading="lazy" src="https://images.unsplash.com/photo-1497250681960-ef046c08a56e?auto=format&fit=crop&w=750&q=80" alt="Fresh green foliage and growing plants">
        <div class="card-body"><h3>Lily</h3><div class="scientific">Lilium species</div><p>Elegant flowers known for their graceful shape and striking blooms.</p><div class="care"><span>☀️ Sun to partial shade</span><span>💧 Even soil moisture</span></div></div>
      </article>

      <article class="card flower-card reveal">
        <img loading="lazy" src="https://images.unsplash.com/photo-1597848212624-e6c2e6c0a3b5?auto=format&fit=crop&w=750&q=80" alt="Bright yellow sunflower">
        <div class="card-body"><h3>Sunflower</h3><div class="scientific">Helianthus annuus</div><p>A cheerful flowering plant that attracts attention with its sunny appearance.</p><div class="care"><span>☀️ Full sun</span><span>💧 Regular deep watering</span></div></div>
      </article>

      <article class="card flower-card reveal">
        <img loading="lazy" src="https://images.unsplash.com/photo-1520763185298-1b434c919102?auto=format&fit=crop&w=750&q=80" alt="Colorful tulip flowers in a garden">
        <div class="card-body"><h3>Tulip</h3><div class="scientific">Tulipa species</div><p>A spring favorite with simple, cup-shaped flowers in many colors.</p><div class="care"><span>☀️ Full sun</span><span>💧 Avoid soggy soil</span></div></div>
      </article>

      <article class="card flower-card reveal">
        <img loading="lazy" src="https://images.unsplash.com/photo-1499002238440-d264edd596ec?auto=format&fit=crop&w=750&q=80" alt="Delicate white flowers in natural light">
        <div class="card-body"><h3>Jasmine</h3><div class="scientific">Jasminum species</div><p>Known for delicate blossoms and a sweet fragrance in many varieties.</p><div class="care"><span>☀️ Sun to partial shade</span><span>💧 Moderate watering</span></div></div>
      </article>

      <article class="card flower-card reveal">
        <img loading="lazy" src="https://images.unsplash.com/photo-1508610048659-a06b669e3321?auto=format&fit=crop&w=750&q=80" alt="Pink aquatic flower in a natural setting">
        <div class="card-body"><h3>Lotus</h3><div class="scientific">Nelumbo nucifera</div><p>An iconic aquatic plant with striking flowers and broad floating leaves.</p><div class="care"><span>☀️ Full sun</span><span>💧 Grows in water</span></div></div>
      </article>
    </div>
    <p style="text-align:center;color:var(--muted);font-size:.82rem;margin-top:25px">Care needs vary by species, climate, soil, and growing conditions.</p>
  </div>
</section>

<section class="section" id="plants">
  <div class="container">
    <div class="section-heading reveal">
      <div class="eyebrow">Small seeds, big wonders</div>
      <h2>Discover the World of Plants</h2>
      <p>Plants provide food and shelter, support ecosystems, and help make gardens welcoming to wildlife.</p>
    </div>

    <div class="fact-panel reveal">
      <div>
        <div class="eyebrow">Did you know?</div>
        <h2>Every plant has a story.</h2>
        <p>From tiny seedlings to towering trees, plants grow in remarkable ways. Discover a new nature fact whenever you like.</p>
        <button class="btn" id="factBtn" style="margin-top:22px">Discover a Plant Fact ✨</button>
      </div>
      <div class="fact-box" aria-live="polite">
        <p id="factText">🌱 Click the button to discover something fascinating about the natural world.</p>
      </div>
    </div>
  </div>
</section>

<section class="section explore-section" id="gallery">
  <div class="container">
    <div class="section-heading reveal">
      <div class="eyebrow">A window into nature</div>
      <h2>Garden Photo Gallery</h2>
      <p>Browse garden-inspired photographs. Select any image to view it in a larger format.</p>
    </div>

    <div class="filters" role="group" aria-label="Filter gallery">
      <button class="filter-btn active" data-filter="all" aria-pressed="true">All</button>
      <button class="filter-btn" data-filter="flowers" aria-pressed="false">Flowers</button>
      <button class="filter-btn" data-filter="trees" aria-pressed="false">Trees</button>
      <button class="filter-btn" data-filter="ponds" aria-pressed="false">Ponds</button>
      <button class="filter-btn" data-filter="landscapes" aria-pressed="false">Landscapes</button>
    </div>

    <div class="gallery-grid">
      <button class="gallery-item" data-category="flowers" data-caption="Colorful garden flowers" aria-label="View colorful garden flowers">
        <img loading="lazy" src="https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=750&q=80" alt="Colorful garden flowers">
        <span>Flowers</span>
      </button>
      <button class="gallery-item" data-category="trees" data-caption="Green forest trees" aria-label="View green forest trees">
        <img loading="lazy" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=750&q=80" alt="Green forest trees">
        <span>Trees</span>
      </button>
      <button class="gallery-item" data-category="ponds" data-caption="Peaceful natural pond" aria-label="View a peaceful natural pond">
        <img loading="lazy" src="https://images.unsplash.com/photo-1439066615861-d1af74d74000?auto=format&fit=crop&w=750&q=80" alt="Natural pond surrounded by plants">
        <span>Ponds</span>
      </button>
      <button class="gallery-item" data-category="landscapes" data-caption="Sunlit natural landscape" aria-label="View a sunlit natural landscape">
        <img loading="lazy" src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&w=750&q=80" alt="Sunlight across a green landscape">
        <span>Landscapes</span>
      </button>
      <button class="gallery-item" data-category="flowers" data-caption="A beautiful rose" aria-label="View a rose">
        <img loading="lazy" src="https://images.unsplash.com/photo-1494972308805-463bc619d34e?auto=format&fit=crop&w=750&q=80" alt="Rose flower">
        <span>Flowers</span>
      </button>
      <button class="gallery-item" data-category="trees" data-caption="Lush green vegetation" aria-label="View lush green vegetation">
        <img loading="lazy" src="https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=750&q=80" alt="Lush vegetation in a woodland">
        <span>Trees</span>
      </button>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="container about-grid">
    <div class="about-image reveal">
      <img loading="lazy" src="https://images.unsplash.com/photo-1416879595882-3373a0480b5b?auto=format&fit=crop&w=1100&q=85" alt="A thriving garden with healthy green plants">
    </div>

    <div class="about-copy reveal">
      <div class="eyebrow">More than just a beautiful place</div>
      <h2>Why Gardens Matter</h2>
      <p>A garden is a living ecosystem. It connects people with nature, provides habitat for wildlife, and reminds us how much life depends on healthy soil, clean water, and thriving plants.</p>
      <p>Even a small garden or a few pots on a balcony can support greenery and create an inviting space for observation and learning.</p>
      <div class="benefit-list">
        <div class="benefit">🌼 <strong>Pollinators</strong><br>Flowers support bees and butterflies.</div>
        <div class="benefit">🌳 <strong>Biodiversity</strong><br>Plants provide habitat and food.</div>
        <div class="benefit">🌿 <strong>Well-being</strong><br>Green spaces invite calm and activity.</div>
        <div class="benefit">🌎 <strong>Environment</strong><br>Healthy gardens support local ecosystems.</div>
      </div>
    </div>
  </div>
</section>

<section class="section explore-section" id="quiz">
  <div class="container">
    <div class="section-heading reveal">
      <div class="eyebrow">Test your nature knowledge</div>
      <h2>The Little Garden Quiz</h2>
      <p>Answer three quick questions and see how much you know about plants.</p>
    </div>

    <div class="quiz-card reveal">
      <div id="quizContent">
        <p class="tag" id="quizProgress">Question 1 of 3</p>
        <h3 id="quizQuestion">Which part of a plant usually absorbs water from the soil?</h3>
        <div class="quiz-options" id="quizOptions"></div>
        <p class="quiz-status" id="quizStatus" aria-live="polite">Choose one answer to continue.</p>
        <button class="btn" id="nextQuestion" hidden>Next Question →</button>
      </div>
      <div id="quizResult" hidden>
        <h3>Your garden score 🌱</h3>
        <p id="scoreText"></p>
        <button class="btn" id="restartQuiz" style="margin-top:20px">Try Again ↻</button>
      </div>
    </div>
  </div>
</section>

<section class="section" id="sounds">
  <div class="container">
    <div class="sound-panel">
      <div>
        <div class="eyebrow">A moment of calm</div>
        <h3 style="font-family:'Playfair Display',serif;font-size:1.6rem;margin:8px 0">Listen to Nature</h3>
        <p>Turn on gentle synthesized birdsong-like tones for a peaceful atmosphere. Sound starts only when you choose.</p>
        <p class="sound-status" id="soundStatus" aria-live="polite">Nature sound is off.</p>
      </div>
      <button class="btn" id="soundToggle">♪ Play Nature Sounds</button>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo" href="#home" style="color:white">Nature's<span>Garden</span> 🌿</a>
        <p style="margin-top:15px">A little corner of the internet dedicated to the beauty, wonder, and importance of the natural world.</p>
        <p class="footer-quote">"Look deep into nature, and you will understand everything better."</p>
      </div>
      <div>
        <h3>Explore</h3>
        <ul>
          <li><a href="#explore">Garden Areas</a></li>
          <li><a href="#flowers">Flowers</a></li>
          <li><a href="#plants">Plant Facts</a></li>
          <li><a href="#gallery">Photo Gallery</a></li>
        </ul>
      </div>
      <div>
        <h3>Discover More</h3>
        <ul>
          <li><a href="#about">Why Gardens Matter</a></li>
          <li><a href="#quiz">Garden Quiz</a></li>
          <li><a href="#sounds">Nature Sounds</a></li>
          <li><a href="#home">Back to Home ↑</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">© <span id="year"></span> Nature's Garden · Made with 🌿 and a love for nature.</div>
  </div>
</footer>

<button class="top-btn" id="topBtn" aria-label="Back to top">↑</button>

<div class="modal" id="imageModal" role="dialog" aria-modal="true" aria-label="Garden photograph viewer">
  <button class="modal-close" id="modalClose" aria-label="Close image viewer">×</button>
  <img id="modalImage" src="" alt="">
  <p class="modal-caption" id="modalCaption"></p>
</div>

<script>
/* Navigation */
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');

menuToggle.addEventListener('click', () => {
  const open = navLinks.classList.toggle('open');
  menuToggle.setAttribute('aria-expanded', String(open));
  menuToggle.setAttribute('aria-label', open ? 'Close navigation menu' : 'Open navigation menu');
  menuToggle.textContent = open ? '✕' : '☰';
});

navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.textContent = '☰';
  });
});

/* Day and night theme */
const themeToggle = document.getElementById('themeToggle');
themeToggle.addEventListener('click', () => {
  const night = document.body.classList.toggle('night');
  themeToggle.textContent = night ? '☀' : '☾';
  themeToggle.setAttribute('aria-label', night ? 'Switch to day theme' : 'Switch to night theme');
  document.querySelector('meta[name="theme-color"]').content = night ? '#101c16' : '#173d2a';
});

/* Reveal elements */
const revealElements = document.querySelectorAll('.reveal');

if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  revealElements.forEach(el => revealObserver.observe(el));
} else {
  revealElements.forEach(el => el.classList.add('visible'));
}

/* Animated statistics */
const counters = document.querySelectorAll('.counter');
const counterObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    const target = Number(el.dataset.target);
    const start = performance.now();
    const duration = 1100;

    function update(now) {
      const progress = Math.min((now - start) / duration, 1);
      el.textContent = Math.round(target * progress);
      if (progress < 1) requestAnimationFrame(update);
    }

    requestAnimationFrame(update);
    counterObserver.unobserve(el);
  });
}, { threshold: 0.7 });

counters.forEach(el => counterObserver.observe(el));

/* Random plant facts */
const facts = [
  '🌱 Plants use sunlight, water, and carbon dioxide to make sugars through photosynthesis.',
  '🐝 Bees and many other pollinators help flowering plants reproduce.',
  '🌳 Tree roots help hold soil together and can reduce erosion.',
  '🌻 Sunflowers belong to the daisy family, Asteraceae.',
  '🪴 Healthy soil contains living organisms that help recycle nutrients.',
  '🌸 Some flowers open or close in response to light and environmental conditions.',
  '💧 Water moves from roots through plant tissues to leaves, where much of it evaporates.',
  '🍂 Fallen leaves can decompose and return nutrients to the soil.',
  '🌿 Native plants can provide food and shelter for local wildlife.',
  '🌎 A garden with different plant species can support a wider range of insects and other animals.'
];

let lastFact = -1;
document.getElementById('factBtn').addEventListener('click', () => {
  let index;
  do { index = Math.floor(Math.random() * facts.length); }
  while (facts.length > 1 && index === lastFact);
  lastFact = index;
  document.getElementById('factText').textContent = facts[index];
});

/* Gallery filters */
const filterButtons = document.querySelectorAll('.filter-btn');
const galleryItems = document.querySelectorAll('.gallery-item');

filterButtons.forEach(button => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;

    filterButtons.forEach(btn => {
      const active = btn === button;
      btn.classList.toggle('active', active);
      btn.setAttribute('aria-pressed', String(active));
    });

    galleryItems.forEach(item => {
      item.hidden = filter !== 'all' && item.dataset.category !== filter;
    });
  });
});

/* Accessible image viewer */
const modal = document.getElementById('imageModal');
const modalImage = document.getElementById('modalImage');
const modalCaption = document.getElementById('modalCaption');
const modalClose = document.getElementById('modalClose');
let previousFocus = null;

function closeModal() {
  modal.classList.remove('open');
  document.body.style.overflow = '';
  modalImage.src = '';
  if (previousFocus) previousFocus.focus();
}

galleryItems.forEach(item => {
  item.addEventListener('click', () => {
    const img = item.querySelector('img');
    previousFocus = item;
    modalImage.src = img.currentSrc || img.src;
    modalImage.alt = img.alt;
    modalCaption.textContent = item.dataset.caption;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    modalClose.focus();
  });
});

modalClose.addEventListener('click', closeModal);
modal.addEventListener('click', e => {
  if (e.target === modal) closeModal();
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();

  if (e.key === 'Tab' && modal.classList.contains('open')) {
    e.preventDefault();
    modalClose.focus();
  }
});

/* Garden quiz */
const questions = [
  {
    question: 'Which part of a plant usually absorbs water from the soil?',
    options: ['Flowers', 'Roots', 'Petals', 'Fruit'],
    answer: 1,
    explanation: 'Roots absorb water and mineral nutrients from the soil.'
  },
  {
    question: 'What do most green plants need for photosynthesis?',
    options: ['Sunlight', 'Plastic', 'Darkness all day', 'Salt water only'],
    answer: 0,
    explanation: 'Light supplies the energy used in photosynthesis.'
  },
  {
    question: 'Which animal is an important pollinator?',
    options: ['Earthworm', 'Bee', 'Fish', 'Snail'],
    answer: 1,
    explanation: 'Bees transfer pollen between flowers as they collect food.'
  }
];

let questionIndex = 0;
let score = 0;
let answered = false;

const quizQuestion = document.getElementById('quizQuestion');
const quizOptions = document.getElementById('quizOptions');
const quizStatus = document.getElementById('quizStatus');
const quizProgress = document.getElementById('quizProgress');
const nextQuestion = document.getElementById('nextQuestion');
const quizContent = document.getElementById('quizContent');
const quizResult = document.getElementById('quizResult');

function renderQuestion() {
  answered = false;
  const q = questions[questionIndex];
  quizProgress.textContent = `Question ${questionIndex + 1} of ${questions.length}`;
  quizQuestion.textContent = q.question;
  quizOptions.replaceChildren();
  quizStatus.textContent = 'Choose one answer to continue.';
  nextQuestion.hidden = true;

  q.options.forEach((option, index) => {
    const btn = document.createElement('button');
    btn.className = 'quiz-option';
    btn.textContent = option;
    btn.addEventListener('click', () => chooseAnswer(index));
    quizOptions.appendChild(btn);
  });
}

function chooseAnswer(index) {
  if (answered) return;
  answered = true;

  const q = questions[questionIndex];
  const buttons = quizOptions.querySelectorAll('button');

  buttons.forEach((btn, i) => {
    btn.disabled = true;
    if (i === q.answer) btn.classList.add('correct');
    if (i === index && i !== q.answer) btn.classList.add('wrong');
  });

  if (index === q.answer) {
    score++;
    quizStatus.textContent = 'Correct! ' + q.explanation;
  } else {
    quizStatus.textContent = 'Not quite. ' + q.explanation;
  }

  nextQuestion.textContent = questionIndex === questions.length - 1 ? 'See My Score →' : 'Next Question →';
  nextQuestion.hidden = false;
}

nextQuestion.addEventListener('click', () => {
  questionIndex++;
  if (questionIndex < questions.length) {
    renderQuestion();
  } else {
    quizContent.hidden = true;
    quizResult.hidden = false;
    document.getElementById('scoreText').textContent =
      `You scored ${score} out of ${questions.length}. ` +
      (score === questions.length ? 'Wonderful! You are a garden expert in the making. 🌿' :
      score >= 2 ? 'Great work! Keep discovering nature.' : 'Keep exploring. Every garden teaches us something new.');
  }
});

document.getElementById('restartQuiz').addEventListener('click', () => {
  questionIndex = 0;
  score = 0;
  quizContent.hidden = false;
  quizResult.hidden = true;
  renderQuestion();
});

renderQuestion();

/* Optional synthesized nature ambience.
   Uses Web Audio API; no downloaded audio or autoplay required. */
let audioContext = null;
let audioNodes = [];
let soundOn = false;
let soundTimer = null;

function playBirdNote() {
  if (!soundOn || !audioContext) return;

  const now = audioContext.currentTime;
  const oscillator = audioContext.createOscillator();
  const gain = audioContext.createGain();

  oscillator.type = 'sine';
  const startFrequency = 1500 + Math.random() * 800;
  oscillator.frequency.setValueAtTime(startFrequency, now);
  oscillator.frequency.exponentialRampToValueAtTime(startFrequency * 1.3, now + 0.08);
  oscillator.frequency.exponentialRampToValueAtTime(startFrequency * 0.85, now + 0.24);

  gain.gain.setValueAtTime(0.0001, now);
  gain.gain.exponentialRampToValueAtTime(0.035, now + 0.035);
  gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.28);

  oscillator.connect(gain);
  gain.connect(audioContext.destination);
  oscillator.start(now);
  oscillator.stop(now + 0.3);
  audioNodes.push(oscillator);
  oscillator.onended = () => {
    oscillator.disconnect();
    gain.disconnect();
    audioNodes = audioNodes.filter(node => node !== oscillator);
  };
}

function stopNatureSound() {
  soundOn = false;
  clearInterval(soundTimer);
  if (audioContext) {
    audioContext.close().catch(() => {});
    audioContext = null;
  }
  audioNodes = [];
  document.getElementById('soundToggle').textContent = '♪ Play Nature Sounds';
  document.getElementById('soundStatus').textContent = 'Nature sound is off.';
}

document.getElementById('soundToggle').addEventListener('click', async () => {
  if (soundOn) {
    stopNatureSound();
    return;
  }

  const AudioContextClass = window.AudioContext || window.webkitAudioContext;
  if (!AudioContextClass) {
    document.getElementById('soundStatus').textContent =
      'Your browser does not support generated nature sounds.';
    return;
  }

  try {
    audioContext = new AudioContextClass();
    await audioContext.resume();
    soundOn = true;
    document.getElementById('soundToggle').textContent = 'Ⅱ Stop Nature Sounds';
    document.getElementById('soundStatus').textContent =
      'Gentle synthesized bird-like tones are playing. This is not a real birdsong recording.';
    playBirdNote();
    soundTimer = setInterval(() => {
      if (Math.random() > 0.25) playBirdNote();
    }, 800 + Math.random() * 600);
  } catch (error) {
    stopNatureSound();
    document.getElementById('soundStatus').textContent =
      'Sound could not start. Please try again.';
  }
});

/* Back to top */
const topBtn = document.getElementById('topBtn');
window.addEventListener('scroll', () => {
  topBtn.classList.toggle('show', window.scrollY > 500);
}, { passive: true });

topBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

/* Current year */
document.getElementById('year').textContent = new Date().getFullYear();

/* Stop audio if the page is hidden */
document.addEventListener('visibilitychange', () => {
  if (document.hidden && soundOn) stopNatureSound();
});
</script>
</body>
</html>
