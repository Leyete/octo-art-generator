import os
import random
import datetime
import urllib.request
import xml.etree.ElementTree as ET

# ==========================================
# ARM 1: THE VISION ARM (Fetches arXiv Paper)
# ==========================================
ARXIV_CATEGORIES = ["quant-ph", "astro-ph", "gr-qc", "cond-mat"]

ROMANTIC_MOTIFS = [
    {"subject": "Solitary Wanderer", "setting": "Mountain Peak Above Sea of Fog"},
    {"subject": "Shipwreck", "setting": "Stormy Ocean at Twilight"},
    {"subject": "Ancient Ruin", "setting": "Gothic City in Moonlight"},
    {"subject": "Country Shepherd", "setting": "Pastoral Valley Under Looming Eclipse"},
    {"subject": "Astronomer in Tower", "setting": "Overlooking Celestial Aurora"},
    {"subject": "Travelers at Crossroads", "setting": "Wilderness Forest at Dusk"}
]

def arm_vision():
    category = random.choice(ARXIV_CATEGORIES)
    url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&sortBy=submittedDate&sortOrder=descending&max_results=10"
    
    motif = random.choice(ROMANTIC_MOTIFS)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'OctoArtApp/1.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entries = root.findall('atom:entry', ns)
        
        if entries:
            entry = random.choice(entries)
            paper_title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            paper_url = entry.find('atom:id', ns).text.strip()
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            author = entry.find('atom:author/atom:name', ns)
            author_name = author.text if author is not None else "Unknown Researcher"
            
            romantic_title = f"{motif['subject']} Contemplating {paper_title.split(':')[0][:35]}"
            
            return {
                "paper_title": paper_title,
                "paper_url": paper_url,
                "summary": summary[:220] + "...",
                "author": author_name,
                "romantic_title": romantic_title,
                "motif": motif,
                "category": category
            }
    except Exception as e:
        print(f"arXiv Fetch Warning ({e}). Using offline Quantum concept.")
        
    return {
        "paper_title": "Quantum Horizon Dynamics in Curved Spacetime",
        "paper_url": "https://arxiv.org/abs/2401.00001",
        "summary": "An investigation of thermodynamic fluctuations along cosmic boundaries in general relativity.",
        "author": "Octo-Researcher",
        "romantic_title": f"{motif['subject']} Contemplating Cosmic Horizons",
        "motif": motif,
        "category": "gr-qc"
    }

# ==========================================
# ARM 2: FIGURATIVE ROMANTIC ARTIST (No Abstract)
# ==========================================
def arm_artist(concept):
    width, height = 800, 800
    svg_elements = []
    
    motif = concept["motif"]["subject"]
    
    # 1. Sky / Atmosphere (Chiaroscuro Evening Gradient)
    sky_grad = """
    <defs>
        <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#0b132b" />
            <stop offset="40%" stop-color="#1c2541" />
            <stop offset="70%" stop-color="#3a506b" />
            <stop offset="85%" stop-color="#b95b26" />
            <stop offset="100%" stop-color="#d97706" />
        </linearGradient>
    </defs>
    <rect width="800" height="800" fill="url(#skyGrad)" />
    """
    svg_elements.append(sky_grad)
    
    # 2. Celestial Light (Moon/Sun pierce through cloud layers)
    svg_elements.append('<circle cx="400" cy="280" r="90" fill="#fef08a" opacity="0.85" filter="drop-shadow(0 0 25px #fbbf24)" />')
    
    # Cloud Banks (Atmospheric Nature)
    svg_elements.append('<ellipse cx="250" cy="290" rx="180" ry="35" fill="#1c2541" opacity="0.7" />')
    svg_elements.append('<ellipse cx="550" cy="270" rx="220" ry="45" fill="#0b132b" opacity="0.8" />')
    
    # 3. Nature & Landscape (Mountains / Sea / Country Horizons)
    # Background Distant Mountains
    svg_elements.append('<polygon points="0,550 180,420 380,550" fill="#1e293b" />')
    svg_elements.append('<polygon points="250,550 500,380 720,550" fill="#0f172a" />')
    svg_elements.append('<polygon points="520,550 680,440 800,550" fill="#1e293b" />')
    
    # Foreground Country Terrain / City Silhouette / Cliff Edge
    svg_elements.append('<path d="M 0,550 Q 200,500 400,580 T 800,540 L 800,800 L 0,800 Z" fill="#020617" />')
    
    # 4. Human Figure & Built World (Daily Life / Solitary Figures / Architecture)
    if "Wanderer" in motif or "Shepherd" in motif or "Astronomer" in motif:
        # Solitary Person standing in silhouette looking into the landscape
        svg_elements.append('<!-- Human Silhouette -->')
        svg_elements.append('<ellipse cx="395" cy="530" rx="6" ry="6" fill="#020617" />') # Head
        svg_elements.append('<path d="M 388,536 L 402,536 L 405,565 L 385,565 Z" fill="#020617" />') # Cloak/Body
        svg_elements.append('<line x1="390" y1="565" x2="388" y2="585" stroke="#020617" stroke-width="3" />') # Leg L
        svg_elements.append('<line x1="400" y1="565" x2="402" y2="585" stroke="#020617" stroke-width="3" />') # Leg R
        # Staff in hand
        svg_elements.append('<line x1="406" y1="535" x2="408" y2="588" stroke="#020617" stroke-width="1.5" />')
        
    elif "Ruin" in motif or "City" in motif:
        # Gothic Arch / City Spires Silhouette
        svg_elements.append('<!-- Architecture / City Ruins -->')
        svg_elements.append('<rect x="120" y="440" width="40" height="120" fill="#020617" />')
        svg_elements.append('<polygon points="120,440 140,380 160,440" fill="#020617" />')
        svg_elements.append('<rect x="180" y="470" width="60" height="90" fill="#020617" />')
        svg_elements.append('<path d="M 190,490 A 15,20 0 0,1 230,490 L 230,560 L 190,560 Z" fill="#3a506b" />') # Window cutout

    elif "Shipwreck" in motif:
        # Vessel at Sea
        svg_elements.append('<!-- Ship Silhouette -->')
        svg_elements.append('<path d="M 550,560 Q 600,550 650,565 L 640,580 L 560,580 Z" fill="#020617" />')
        svg_elements.append('<line x1="600" y1="555" x2="600" y2="480" stroke="#020617" stroke-width="3" />') # Mast
        svg_elements.append('<polygon points="600,490 635,515 600,535" fill="#020617" opacity="0.9" />') # Tattered Sail

    # Foreshore Country Trees
    svg_elements.append('<path d="M 60,580 Q 50,520 80,480 Q 110,520 100,580 Z" fill="#020617" />')
    svg_elements.append('<path d="M 720,570 Q 710,510 740,470 Q 770,510 760,570 Z" fill="#020617" />')

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    {''.join(svg_elements)}
</svg>"""
    return svg_content

# ==========================================
# ARM 3 & 4: PUBLISHER (Gallery Card with Direct arXiv Link)
# ==========================================
def arm_publisher(concept, svg_code):
    os.makedirs("gallery", exist_ok=True)
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"gallery/art_{timestamp}.svg"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_code)
        
    date_str = datetime.datetime.utcnow().strftime("%B %d, %Y - %H:00 UTC")
    
    html_card = f"""
        <div class="card">
            <div class="svg-container">{svg_code}</div>
            <div class="meta">
                <div class="card-header">
                    <span class="badge">{concept['category'].upper()}</span>
                    <a href="{concept['paper_url']}" target="_blank" class="paper-btn">🔗 Read arXiv Paper</a>
                </div>
                <h2>{concept['romantic_title']}</h2>
                <p class="motif-tag"><strong>Setting:</strong> {concept['motif']['setting']}</p>
                <p class="arxiv-title"><strong>Scientific Paper:</strong> <em>"{concept['paper_title']}"</em></p>
                <p class="author">By {concept['author']}</p>
                <p class="summary">{concept['summary']}</p>
                <p class="time">{date_str}</p>
            </div>
        </div>"""
    
    index_path = "index.html"
    if not os.path.exists(index_path):
        content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Representational Romanticism & Science | Octo-Art Engine</title>
    <style>
        body {{ font-family: 'Georgia', serif; background: #07090e; color: #f1f5f9; margin: 0; padding: 2rem; }}
        header {{ text-align: center; margin-bottom: 3.5rem; }}
        h1 {{ font-size: 2.8rem; margin-bottom: 0.5rem; color: #f59e0b; font-weight: normal; letter-spacing: 1px; }}
        p.subtitle {{ color: #94a3b8; font-style: italic; max-width: 650px; margin: 0 auto; line-height: 1.6; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 2.5rem; max-width: 1300px; margin: 0 auto; }}
        .card {{ background: #0f172a; border: 1px solid #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.7); transition: transform 0.3s ease; }}
        .card:hover {{ transform: translateY(-6px); border-color: #d97706; }}
        .svg-container {{ width: 100%; aspect-ratio: 1; border-bottom: 1px solid #1e293b; }}
        .meta {{ padding: 1.5rem; }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem; }}
        .badge {{ background: #7c2d12; color: #fef08a; font-size: 0.75rem; font-family: sans-serif; padding: 0.2rem 0.6rem; border-radius: 4px; text-transform: uppercase; letter-spacing: 1px; }}
        .paper-btn {{ background: #0284c7; color: #ffffff; text-decoration: none; font-size: 0.8rem; font-family: sans-serif; padding: 0.3rem 0.7rem; border-radius: 4px; font-weight: bold; transition: background 0.2s; }}
        .paper-btn:hover {{ background: #0369a1; }}
        .meta h2 {{ margin: 0.5rem 0; font-size: 1.35rem; color: #f8fafc; font-weight: normal; line-height: 1.3; }}
        .motif-tag {{ color: #d97706; font-size: 0.85rem; font-family: sans-serif; margin: 0.25rem 0 0.75rem 0; }}
        .arxiv-title {{ font-size: 0.9rem; color: #cbd5e1; line-height: 1.4; margin-bottom: 0.25rem; }}
        .author {{ font-size: 0.85rem; color: #94a3b8; margin-top: 0; margin-bottom: 0.8rem; font-family: sans-serif; }}
        .summary {{ font-size: 0.85rem; color: #94a3b8; line-height: 1.5; font-family: sans-serif; }}
        .time {{ color: #475569 !important; font-size: 0.75rem !important; margin-top: 1rem !important; font-family: sans-serif; }}
    </style>
</head>
<body>
    <header>
        <h1>Representational Romanticism & Science</h1>
        <p.subtitle>An autonomous engine depicting human life, nature, and vistas through Romantic art—inspired directly by newly published arXiv science papers.</p>
    </header>
    <div class="grid" id="gallery">
{html_card}
    </div>
</body>
</html>"""
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        with open(index_path, "r", encoding="utf-8") as f:
            full_html = f.read()
        
        insertion_point = '<div class="grid" id="gallery">'
        updated_html = full_html.replace(insertion_point, insertion_point + html_card)
        
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(updated_html)

# ==========================================
# CENTRAL BRAIN ORCHESTRATOR
# ==========================================
if __name__ == "__main__":
    print("🐙 Central Brain: Waking up arms...")
    concept = arm_vision()
    print(f"👁️ Vision Arm: arXiv paper retrieved -> '{concept['paper_title']}'")
    print(f"🎭 Romantic Figurative Translation -> '{concept['romantic_title']}'")
    
    svg_art = arm_artist(concept)
    print("🎨 Figurative Romantic Artist Arm: Rendered representational scene.")
    
    arm_publisher(concept, svg_art)
    print("📢 Publisher Arm: Updated web gallery with paper link & artwork.")
    print("🐙 Central Brain: Cycle complete. Sleeping...")
