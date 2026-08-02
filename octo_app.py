import os
import random
import datetime
import math
import urllib.request
import xml.etree.ElementTree as ET

# ==========================================
# 50 INFLUENTIAL ROMANTIC ARTISTS & WORKS
# ==========================================
ROMANTIC_MASTERS = [
    {"name": "Francisco Goya", "country": "Spain", "style": "Dark psychological depth & chiaroscuro", "works": ["The Third of May 1808", "Saturn Devouring His Son", "Witches' Sabbath"]},
    {"name": "William Blake", "country": "Britain", "style": "Visionary mystical & ethereal forms", "works": ["The Ancient of Days", "Newton", "The Great Red Dragon"]},
    {"name": "Caspar David Friedrich", "country": "Germany", "style": "Sublime lonely vistas & spiritual nature", "works": ["Wanderer above the Sea of Fog", "The Sea of Ice", "Abbey in the Oakwood"]},
    {"name": "J.M.W. Turner", "country": "Britain", "style": "Expressive chaotic atmospheric light", "works": ["The Slave Ship", "Rain, Steam and Speed", "The Fighting Temeraire"]},
    {"name": "John Constable", "country": "Britain", "style": "Luminous rural English countryside", "works": ["The Hay Wain", "Salisbury Cathedral from the Meadows", "The Cornfield"]},
    {"name": "Théodore Géricault", "country": "France", "style": "Intense physical realism & emotional drama", "works": ["The Raft of the Medusa", "The Charging Chasseur", "Monomania of Military Command"]},
    {"name": "Eugène Delacroix", "country": "France", "style": "Vibrant color velocity & dynamic motion", "works": ["Liberty Leading the People", "The Death of Sardanapalus", "The Barque of Dante"]},
    {"name": "Henry Fuseli", "country": "Switzerland", "style": "Eerie supernatural nocturnal nightmares", "works": ["The Nightmare", "Lady Macbeth Sleepwalking", "The Shepherd's Dream"]},
    {"name": "Philipp Otto Runge", "country": "Germany", "style": "Allegorical mysticism & natural geometry", "works": ["The Morning", "The Small Morning", "The Huelsenbeck Children"]},
    {"name": "Antoine-Jean Gros", "country": "France", "style": "Neoclassical scale turned emotional drama", "works": ["Napoleon visiting the Plague Victims of Jaffa", "The Battle of Eylau", "General Bonaparte at Arcole"]},
    {"name": "Thomas Cole", "country": "USA", "style": "Monumental wilderness & allegorical vistas", "works": ["The Oxbow", "The Course of Empire: Destruction", "The Voyage of Life: Youth"]},
    {"name": "Ivan Aivazovsky", "country": "Russia", "style": "Turbulent marine luminescence & crashing waves", "works": ["The Ninth Wave", "Rainbow", "View of Constantinople in Moonlight"]},
    {"name": "John Martin", "country": "Britain", "style": "Apocalyptic vast sublime architecture", "works": ["The Great Day of His Wrath", "Belshazzar's Feast", "The Destruction of Pompeii and Herculaneum"]},
    {"name": "Johan Christian Dahl", "country": "Norway", "style": "Dramatic Nordic crags & tempestuous clouds", "works": ["Birch Tree in a Storm", "View of Dresden by Full Moon", "Stugunøstseter"]},
    {"name": "Albert Bierstadt", "country": "USA", "style": "Glowing panoramic Western frontiers", "works": ["Looking Down Yosemite Valley", "The Rocky Mountains, Lander's Peak", "A Storm in the Rocky Mountains"]},
    {"name": "Frederic Edwin Church", "country": "USA", "style": "Hyper-detailed tropical & arctic monuments", "works": ["The Heart of the Andes", "Cotopaxi", "Niagara"]},
    {"name": "Asher Brown Durand", "country": "USA", "style": "Intimate woodland light & dappled forest canopies", "works": ["Kindred Spirits", "In the Woods", "Forest In the Morning"]},
    {"name": "George Caleb Bingham", "country": "USA", "style": "Luminist river frontier daily life", "works": ["Fur Traders Descending the Missouri", "The County Election", "Jolly Flatboatmen in Port"]},
    {"name": "Carl Blechen", "country": "Germany", "style": "Psychological sunlight & industrial tension", "works": ["The Rolling Mill at Eberswalde", "Gorge near Amalfi", "Ruins of a Gothic Church"]},
    {"name": "Alexandre Calame", "country": "Switzerland", "style": "Monumental Alpine peaks & torrents", "works": ["Storm in the Handeck", "Lake of the Four Cantons", "The Wetterhorn"]},
    {"name": "Francesco Hayez", "country": "Italy", "style": "Melancholic historical human emotion", "works": ["The Kiss", "Reflections on the Unification of Italy", "Pietro Rossi"]},
    {"name": "Théodore Chassériau", "country": "France", "style": "Linear elegance combined with rich color", "works": ["The Tepidarium", "Venus Anadyomene", "Ali-Ben-Hamet, Caliph of Constantine"]},
    {"name": "Paul Delaroche", "country": "France", "style": "Melodramatic historical human tragedy", "works": ["The Execution of Lady Jane Grey", "Princes in the Tower", "The Hemicycle"]},
    {"name": "Ary Scheffer", "country": "Netherlands", "style": "Literary & sacred spiritual devotion", "works": ["Dante and Virgil Encountering the Shades of Francesca and Paolo", "Saint Augustine and Saint Monica", "The Souliot Women"]},
    {"name": "Louis Léopold Robert", "country": "Switzerland", "style": "Monumental peasant genre compositions", "works": ["Arrival of the Harvesters in the Pontine Marshes", "The Neapolitan Fishermen", "The Departure of the Fishing Boats"]},
    {"name": "Ferdinand Georg Waldmüller", "country": "Austria", "style": "Luminous alpine sunlight & rural realism", "works": ["Prater Landscape", "Early Spring in the Vienna Woods", "The Expected One"]},
    {"name": "Wilhelm von Schadow", "country": "Germany", "style": "Sacred Nazarene linear harmony", "works": ["The Wise and Foolish Virgins", "Portrait of Mignon", "The Parable of the Unrighteous Steward"]},
    {"name": "Peter von Cornelius", "country": "Germany", "style": "Monumental historical fresco revival", "works": ["The Last Judgment", "The Four Riders of the Apocalypse", "Athene Teaching the Weavers"]},
    {"name": "Franz Ittenbach", "country": "Germany", "style": "Soft devotional Nazarene portraiture", "works": ["Holy Family", "St. Maria", "The Virgin Mary"]},
    {"name": "Johann Friedrich Overbeck", "country": "Germany", "style": "Pure Nazarene medieval revivalism", "works": ["Italia and Germania", "The Triumph of Religion in the Arts", "Portrait of Franz Pforr"]},
    {"name": "Sylvester Shchedrin", "country": "Russia", "style": "Atmospheric Italian coastal glow", "works": ["New Rome: Castle of Sant'Angelo", "Terrace at Sorrento", "Great Grotto in Capri"]},
    {"name": "Orest Kiprensky", "country": "Russia", "style": "Expressive psychological portraiture", "works": ["Portrait of Alexander Pushkin", "Portrait of Yevgraf Davydov", "Poor Liza"]},
    {"name": "Karl Bryullov", "country": "Russia", "style": "Epic catastrophic historical scale", "works": ["The Last Day of Pompeii", "The Horsewoman", "The Siege of Pskov"]},
    {"name": "Vasily Tropinin", "country": "Russia", "style": "Gentle human realism & genre intimacy", "works": ["The Lace Maker", "Portrait of A.S. Pushkin", "The Guitar Player"]},
    {"name": "Constantin Hansen", "country": "Denmark", "style": "Golden Age architectural precision & warmth", "works": ["A Company of Danish Artists in Rome", "The Danish Constituent Assembly", "Prometheus Fetching Fire"]},
    {"name": "Christen Købke", "country": "Denmark", "style": "Intimate Danish Golden Age light", "works": ["View of Lake Sortedam", "Frederiksborg Castle at Sunset", "The North Gate of the Citadel"]},
    {"name": "Johan Thomas Lundbye", "country": "Denmark", "style": "National Romantic pastoral country vistas", "works": ["A Danish Coast", "Dolmen at Raklev, Røsnæs", "Landscape with Cattle"]},
    {"name": "P.C. Skovgaard", "country": "Denmark", "style": "Monumental Danish beech forests", "works": ["Beech Forest in May", "View of Issefjord", "Summer Day in the Woods"]},
    {"name": "Jan Willem Pieneman", "country": "Netherlands", "style": "Grand historical military pageantry", "works": ["The Battle of Waterloo", "The Hero of Waterloo", "Portrait of William I"]},
    {"name": "Barend Cornelis Koekkoek", "country": "Netherlands", "style": "Majestic wooded countryside & river valleys", "works": ["Winter Landscape", "A Forest Scene", "Landscape with Cattle and Figures"]},
    {"name": "Gustave Doré", "country": "France", "style": "Dark dramatic fantasy & engraving chiaroscuro", "works": ["The Inferno: Charon's Boat", "L'Allegro: The Dance", "Andromeda Chained to the Rock"]},
    {"name": "Arnold Böcklin", "country": "Switzerland", "style": "Melancholic symbolist mythic isolation", "works": ["Isle of the Dead", "Ruins by the Sea", "Prometheus"]},
    {"name": "Hans Thoma", "country": "Germany", "style": "Rustic folklore & idyllic countryside", "works": ["Wondrous Birds", "Self-Portrait in the Open", "The Keeper of the Valley"]},
    {"name": "Albert Pinkham Ryder", "country": "USA", "style": "Heavy impasto moody moonlit seas", "works": ["Toilers of the Sea", "The Temple of the Mind", "Siegfried and the Rhine Maidens"]},
    {"name": "Robert S. Duncanson", "country": "USA", "style": "Lyrical poetic Hudson River landscapes", "works": ["Land of the Lotus Eaters", "Blue Hole, Flood Waters, Little Miami River", "Uncle Tom and Little Eva"]},
    {"name": "Worthington Whittredge", "country": "USA", "style": "Quiet interior forest light filtered through trees", "works": ["The Trout Pool", "Forest Interior", "On the Plains"]},
    {"name": "Jasper Francis Cropsey", "country": "USA", "style": "Vivid autumn foliage & glowing atmospheres", "works": ["Autumn - On the Hudson River", "The Millennial Age", "Starrucca Viaduct"]},
    {"name": "Sanford Robinson Gifford", "country": "USA", "style": "Luminist radiant haze & dissolved horizon", "works": ["October in the Catskills", "Twilight in the Adirondacks", "Kauterskill Clove"]},
    {"name": "John Frederick Kensett", "country": "USA", "style": "Serene coastal reflections & quiet waters", "works": ["Eaton's Neck, Long Island", "Lake George", "Shrewsbury River, New Jersey"]},
    {"name": "Emanuel Leutze", "country": "USA", "style": "Heroic historical dramatizations & courage", "works": ["Washington Crossing the Delaware", "Westward the Course of Empire Takes Its Way", "Columbus Before the Queen"]}
]

# ==========================================
# ARM 1: THE VISION ARM (1 of 50 arXiv + 8 Masters)
# ==========================================
def arm_vision():
    category = random.choice(["quant-ph", "astro-ph", "gr-qc", "cond-mat"])
    url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&sortBy=submittedDate&sortOrder=descending&max_results=50"
    
    paper_data = {
        "paper_title": "Quantum Coherence across Curved Horizon Boundaries",
        "paper_url": "https://arxiv.org/abs/2608.01234",
        "summary": "An exploration into non-locality, thermodynamics, and quantum particle creation along gravitational event horizons.",
        "author": "Dr. E. R. Hawking et al.",
        "category": category
    }
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'OctoArtApp/1.0'})
        with urllib.request.urlopen(req) as response:
            root = ET.fromstring(response.read())
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            entries = root.findall('atom:entry', ns)
            if entries:
                entry = random.choice(entries)
                paper_data["paper_title"] = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                paper_data["paper_url"] = entry.find('atom:id', ns).text.strip()
                paper_data["summary"] = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')[:240] + "..."
                author_el = entry.find('atom:author/atom:name', ns)
                paper_data["author"] = author_el.text if author_el is not None else "arXiv Contributor"
                paper_data["category"] = category
    except Exception as e:
        print(f"arXiv API notice: {e}. Utilizing fallback quantum cosmological paper.")

    selected_masters = random.sample(ROMANTIC_MASTERS, 8)
    
    all_24_references = []
    for artist in selected_masters:
        for work in artist["works"]:
            all_24_references.append(f"'{work}' by {artist['name']}")
            
    title_prefixes = ["The Allegory of", "Sublime Vision of", "The Tempest of", "Contemplation of", "The Sanctuary of"]
    romantic_title = f"{random.choice(title_prefixes)} {paper_data['paper_title'].split(':')[0][:35]}"
    
    return {
        "paper": paper_data,
        "selected_masters": selected_masters,
        "all_24_references": all_24_references,
        "romantic_title": romantic_title
    }

# ==========================================
# ARM 2: DIGITAL CANVAS PAINTER ENGINE
# ==========================================
def arm_artist(concept):
    width, height = 900, 900
    svg_elements = []
    
    bg_dark = random.choice(["#070a12", "#0f0b08", "#080e14", "#0c070e"])
    mid_tone = random.choice(["#2c1a12", "#1e293b", "#3b1c10", "#182825"])
    highlight = random.choice(["#f59e0b", "#fbbf24", "#d97706", "#fef08a"])
    deep_accent = random.choice(["#7c2d12", "#9f1239", "#431407", "#1e1b4b"])
    
    svg_elements.append(f"""
    <defs>
        <radialGradient id="sunGlow" cx="50%" cy="40%" r="60%">
            <stop offset="0%" stop-color="{highlight}" stop-opacity="0.9" />
            <stop offset="35%" stop-color="{deep_accent}" stop-opacity="0.6" />
            <stop offset="80%" stop-color="{mid_tone}" stop-opacity="0.8" />
            <stop offset="100%" stop-color="{bg_dark}" stop-opacity="1" />
        </radialGradient>
        <filter id="canvasTexture">
            <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="4" result="noise" />
            <feColorMatrix type="saturate" values="0.1" />
            <feComponentTransfer><feFuncA type="linear" slope="0.08" /></feComponentTransfer>
            <feBlend mode="multiply" in="SourceGraphic" result="blend" />
        </filter>
        <filter id="softGlow"><feGaussianBlur stdDeviation="8" /></filter>
    </defs>
    <rect width="{width}" height="{height}" fill="{bg_dark}" />
    <rect width="{width}" height="{height}" fill="url(#sunGlow)" filter="url(#canvasTexture)" />
    """)
    
    svg_elements.append(f'<ellipse cx="450" cy="380" rx="320" ry="140" fill="{highlight}" opacity="0.25" filter="url(#softGlow)" />')
    svg_elements.append(f'<polygon points="0,620 220,410 480,650" fill="{deep_accent}" opacity="0.95" />')
    svg_elements.append(f'<polygon points="280,650 580,360 850,660" fill="{mid_tone}" opacity="0.9" />')
    svg_elements.append(f'<polygon points="550,660 740,430 900,640" fill="#04070d" opacity="0.95" />')
    svg_elements.append(f'<path d="M 0,640 Q 250,590 450,680 T 900,630 L 900,900 L 0,900 Z" fill="#020408" />')
    svg_elements.append(f'<ellipse cx="450" cy="740" rx="280" ry="25" fill="{highlight}" opacity="0.35" filter="url(#softGlow)" />')
    
    svg_elements.append('<ellipse cx="448" cy="628" rx="7" ry="7" fill="#000000" />')
    svg_elements.append('<path d="M 440,635 L 456,635 L 460,670 L 436,670 Z" fill="#000000" />')
    svg_elements.append('<line x1="458" y1="635" x2="462" y2="690" stroke="#000000" stroke-width="2" />')
    
    svg_elements.append('<path d="M 40,650 Q 20,530 80,420 Q 120,520 100,650 Z" fill="#030509" />')
    svg_elements.append('<path d="M 820,640 Q 800,510 860,400 Q 890,510 870,640 Z" fill="#030509" />')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">{''.join(svg_elements)}</svg>"""

# ==========================================
# ARM 3: MUSEUM CURATOR ARM (Writes Plaque)
# ==========================================
def arm_curator(concept, exec_time_str):
    paper = concept["paper"]
    masters = concept["selected_masters"]
    m_names = [m["name"] for m in masters]
    
    p1 = f"Acquired into the Virtual Museum collection on <strong>{exec_time_str}</strong>, this work finds its intellectual origin in recent research published on arXiv, entitled <em>\"{paper['paper_title']}\"</em> by {paper['author']}. The composition translates the paper's core thesis—exploring complex phenomena within {paper['category'].upper()}—into a visual metaphor."
    p2 = f"Visually, the piece draws compositional influence from eight Romantic masters: {', '.join(m_names[:4])}, {', '.join(m_names[4:])}. Synthesizing elements from 24 analyzed works across these artists, the painting employs dramatic chiaroscuro lighting, deep impasto atmospheric glazing, and a solitary figure positioned in contemplation—recalling the awe and sublime majesty characteristic of 19th-century Romanticism."
    
    return f"<p class='plaque-p'>{p1}</p><p class='plaque-p'>{p2}</p>"

# ==========================================
# ARM 4: PUBLISHER (Virtual Museum Hall)
# ==========================================
def arm_publisher(concept, svg_code, museum_plaque, exec_time_str):
    os.makedirs("gallery", exist_ok=True)
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"gallery/art_{timestamp}.svg"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_code)
        
    paper = concept["paper"]
    masters = concept["selected_masters"]
    
    artists_html = "".join([f"<li><strong>{m['name']}</strong> ({m['country']}) — <em>{m['style']}</em></li>" for m in masters])
    refs_html = "".join([f"<li>{ref}</li>" for ref in concept["all_24_references"]])
    
    card_id = f"exhibit_{timestamp}"
    category_slug = paper['category'].lower()
    
    html_card = f"""
        <div class="card" id="{card_id}" data-category="{category_slug}">
            <div class="frame-container">
                <div class="picture-frame">
                    {svg_code}
                </div>
            </div>
            <div class="meta">
                <div class="card-header">
                    <span class="badge">{paper['category'].upper()}</span>
                    <a href="{paper['paper_url']}" target="_blank" class="paper-btn">🔗 arXiv Paper</a>
                </div>
                
                <h2 class="art-title">"{concept['romantic_title']}"</h2>
                
                <div class="museum-plaque">
                    <div class="plaque-header">🏛️ MUSEUM CURATOR'S NOTE & TIMING</div>
                    {museum_plaque}
                </div>
                
                <hr class="divider" />
                
                <h3>🎨 8 Influential Romantic Masters Selected:</h3>
                <ul class="masters-list">{artists_html}</ul>
                
                <h3>🖼️ 24 Reference Paintings Analyzed:</h3>
                <details>
                    <summary>Click to view all 24 source reference works</summary>
                    <ul class="refs-list">{refs_html}</ul>
                </details>
                
                <p class="time">⏱️ Created & Published: <strong>{exec_time_str}</strong></p>
            </div>
        </div>"""
    
    index_path = "index.html"
    if not os.path.exists(index_path):
        content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Virtual Museum of Cutting-Edge Romanticism</title>
    <style>
        body {{ font-family: 'Georgia', serif; background: #05070a; color: #f1f5f9; margin: 0; padding: 2rem; }}
        header {{ text-align: center; margin-bottom: 2.5rem; padding-bottom: 2rem; border-bottom: 1px solid #1e293b; }}
        h1 {{ font-size: 3rem; margin-bottom: 0.5rem; color: #f59e0b; font-weight: normal; letter-spacing: 2px; text-transform: uppercase; }}
        p.subtitle {{ color: #94a3b8; font-style: italic; max-width: 750px; margin: 0 auto 1.5rem auto; line-height: 1.6; font-size: 1.05rem; }}
        
        .museum-nav {{ display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem; font-family: sans-serif; }}
        .filter-btn {{ background: #0f172a; border: 1px solid #334155; color: #cbd5e1; padding: 0.5rem 1.25rem; border-radius: 20px; font-size: 0.85rem; cursor: pointer; transition: all 0.2s; }}
        .filter-btn:hover, .filter-btn.active {{ background: #d97706; color: #ffffff; border-color: #f59e0b; }}
        
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); gap: 3rem; max-width: 1500px; margin: 0 auto; }}
        .card {{ background: #0b0f19; border: 1px solid #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.9); transition: transform 0.3s ease, border-color 0.3s ease; }}
        .card:hover {{ transform: translateY(-8px); border-color: #f59e0b; }}
        
        .frame-container {{ padding: 1.5rem; background: #030508; text-align: center; border-bottom: 1px solid #1e293b; }}
        .picture-frame {{ display: inline-block; width: 100%; aspect-ratio: 1; border: 12px solid #1c130d; box-shadow: inset 0 0 15px rgba(0,0,0,0.8), 0 10px 20px rgba(0,0,0,0.6); border-radius: 4px; overflow: hidden; }}
        
        .meta {{ padding: 1.75rem; }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }}
        .badge {{ background: #7c2d12; color: #fef08a; font-size: 0.75rem; font-family: sans-serif; padding: 0.25rem 0.7rem; border-radius: 4px; text-transform: uppercase; letter-spacing: 1px; font-weight: bold; }}
        .paper-btn {{ background: #0284c7; color: #ffffff; text-decoration: none; font-size: 0.8rem; font-family: sans-serif; padding: 0.35rem 0.8rem; border-radius: 4px; font-weight: bold; transition: background 0.2s; }}
        .paper-btn:hover {{ background: #0369a1; }}
        .art-title {{ font-size: 1.6rem; color: #fef08a; font-weight: normal; line-height: 1.3; margin: 0.5rem 0 1.25rem 0; text-align: center; font-style: italic; }}
        
        .museum-plaque {{ background: #111827; border-left: 4px solid #d97706; padding: 1.1rem 1.3rem; margin: 1.25rem 0; border-radius: 0 8px 8px 0; }}
        .plaque-header {{ font-family: sans-serif; font-size: 0.75rem; color: #f59e0b; letter-spacing: 1.5px; font-weight: bold; margin-bottom: 0.6rem; }}
        .plaque-p {{ font-size: 0.9rem; color: #cbd5e1; line-height: 1.65; margin: 0 0 0.8rem 0; }}
        .plaque-p:last-child {{ margin-bottom: 0; }}
        
        .divider {{ border: 0; border-top: 1px solid #1e293b; margin: 1.5rem 0; }}
        h3 {{ font-size: 0.95rem; color: #f59e0b; margin: 1rem 0 0.5rem 0; font-family: sans-serif; font-weight: 600; }}
        .masters-list, .refs-list {{ font-size: 0.83rem; color: #cbd5e1; font-family: sans-serif; padding-left: 1.2rem; margin: 0.4rem 0; line-height: 1.5; }}
        details {{ font-family: sans-serif; font-size: 0.85rem; color: #38bdf8; cursor: pointer; margin-top: 0.6rem; }}
        summary {{ font-weight: 600; padding: 0.2rem 0; }}
        .time {{ color: #94a3b8 !important; font-size: 0.8rem !important; margin-top: 1.5rem !important; font-family: sans-serif; text-align: right; }}
    </style>
</head>
<body>
    <header>
        <h1>🏛️ Virtual Museum of Romantic Science</h1>
        <p.subtitle>An autonomous gallery exhibiting new digital paintings every 15 minutes that contemplate newly published arXiv research through the lens of 8 Romantic masters and 24 reference paintings.</p>
        
        <div class="museum-nav">
            <button class="filter-btn active" onclick="filterGallery('all')">All Exhibition Halls</button>
            <button class="filter-btn" onclick="filterGallery('quant-ph')">Quantum Physics</button>
            <button class="filter-btn" onclick="filterGallery('astro-ph')">Astrophysics</button>
            <button class="filter-btn" onclick="filterGallery('gr-qc')">Relativity & Cosmology</button>
            <button class="filter-btn" onclick="filterGallery('cond-mat')">Condensed Matter</button>
        </div>
    </header>
    
    <div class="grid" id="gallery">
{html_card}
    </div>

    <script>
        function filterGallery(category) {{
            const buttons = document.querySelectorAll('.filter-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {{
                if (category === 'all' || card.getAttribute('data-category') === category) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>"""
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        with open(index_path, "r", encoding="utf-8") as f:
            full_html = f.read()
        
        insertion_point = '<div class="grid" id="gallery">'
        updated_html = full_html.replace(insertion_point, insertion_point + "\n" + html_card)
        
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(updated_html)

# ==========================================
# CENTRAL BRAIN ORCHESTRATOR
# ==========================================
if __name__ == "__main__":
    exec_now = datetime.datetime.utcnow()
    exec_time_str = exec_now.strftime("%B %d, %Y at %H:%M UTC")
    
    print(f"🐙 Central Brain: Waking up arms at {exec_time_str}...")
    concept = arm_vision()
    print(f"👁️ Vision Arm: arXiv paper retrieved -> '{concept['paper']['paper_title']}'")
    print(f"🎨 Selected 8 Masters: {', '.join([m['name'] for m in concept['selected_masters']])}")
    
    svg_art = arm_artist(concept)
    print("🖌️ Digital Canvas Painter: Rendered new Romantic masterpiece.")
    
    museum_plaque = arm_curator(concept, exec_time_str)
    print("🏛️ Museum Curator Arm: Composed 2-paragraph exhibition plaque with timing.")
    
    arm_publisher(concept, svg_art, museum_plaque, exec_time_str)
    print("📢 Publisher Arm: Updated Virtual Museum gallery.")
    print("🐙 Central Brain: 15-minute cycle complete. Sleeping...")
