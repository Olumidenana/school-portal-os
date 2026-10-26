with open(r"C:\Users\giant\.gemini\antigravity\scratch\school-portal-os\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update the 3 cards in the Blog & News section to have working click handlers
old_cards = """      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- News Card 1: Congratulations Award Badge (From PDF Page 4) -->
        <div class="bg-white rounded-3xl border-2 border-brand-deepNavy shadow-pdf-green overflow-hidden flex flex-col justify-between hover:-translate-y-1 transition-transform">
          <div>
            <div class="p-6 bg-gradient-to-br from-amber-50 to-amber-100 flex items-center justify-center border-b border-gray-100">
              <img src="images/crops/award_congrats_badge.jpg" alt="Olive Branches Congratulations Badge" class="max-h-48 object-contain">
            </div>
            <div class="p-6 space-y-2">
              <div class="flex items-center space-x-1.5 text-xs font-bold text-brand-gold">
                <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
                <span>9. February 2026</span>
              </div>
              <h3 class="font-headline font-black text-xl text-brand-deepNavy">
                Congratulations!
              </h3>
              <p class="font-body text-xs sm:text-sm text-gray-600 leading-relaxed">
                Huge Congratulations To Olive Branches Schools, Osogbo, Nigeria, on being recognized for outstanding performance in National Mathematics & Science Olympiad!
              </p>
            </div>
          </div>
          <div class="p-6 pt-0 flex items-center justify-between text-xs font-bold text-brand-forest">
            <button onclick="alert('Full article: Olive Branches students clinched top honors in Osun State.')" class="hover:underline flex items-center space-x-1">
              <span>Read More</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
            <button onclick="navigator.clipboard?.writeText(window.location.href); alert('Article link copied to clipboard!');" class="p-2 rounded-full bg-gray-100 hover:bg-gray-200">
              <i data-lucide="share-2" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- News Card 2: Excursions to London & Osun Sacred Grove -->
        <div class="bg-white rounded-3xl border-2 border-brand-deepNavy shadow-pdf-green overflow-hidden flex flex-col justify-between hover:-translate-y-1 transition-transform">
          <div>
            <div class="h-48 overflow-hidden">
              <img src="images/crops/excursion_trafalgar_square.jpg" alt="Trafalgar Square London Excursion" class="w-full h-full object-cover">
            </div>
            <div class="p-6 space-y-2">
              <div class="flex items-center space-x-1.5 text-xs font-bold text-brand-gold">
                <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
                <span>International Tour</span>
              </div>
              <h3 class="font-headline font-black text-xl text-brand-deepNavy">
                London Educational Tour
              </h3>
              <p class="font-body text-xs sm:text-sm text-gray-600 leading-relaxed">
                Scholars of The Olive Branches explore Trafalgar Square, British Museum, and Greenwich Royal Observatory during experiential summer learning tour.
              </p>
            </div>
          </div>
          <div class="p-6 pt-0 flex items-center justify-between text-xs font-bold text-brand-forest">
            <button onclick="scrollToSection('gallery')" class="hover:underline flex items-center space-x-1">
              <span>View Photos</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- News Card 3: Sparkle Nite Arts & Performance -->
        <div class="bg-white rounded-3xl border-2 border-brand-deepNavy shadow-pdf-green overflow-hidden flex flex-col justify-between hover:-translate-y-1 transition-transform">
          <div>
            <div class="h-48 overflow-hidden">
              <img src="images/crops/gallery_sparkle_nite.jpg" alt="Sparkle Nite Performance" class="w-full h-full object-cover">
            </div>
            <div class="p-6 space-y-2">
              <div class="flex items-center space-x-1.5 text-xs font-bold text-brand-gold">
                <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
                <span>Campus Culture</span>
              </div>
              <h3 class="font-headline font-black text-xl text-brand-deepNavy">
                Annual Sparkle Nite
              </h3>
              <p class="font-body text-xs sm:text-sm text-gray-600 leading-relaxed">
                A dazzling showcase of music, classical ballet, drama, and public speaking celebrating our students' multifaceted God-given talents.
              </p>
            </div>
          </div>
          <div class="p-6 pt-0 flex items-center justify-between text-xs font-bold text-brand-forest">
            <button onclick="scrollToSection('gallery')" class="hover:underline flex items-center space-x-1">
              <span>View Gallery</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

      </div>"""

new_cards = """      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- News Card 1: Congratulations Award Badge -->
        <div class="bg-white rounded-3xl border-2 border-brand-deepNavy shadow-pdf-green overflow-hidden flex flex-col justify-between hover:-translate-y-1 transition-transform group cursor-pointer" onclick="openArticleModal('congratulations')">
          <div>
            <div class="p-6 bg-gradient-to-br from-amber-50 to-amber-100 flex items-center justify-center border-b border-gray-100 overflow-hidden">
              <img src="images/crops/award_congrats_badge.jpg" alt="Olive Branches Congratulations Badge" class="max-h-48 object-contain group-hover:scale-105 transition-transform duration-300">
            </div>
            <div class="p-6 space-y-2">
              <div class="flex items-center justify-between text-xs font-bold">
                <span class="text-brand-gold flex items-center space-x-1">
                  <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
                  <span>Feb 9, 2026</span>
                </span>
                <span class="bg-amber-100 text-amber-900 px-2.5 py-0.5 rounded-full text-[10px] uppercase font-black">
                  Olympiad Honors
                </span>
              </div>
              <h3 class="font-headline font-black text-xl text-brand-deepNavy group-hover:text-brand-forest transition-colors">
                Congratulations to Our Scholars!
              </h3>
              <p class="font-body text-xs sm:text-sm text-gray-600 leading-relaxed">
                Huge Congratulations To Olive Branches Schools, Osogbo, Nigeria, on being recognized for outstanding performance in the National Mathematics & Science Olympiad!
              </p>
            </div>
          </div>
          <div class="p-6 pt-0 flex items-center justify-between text-xs font-bold text-brand-forest border-t border-gray-50 pt-4 mt-2">
            <span class="text-brand-forest group-hover:text-brand-leaf flex items-center space-x-1 font-headline font-black uppercase text-xs">
              <span>Read Full Article</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </span>
            <span class="text-gray-400 font-medium">3 min read</span>
          </div>
        </div>

        <!-- News Card 2: London Tour & UNESCO Grove -->
        <div class="bg-white rounded-3xl border-2 border-brand-deepNavy shadow-pdf-green overflow-hidden flex flex-col justify-between hover:-translate-y-1 transition-transform group cursor-pointer" onclick="openArticleModal('london_tour')">
          <div>
            <div class="h-48 overflow-hidden relative">
              <img src="images/crops/excursion_trafalgar_square.jpg" alt="Trafalgar Square London Excursion" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <div class="absolute top-3 right-3 bg-brand-forest/90 text-white px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase">
                Global Tour
              </div>
            </div>
            <div class="p-6 space-y-2">
              <div class="flex items-center justify-between text-xs font-bold">
                <span class="text-brand-gold flex items-center space-x-1">
                  <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
                  <span>Jan 18, 2026</span>
                </span>
                <span class="bg-blue-100 text-blue-900 px-2.5 py-0.5 rounded-full text-[10px] uppercase font-black">
                  UN Club Excursion
                </span>
              </div>
              <h3 class="font-headline font-black text-xl text-brand-deepNavy group-hover:text-brand-forest transition-colors">
                Learning Beyond Borders
              </h3>
              <p class="font-body text-xs sm:text-sm text-gray-600 leading-relaxed">
                Scholars of The Olive Branches explore Trafalgar Square, the British Museum, and the UNESCO Osun-Osogbo Sacred Grove during our global learning expeditions.
              </p>
            </div>
          </div>
          <div class="p-6 pt-0 flex items-center justify-between text-xs font-bold text-brand-forest border-t border-gray-50 pt-4 mt-2">
            <span class="text-brand-forest group-hover:text-brand-leaf flex items-center space-x-1 font-headline font-black uppercase text-xs">
              <span>Read Full Article</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </span>
            <span class="text-gray-400 font-medium">4 min read</span>
          </div>
        </div>

        <!-- News Card 3: Sparkle Nite Arts & Performance -->
        <div class="bg-white rounded-3xl border-2 border-brand-deepNavy shadow-pdf-green overflow-hidden flex flex-col justify-between hover:-translate-y-1 transition-transform group cursor-pointer" onclick="openArticleModal('sparkle_nite')">
          <div>
            <div class="h-48 overflow-hidden relative">
              <img src="images/crops/gallery_sparkle_nite.jpg" alt="Sparkle Nite Performance" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <div class="absolute top-3 right-3 bg-pink-700/90 text-white px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase">
                Arts Gala
              </div>
            </div>
            <div class="p-6 space-y-2">
              <div class="flex items-center justify-between text-xs font-bold">
                <span class="text-brand-gold flex items-center space-x-1">
                  <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
                  <span>Dec 14, 2025</span>
                </span>
                <span class="bg-pink-100 text-pink-900 px-2.5 py-0.5 rounded-full text-[10px] uppercase font-black">
                  Annual Festival
                </span>
              </div>
              <h3 class="font-headline font-black text-xl text-brand-deepNavy group-hover:text-brand-forest transition-colors">
                Annual Sparkle Nite Gala
              </h3>
              <p class="font-body text-xs sm:text-sm text-gray-600 leading-relaxed">
                A dazzling celebration of classical ballet, orchestral melody, drama, and oratory honoring our students' multifaceted God-given talents.
              </p>
            </div>
          </div>
          <div class="p-6 pt-0 flex items-center justify-between text-xs font-bold text-brand-forest border-t border-gray-50 pt-4 mt-2">
            <span class="text-brand-forest group-hover:text-brand-leaf flex items-center space-x-1 font-headline font-black uppercase text-xs">
              <span>Read Full Article</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </span>
            <span class="text-gray-400 font-medium">3 min read</span>
          </div>
        </div>

      </div>"""

if old_cards in html:
    html = html.replace(old_cards, new_cards)
    print("Updated news cards with click handlers successfully!")
else:
    print("Warning: old_cards not matched!")

# 2. Add Article Reader Modal HTML right before footer
modal_html = """  <!-- ==========================================
       FULL ARTICLE READER MODAL
       ========================================== -->
  <div id="article-reader-modal" class="fixed inset-0 bg-black/70 backdrop-blur-md z-50 hidden flex items-center justify-center p-3 sm:p-6 overflow-y-auto">
    <div class="bg-white rounded-3xl max-w-3xl w-full shadow-2xl overflow-hidden my-auto border-2 border-brand-forest relative animate-in fade-in zoom-in-95 duration-200">
      
      <!-- Modal Close Button -->
      <button onclick="closeArticleModal()" class="absolute top-4 right-4 z-20 w-10 h-10 rounded-full bg-white/90 hover:bg-white text-gray-700 shadow-md flex items-center justify-center transition-colors">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <!-- Feature Image -->
      <div class="relative h-64 sm:h-80 w-full overflow-hidden bg-gray-100">
        <img id="modal-article-img" src="" alt="Article Banner" class="w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex items-end p-6 sm:p-8">
          <div class="space-y-2 text-white">
            <span id="modal-article-cat" class="px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider bg-brand-gold text-brand-forest inline-block shadow">
              Category
            </span>
            <h2 id="modal-article-title" class="font-headline font-black text-2xl sm:text-3xl leading-tight">
              Article Title
            </h2>
          </div>
        </div>
      </div>

      <!-- Article Metadata Bar -->
      <div class="px-6 sm:px-8 py-3 bg-green-50 border-b border-green-100 flex flex-wrap items-center justify-between text-xs text-gray-600 gap-2">
        <div class="flex items-center space-x-3">
          <span id="modal-article-author" class="font-bold text-brand-forest flex items-center space-x-1">
            <i data-lucide="user" class="w-3.5 h-3.5"></i>
            <span>The Olive Branches Editorial Board</span>
          </span>
          <span>•</span>
          <span id="modal-article-date" class="flex items-center space-x-1">
            <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
            <span>Date</span>
          </span>
        </div>
        <span id="modal-article-readtime" class="text-gray-500 font-medium">3 min read</span>
      </div>

      <!-- Article Rich Body Content -->
      <div id="modal-article-body" class="p-6 sm:p-8 space-y-4 font-body text-gray-800 leading-relaxed max-h-[50vh] overflow-y-auto">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Modal Bottom Actions & Share -->
      <div class="p-4 sm:p-6 bg-gray-50 border-t border-gray-100 flex flex-col sm:flex-row justify-between items-center gap-3">
        <div class="flex items-center space-x-2 text-xs font-bold text-gray-600">
          <span>Share Article:</span>
          <button onclick="shareArticleWhatsApp()" class="p-2 rounded-full bg-green-100 hover:bg-green-200 text-green-800" title="Share to WhatsApp">
            <i data-lucide="message-circle" class="w-4 h-4"></i>
          </button>
          <button onclick="navigator.clipboard?.writeText(window.location.href); alert('Article link copied to clipboard!');" class="p-2 rounded-full bg-gray-200 hover:bg-gray-300 text-gray-700" title="Copy Link">
            <i data-lucide="share-2" class="w-4 h-4"></i>
          </button>
        </div>

        <button onclick="closeArticleModal()" class="w-full sm:w-auto bg-brand-forest hover:bg-green-900 text-white text-xs font-headline font-bold px-6 py-2.5 rounded-full transition-colors">
          Back to School News
        </button>
      </div>

    </div>
  </div>\n\n"""

# Place modal before </footer>
if "  <!-- ==========================================\n       FOOTER\n       ========================================== -->" in html:
    html = html.replace("  <!-- ==========================================\n       FOOTER\n       ========================================== -->", modal_html + "  <!-- ==========================================\n       FOOTER\n       ========================================== -->")
    print("Added Article Reader Modal HTML successfully!")
else:
    print("Warning: footer marker not matched directly!")

# 3. Add Article Database and Reader JS functions
article_js = """    // Full Article Database for The Olive Branches Journal & News
    const articlesDatabase = {
      congratulations: {
        title: "Congratulations! Olive Branches Schools Recognized for National STEM & Olympiad Excellence",
        category: "Academic Honors",
        date: "February 9, 2026",
        readTime: "3 min read",
        author: "Editorial & Academic Affairs Board",
        image: "images/crops/award_congrats_badge.jpg",
        content: `
          <p class="text-base text-gray-700 leading-relaxed mb-4">
            The management, academic staff, and student body of <strong>The Olive Branches Schools, Osogbo, Nigeria</strong> celebrate a landmark achievement as our scholars clinched top awards across the state and national levels in the recent National Mathematics & Science Olympiad competition.
          </p>
          <h4 class="text-lg font-headline font-black text-brand-forest mt-4 mb-2">Excellence in the Sciences: A Culture, Not An Accident</h4>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            Reflecting on this milestone, our Executive Director and Proprietress, <strong>Dr. (Mrs.) F. A. Omigbodun</strong>, remarked that this recognition is a divine testament to the scripture that anchors the institution — <em>Isaiah 8:18</em>: "Behold, I and the children whom the Lord hath given me are for signs and wonders."
          </p>
          <blockquote class="border-l-4 border-brand-gold bg-amber-50/60 p-4 rounded-r-xl italic text-gray-800 my-4 text-sm font-medium">
            "Our Latin creed, <strong>Per Angusta Ad Augusta</strong> (Through Difficulties to Greatness), represents the mental resilience we instill into every child. We do not believe in academic shortcuts or false facades; our fully equipped chemistry, physics, and biology laboratories allow students to test, discover, and own their knowledge."
          </blockquote>
          <h4 class="text-lg font-headline font-black text-brand-forest mt-4 mb-2">Student Spotlights</h4>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            Special commendations were presented to senior science scholars including <strong>Farouq Adeyemi (SS2 Science)</strong> and his peers whose innovative robotics and experimental submissions earned top ranks among competing secondary schools across Osun State and the South-West region.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            The Olive Branches Schools continues to pave the way in combining rigorous academic standards, Godly moral character, and hands-on technological literacy. Admissions for the 2026/2027 academic session are currently open across the Pre-School, Junior School, Middle School, and High School wings.
          </p>
        `
      },
      london_tour: {
        title: "Experiential Learning Beyond Borders: The United Nations Club & London Educational Excursion",
        category: "International Excursion",
        date: "January 18, 2026",
        readTime: "4 min read",
        author: "Directorate of Student Affairs & Global Programs",
        image: "images/crops/excursion_trafalgar_square.jpg",
        content: `
          <p class="text-base text-gray-700 leading-relaxed mb-4">
            True education does not terminate at classroom walls. At The Olive Branches Schools, our scholars are groomed to become critically conscious global citizens who appreciate both their rich African heritage and modern international developments.
          </p>
          <h4 class="text-lg font-headline font-black text-brand-forest mt-4 mb-2">From Osun-Osogbo Sacred Grove to Trafalgar Square</h4>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            During the term, the school's United Nations Club embarked on a multi-phase educational exploration. The first leg focused on local cultural conservation with an immersive research expedition to the <strong>Osun-Osogbo Sacred Grove</strong> — a UNESCO World Heritage Site in our hometown of Osogbo. Scholars documented indigenous plant biodiversity, traditional Yoruba architecture, and ecological preservation.
          </p>
          <blockquote class="border-l-4 border-brand-forest bg-green-50/60 p-4 rounded-r-xl italic text-gray-800 my-4 text-sm font-medium">
            "Watching our students examine historical artifacts at the British Museum and stand at the Prime Meridian line in Greenwich after studying the Osun Grove was breathtaking. They realize that they belong on the world stage."
          </blockquote>
          <h4 class="text-lg font-headline font-black text-brand-forest mt-4 mb-2">Highlights of the London Tour</h4>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            The international cohort explored iconic global landmarks including <strong>Trafalgar Square</strong>, the London Eye, the Science Museum, and the Houses of Parliament. Students engaged in structured debate sessions and interactive science workshops alongside international peers.
          </p>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            These international and domestic excursions are integrated annually into our curriculum, ensuring that Olive Branches scholars graduate with a truly global perspective.
          </p>
        `
      },
      sparkle_nite: {
        title: "Annual Sparkle Nite Gala: A Dazzling Celebration of Performing Arts, Ballet & Public Speaking",
        category: "Arts & Campus Culture",
        date: "December 14, 2025",
        readTime: "3 min read",
        author: "Department of Creative Arts & Languages",
        image: "images/crops/gallery_sparkle_nite.jpg",
        content: `
          <p class="text-base text-gray-700 leading-relaxed mb-4">
            The campus auditorium erupted in applause as scholars from the Pre-School up to the High School presented the 2025 edition of our flagship cultural and stage showcase: <strong>Sparkle Nite</strong>.
          </p>
          <h4 class="text-lg font-headline font-black text-brand-forest mt-4 mb-2">Multifaceted Talents on Display</h4>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            Dressed in vibrant tutus, formal blazers, and traditional cultural attires, our young performers mesmerized parents and guests with classical ballet routines, choral anthems rendered harmoniously in English, Yoruba, and French, and a dramatic stage adaptation highlighting leadership, faith, and honesty.
          </p>
          <blockquote class="border-l-4 border-brand-leaf bg-emerald-50/60 p-4 rounded-r-xl italic text-gray-800 my-4 text-sm font-medium">
            "Sparkle Nite gives every child a voice. When a six-year-old steps onto a stage with confidence, or an SS3 student recites French poetry fluently before hundreds of parents, that is transformative character molding."
          </blockquote>
          <h4 class="text-lg font-headline font-black text-brand-forest mt-4 mb-2">Oratory & Musical Orchestration</h4>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            The school orchestra showcased violin and brass performances, followed by public speaking presentations addressing modern scientific and ethical issues. The night concluded with the uplifting rendition of the <strong>School Creed</strong>: <em>"I am a planting of The Lord, Rooted and grounded in the Rock... Whatever I do shall prosper!"</em>
          </p>
        `
      }
    };

    let activeArticleKey = 'congratulations';

    function openArticleModal(key) {
      const article = articlesDatabase[key];
      if (!article) return;
      activeArticleKey = key;

      document.getElementById('modal-article-title').innerText = article.title;
      document.getElementById('modal-article-cat').innerText = article.category;
      document.getElementById('modal-article-date').innerHTML = `<i data-lucide="calendar" class="w-3.5 h-3.5"></i><span>${article.date}</span>`;
      document.getElementById('modal-article-readtime').innerText = article.readTime;
      document.getElementById('modal-article-author').innerHTML = `<i data-lucide="user" class="w-3.5 h-3.5"></i><span>${article.author}</span>`;
      document.getElementById('modal-article-img').src = article.image;
      document.getElementById('modal-article-body').innerHTML = article.content;

      const modal = document.getElementById('article-reader-modal');
      modal.classList.remove('hidden');
      if (window.lucide) lucide.createIcons();
    }

    function closeArticleModal() {
      document.getElementById('article-reader-modal').classList.add('hidden');
    }

    function shareArticleWhatsApp() {
      const article = articlesDatabase[activeArticleKey];
      const text = `*${encodeURIComponent(article.title)}*%0A${encodeURIComponent(window.location.href)}`;
      window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
    }\n\n"""

# Insert JS before </script>
html = html.replace("    function openVideoPlayer() {", article_js + "    function openVideoPlayer() {")

with open(r"C:\Users\giant\.gemini\antigravity\scratch\school-portal-os\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved index.html with interactive Article Reader Modal!")
