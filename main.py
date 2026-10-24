
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#164b32">
    <title>Peaceful Garden | A Beautiful World of Nature</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
            scroll-padding-top: 75px;
        }

        body {
            font-family: 'Trebuchet MS', Arial, sans-serif;
            background: #f5fff2;
            color: #24452d;
            overflow-x: hidden;
            line-height: 1.7;
        }

        /* NAVIGATION */

        nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 14px 7%;
            background: rgba(12, 54, 35, 0.92);
            backdrop-filter: blur(12px);
            color: white;
        }

        .logo {
            font-size: 1.4rem;
            font-weight: bold;
            color: #d7ffad;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
            font-size: 0.9rem;
            transition: color 0.3s;
        }

        nav a:hover {
            color: #d7ffad;
        }

        /* HERO SECTION */

        .hero {
            min-height: 100vh;
            min-height: 100svh;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 110px 20px 150px;
            overflow: hidden;
            isolation: isolate;
            background:
                linear-gradient(
                    180deg,
                    rgba(17, 72, 47, 0.12),
                    rgba(8, 54, 32, 0.65)
                ),
                linear-gradient(180deg, #9de8ff 0%, #e1ffcd 57%, #66bd56 100%);
        }

        .sun {
            position: absolute;
            top: 16%;
            right: 14%;
            width: 95px;
            height: 95px;
            background: #fff4a9;
            border-radius: 50%;
            box-shadow: 0 0 65px #fff4a9;
            z-index: -1;
        }

        .hero-content {
            max-width: 850px;
            color: white;
            z-index: 3;
            animation: appear 1.4s ease;
        }

        .eyebrow {
            display: inline-block;
            padding: 7px 17px;
            border: 1px solid rgba(255,255,255,0.7);
            border-radius: 30px;
            background: rgba(255,255,255,0.16);
            font-size: 0.9rem;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }

        h1 {
            font-size: clamp(2.8rem, 8vw, 6.5rem);
            line-height: 1.05;
            margin-bottom: 24px;
            text-shadow: 0 5px 20px rgba(0, 45, 20, 0.35);
        }

        h1 span {
            color: #e7ffb4;
        }

        .hero-content p {
            max-width: 600px;
            margin: 0 auto 30px;
            font-size: clamp(1rem, 2.5vw, 1.2rem);
        }

        .btn {
            display: inline-block;
            padding: 13px 28px;
            border-radius: 30px;
            background: #fff;
            color: #17633b;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        }

        .btn:hover {
            background: #dfffad;
            transform: translateY(-4px);
        }

        /* HILLS */

        .hill {
            position: absolute;
            bottom: -100px;
            width: 120%;
            height: 250px;
            border-radius: 50% 50% 0 0;
            z-index: 0;
        }

        .hill-back {
            left: -20%;
            background: #77c96c;
            bottom: -120px;
        }

        .hill-front {
            right: -25%;
            height: 200px;
            background: #328b45;
            bottom: -130px;
        }

        /* FLOATING BUTTERFLIES */

        .butterfly {
            position: absolute;
            font-size: 2rem;
            animation: flutter 8s ease-in-out infinite;
            z-index: 2;
        }

        .b1 {
            top: 27%;
            left: 12%;
        }

        .b2 {
            top: 52%;
            right: 12%;
            animation-delay: -3s;
        }

        .b3 {
            top: 20%;
            left: 65%;
            animation-delay: -5s;
        }

        @keyframes flutter {
            0%, 100% {
                transform: translate(0, 0) rotate(-8deg);
            }
            50% {
                transform: translate(30px, -35px) rotate(12deg);
            }
        }

        @keyframes appear {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* GENERAL SECTIONS */

        section {
            padding: 90px 7%;
            scroll-margin-top: 65px;
        }

        .section-title {
            text-align: center;
            margin-bottom: 45px;
        }

        .section-title small {
            color: #4c9d52;
            text-transform: uppercase;
            letter-spacing: 3px;
            font-weight: bold;
        }

        .section-title h2 {
            color: #205d37;
            font-size: clamp(2rem, 5vw, 3.3rem);
            line-height: 1.2;
            margin-top: 10px;
        }

        .section-title p {
            max-width: 620px;
            margin: 15px auto 0;
            color: #66816a;
        }

        /* ABOUT THE GARDEN */

        .about {
            background: #f5fff2;
        }

        .about-card {
            max-width: 950px;
            margin: auto;
            padding: clamp(25px, 6vw, 55px);
            background: white;
            border-radius: 25px;
            box-shadow: 0 12px 45px rgba(36, 93, 44, 0.09);
            border: 1px solid #e2f4da;
            text-align: center;
        }

        .about-icon {
            font-size: 4rem;
            margin-bottom: 15px;
        }

        .about-card p {
            font-size: clamp(1rem, 2vw, 1.15rem);
            color: #536c55;
            line-height: 2;
        }

        .highlight {
            color: #2d9149;
            font-weight: bold;
        }

        /* NATURE CARDS */

        .nature {
            background: linear-gradient(180deg, #e9fbe4, #f8fff5);
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 25px;
            max-width: 1150px;
            margin: auto;
        }

        .card {
            background: white;
            border-radius: 22px;
            overflow: hidden;
            box-shadow: 0 8px 30px rgba(31, 82, 42, 0.08);
            transition: transform 0.35s, box-shadow 0.35s;
            text-align: center;
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 18px 35px rgba(31, 82, 42, 0.15);
        }

        .card-visual {
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 5rem;
        }

        .flowers-bg {
            background: linear-gradient(135deg, #ffe1ec, #fff2c9);
        }

        .birds-bg {
            background: linear-gradient(135deg, #cceeff, #d8f5d5);
        }

        .trees-bg {
            background: linear-gradient(135deg, #d6f2c9, #9edc9b);
        }

        .card-content {
            padding: 24px 22px 30px;
        }

        .card h3 {
            font-size: 1.4rem;
            color: #24643b;
            margin-bottom: 10px;
        }

        .card p {
            font-size: 0.96rem;
            color: #69806a;
        }

        /* PEACEFUL MESSAGE */

        .quote {
            text-align: center;
            color: white;
            background:
                linear-gradient(rgba(11, 64, 36, 0.85),
                                rgba(11, 64, 36, 0.88)),
                linear-gradient(135deg, #55a94d, #164b32);
            padding: 100px 8%;
        }

        .quote .big-leaf {
            font-size: 4rem;
        }

        .quote h2 {
            font-size: clamp(2rem, 5vw, 3.5rem);
            margin: 15px auto;
            max-width: 800px;
            line-height: 1.3;
        }

        .quote p {
            color: #d7f1d0;
            max-width: 600px;
            margin: auto;
        }

        /* FLOWER GALLERY */

        .gallery {
            background: #fffdf5;
        }

        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
            max-width: 1100px;
            margin: auto;
        }

        .flower-box {
            min-height: 180px;
            border-radius: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 6px;
            transition: transform 0.3s;
        }

        .flower-box:hover {
            transform: scale(1.04);
        }

        .flower-box span {
            font-size: 4rem;
        }

        .flower-box h3 {
            font-size: 1.1rem;
            color: #315b35;
        }

        .pink { background: #ffe6f0; }
        .yellow { background: #fff4bf; }
        .purple { background: #eee3ff; }
        .orange { background: #ffead8; }
        .blue { background: #e0f3ff; }
        .green { background: #e0f6d8; }

        /* FINAL SECTION */

        .visit {
            text-align: center;
            background: linear-gradient(180deg, #e9fbe4, #d3f0c9);
        }

        .visit h2 {
            font-size: clamp(2rem, 5vw, 3.5rem);
            color: #205d37;
            margin-bottom: 15px;
        }

        .visit p {
            max-width: 650px;
            margin: 0 auto 25px;
            color: #5b785e;
        }

        .visit .btn {
            background: #21683d;
            color: white;
        }

        /* FOOTER */

        footer {
            text-align: center;
            padding: 25px 15px;
            background: #103c29;
            color: #d6ebd4;
        }

        footer span {
            color: #caff9b;
        }

        /* SCROLL TO TOP */

        .top-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 45px;
            height: 45px;
            border: none;
            border-radius: 50%;
            background: #21683d;
            color: white;
            font-size: 1.4rem;
            cursor: pointer;
            z-index: 90;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            opacity: 0;
            pointer-events: none;
            transform: translateY(10px);
            transition: 0.3s;
        }

        .top-btn.visible {
            opacity: 1;
            pointer-events: auto;
            transform: translateY(0);
        }

        /* MOBILE RESPONSIVE */

        @media (max-width: 800px) {
            nav {
                padding: 12px 5%;
            }

            .logo {
                font-size: 1.1rem;
            }

            nav a {
                margin-left: 10px;
                font-size: 0.78rem;
            }

            .cards {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .card:last-child {
                grid-column: 1 / -1;
                max-width: 100%;
            }

            .gallery-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            section {
                padding: 70px 5%;
            }

            .hero {
                padding-left: 7%;
                padding-right: 7%;
            }
        }

        @media (max-width: 420px) {
            nav {
                padding: 12px 4%;
            }

            .logo {
                font-size: 1rem;
            }

            nav a {
                margin-left: 7px;
                font-size: 0.72rem;
            }

            .cards {
                grid-template-columns: 1fr;
            }

            .card:last-child {
                grid-column: auto;
            }

            .gallery-grid {
                gap: 12px;
            }

            .flower-box {
                min-height: 145px;
            }

            .flower-box span {
                font-size: 3.2rem;
            }

            .sun {
                width: 65px;
                height: 65px;
            }

            .butterfly {
                font-size: 1.5rem;
            }
        }

        /* REDUCE ANIMATION WHEN REQUESTED BY DEVICE */

        @media (prefers-reduced-motion: reduce) {
            html {
                scroll-behavior: auto;
            }

            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
    </style>
</head>

<body>

    <!-- NAVIGATION -->
    <nav>
        <div class="logo">🌿 Peaceful Garden</div>

        <div>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#nature">Nature</a>
            <a href="#gallery">Flowers</a>
        </div>
    </nav>

    <!-- HERO -->
    <header class="hero" id="home">
        <div class="sun"></div>

        <div class="butterfly b1">🦋</div>
        <div class="butterfly b2">🦋</div>
        <div class="butterfly b3">🦋</div>

        <div class="hero-content">
            <div class="eyebrow">WELCOME TO NATURE</div>

            <h1>A World of <span>Flowers</span></h1>

            <p>
                Discover a peaceful garden where colorful flowers bloom,
                butterflies dance, birds sing, and nature tells its beautiful story.
            </p>

            <a href="#about" class="btn">Explore the Garden ↓</a>
        </div>

        <div class="hill hill-back"></div>
        <div class="hill hill-front"></div>
    </header>

    <!-- ABOUT -->
    <section class="about" id="about">

        <div class="section-title">
            <small>Discover the beauty</small>
            <h2>A Garden Full of Life</h2>
            <p>
                Step into a little world of natural beauty, freshness, and peace.
            </p>
        </div>

        <div class="about-card">
            <div class="about-icon">🌳🌷</div>

            <p>
                A garden is a beautiful and peaceful place filled with
                <span class="highlight">colorful flowers, green plants, and tall trees.</span>
                The fresh green grass covers the ground, and butterflies flutter
                from flower to flower. Birds sing sweetly in the branches, while
                bees collect nectar from the flowers. A gentle breeze makes the
                leaves sway, spreading a refreshing feeling throughout the garden.
                There are different kinds of flowers, such as roses, lilies, and
                sunflowers, which make the garden look bright and attractive.
                The fragrance of the flowers fills the air, and the sound of
                birds creates a pleasant atmosphere. A garden is a perfect place
                to relax, enjoy nature, and spend time peacefully.
            </p>
        </div>
    </section>

    <!-- NATURE CARDS -->
    <section class="nature" id="nature">

        <div class="section-title">
            <small>Little wonders of nature</small>
            <h2>Life in the Garden</h2>
            <p>
                Every little thing in a garden adds its own magic and beauty.
            </p>
        </div>

        <div class="cards">

            <article class="card">
                <div class="card-visual flowers-bg">🌺🌸🌼</div>
                <div class="card-content">
                    <h3>Colorful Flowers</h3>
                    <p>
                        Roses, lilies, and sunflowers fill the garden with
                        beautiful colors and a lovely fragrance.
                    </p>
                </div>
            </article>

            <article class="card">
                <div class="card-visual birds-bg">🐦🦋🐝</div>
                <div class="card-content">
                    <h3>Birds & Butterflies</h3>
                    <p>
                        Sweet bird songs and dancing butterflies make every
                        corner of the garden feel alive.
                    </p>
                </div>
            </article>

            <article class="card">
                <div class="card-visual trees-bg">🌳🌿🍃</div>
                <div class="card-content">
                    <h3>Green Nature</h3>
                    <p>
                        Tall trees, fresh grass, and gentle breezes create
                        a refreshing place to rest and relax.
                    </p>
                </div>
            </article>

        </div>
    </section>

    <!-- PEACEFUL MESSAGE -->
    <section class="quote">
        <div class="big-leaf">🍃</div>

        <h2>Find Your Peace in the Beauty of Nature</h2>

        <p>
            Breathe deeply, listen to the birds, feel the gentle breeze,
            and let the peaceful garden brighten your day.
        </p>
    </section>

    <!-- FLOWER GALLERY -->
    <section class="gallery" id="gallery">

        <div class="section-title">
            <small>A rainbow of petals</small>
            <h2>Flowers of the Garden</h2>
            <p>
                Each flower has its own charm. Together, they make the garden magical.
            </p>
        </div>

        <div class="gallery-grid">

            <div class="flower-box pink">
                <span>🌹</span>
                <h3>Rose</h3>
            </div>

            <div class="flower-box yellow">
                <span>🌻</span>
                <h3>Sunflower</h3>
            </div>

            <div class="flower-box purple">
                <span>🪻</span>
                <h3>Lavender</h3>
            </div>

            <div class="flower-box orange">
                <span>🌷</span>
                <h3>Tulip</h3>
            </div>

            <div class="flower-box blue">
                <span>💠</span>
                <h3>Blue Blooms</h3>
            </div>

            <div class="flower-box green">
                <span>🌼</span>
                <h3>Daisy</h3>
            </div>

        </div>
    </section>

    <!-- ENDING -->
    <section class="visit">
        <div style="font-size: 4rem;">🦋🌿🌸</div>

        <h2>Let Nature Bring You Joy</h2>

        <p>
            A garden reminds us that beauty can be found in simple things:
            a blooming flower, a singing bird, a green leaf, and a peaceful moment.
            Take care of nature, and nature will continue to inspire us.
        </p>

        <a href="#home" class="btn">Back to the Beginning ↑</a>
    </section>

    <!-- FOOTER -->
    <footer>
        <p>Made with <span>♥</span> for the beauty of nature</p>
        <p>© <span id="year"></span> Peaceful Garden | Every flower tells a story.</p>
    </footer>

    <!-- SCROLL TO TOP BUTTON -->
    <button class="top-btn" id="topBtn"
            aria-label="Scroll to top" title="Back to top">
        ↑
    </button>

    <script>
        // Automatically update the year
        document.getElementById("year").textContent =
            new Date().getFullYear();

        // Show the scroll-to-top button after scrolling
        const topBtn = document.getElementById("topBtn");

        window.addEventListener("scroll", function () {
            if (window.scrollY > 350) {
                topBtn.classList.add("visible");
            } else {
                topBtn.classList.remove("visible");
            }
        });

        // Scroll smoothly to the top
        topBtn.addEventListener("click", function () {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    </script>

</body>
</html>
