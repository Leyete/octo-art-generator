import os
import random
import datetime
import math
import urllib.request
import xml.etree.ElementTree as ET

# ==========================================
# ARM 1: THE VISION ARM (Fetches arXiv Paper)
# ==========================================
ARXIV_CATEGORIES = ["quant-ph", "astro-ph", "gr-qc", "cond-mat"]

ROMANTIC_PREFIXES = [
    "Meditation on", "The Sublime Mystery of", "Vision of", "Awe Before the",
    "The Tempest of", "Ethereal Echoes of", "The Infinite Reach of"
]

def arm_vision():
    category = random.choice(ARXIV_CATEGORIES)
    url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&sortBy=submittedDate&sortOrder=descending&max_results=10"
    
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
            
            romantic_title = f"{random.choice(ROMANTIC_PREFIXES)} {paper_title.split(':')[0][:40]}"
            
            return {
                "paper_title": paper_title,
                "paper_url": paper_url,
                "summary": summary[:250] + "...",
                "author": author_name,
                "romantic_title": romantic_title,
                "category": category
            }
    except Exception as e:
        print(f"arXiv Fetch Warning ({e}). Using offline Quantum Cosmological concept.")
        
    return {
        "paper_title": "Quantum Fluctuations in Spacetime Horizons",
        "paper_url": "https://arxiv.org",
        "summary": "An exploration into the thermodynamic and quantum state transitions occurring at cosmic horizon boundaries.",
        "author": "Octo-Researcher",
        "romantic_title": "Vision of the Quantum Horizon",
        "category": "gr-qc"
    }

# ==========================================
# ARM 2: THE ROMANTIC ARTIST ARM (SVG Engine)
# ==========================================
ROMANTIC_PALETTES = [
    # Turner Storm: Deep slate, indigo, fiery gold, ethereal cream
    ["#0b0f19", "#1e1b4b", "#7c2d12", "#d97706", "#fef08a", "#f8fafc"],
    # Friedrich Twilight: Deep abyss, crimson glow, mist cyan, golden hour
    ["#030712", "#450a0a", "#9f1239", "#0284c7", "#fbbf24", "#f0fdf4"],
    # Blake Cosmic: Void black, violet tempest, radiant magenta, starlight
    ["#090514", "#2e1065", "#7e22ce", "#e11d48", "#38bdf8", "#fef08a"]
]

def arm_artist(concept):
    palette = random.choice(ROMANTIC_PALETTES)
    bg_color = palette[0]
    art_colors = palette[1:]
    
    width, height = 800, 800
    svg_elements = []
    
    center_x, center_y = width / 2, height / 2
    
    # 1. Atmospheric Gradient (Romantic mist/sky effect)
    grad_id = f"bg_grad_{random.randint(1000,9999)}"
    svg_elements.append(f"""
    <defs>
        <radialGradient id="{grad_id}" cx="50%" cy="50%" r="75%">
            <stop offset="0%" stop-color="{palette[3]}" stop-opacity="0.8" />
            <stop offset="40%" stop-color="{palette[1]}" stop-opacity="0.6" />
            <stop offset="100%" stop-color="{bg_color}" stop-opacity="1" />
        </radialGradient>
        <filter id="blur">
            <feGaussianBlur stdDeviation="3" />
        </filter>
    </defs>
    <rect width="{width}" height="{height}" fill="url(#{grad_id})" />
    """)
    
    # 2. The Sublime Focal Core (Ethereal light source cutting through void)
    core_r = random.randint(180, 320)
    svg_elements.append(f'<circle cx="{center_x}" cy="{center_y}" r="{core_r}" fill="{palette[4]}" opacity="0.15" filter="url(#blur)" />')
    svg_elements.append(f'<circle cx="{center_x}" cy="{center_y}" r="{core_r//2}" fill="{palette[3]}" opacity="0.25" filter="url(#blur)" />')

    # 3. Golden Ratio Spirals & Organic Field Curves (Representing physical law as natural majesty)
    num_curves = random.randint(30, 60)
    for i in range(num_curves):
        color = random.choice(art_colors)
        opacity = round(random.uniform(0.15, 0.7), 2)
        sw = random.uniform(0.8, 3.5)
        
        # Spiral mathematics (Golden Ratio growth)
        points = []
        angle = 0
        radius = random.randint(5, 30)
        growth = random.uniform(1.08, 1.15)
        
        start_x = center_x + random.randint(-150, 150)
        start_y = center_y + random.randint(-150, 150)
        
        for _ in range(random.randint(20, 45)):
            px = start_x + radius * math.cos(angle)
            py = start_y + radius * math.sin(angle)
            points.append(f"{px:.1f},{py:.1f}")
            angle += 0.3
            radius *= growth
            if radius > 450:
                break
                
        if len(points) > 2:
            pts_str = " ".join(points)
            svg_elements.append(f'<polyline points="{pts_str}" fill="none" stroke="{color}" stroke-width="{sw}" opacity="{opacity}" />')

    # 4. Stellar / Quantum Dust Swarm (Chiaroscuro light particles)
    num_particles = random.randint(150, 300)
    for _ in range(num_particles):
        px = center_x + random.gauss(0, 220)
        py = center_y + random.gauss(0, 220)
        pr = random.uniform(0.8, 3.2)
        p_color = random.choice([palette[3], palette[4], "#ffffff"])
        p_op = round(random.uniform(0.3, 0.9), 2)
        svg_elements.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{pr:.1f}" fill="{p_color}" opacity="{p_op}" />')

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    {''.join(svg_elements)}
</svg>"""
    return svg_content

# ==========================================
# ARM 3 & 4: PUBLISHER & HISTORIAN (Gallery)
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
                <span class="badge">{concept['category'].upper()}</span>
                <h2>{concept['romantic_title']}</h2>
                <p class="arxiv-title"><strong>Inspiration:</strong> <em>"{concept['paper_title']}"</em></p>
                <p class="author">By {concept['author']}</p>
                <p class="summary">{concept['summary']}</p>
                <a href="{concept['paper_url']}" target="_blank" class="paper-link">Read arXiv Paper &rarr;</a>
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
    <title>Cutting-Edge Romanticism | Octo-Art Engine</title>
    <style>
        body {{ font-family: 'Georgia', serif; background: #07090e; color: #f1f5f9; margin: 0; padding: 2rem; }}
        header {{ text-align: center; margin-bottom: 3.5rem; }}
        h1 {{ font-size: 2.8rem; margin-bottom: 0.5rem; color: #f59e0b; font-weight: normal; letter-spacing: 1px; }}
        p.subtitle {{ color: #94a3b8; font-style: italic; max-width: 600px; margin: 0 auto; line-height: 1.6; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 2.5rem; max-width: 1300px; margin: 0 auto; }}
        .card {{ background: #0f172a; border: 1px solid #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.7); transition: transform 0.3s ease; }}
        .card:hover {{ transform: translateY(-6px); border-color: #d97706; }}
        .svg-container {{ width: 100%; aspect-ratio: 1; border-bottom: 1px solid #1e293b; }}
        .meta {{ padding: 1.5rem; }}
        .badge {{ background: #7c2d12; color: #fef08a; font-size: 0.75rem; font-family: sans-serif; padding: 0.2rem 0.6rem; border-radius: 4px; text-transform: uppercase; letter-spacing: 1px; }}
        .meta h2 {{ margin: 0.8rem 0 0.5rem 0; font-size: 1.35rem; color: #f8fafc; font-weight: normal; }}
        .arxiv-title {{ font-size: 0.95rem; color: #cbd5e1; line-height: 1.4; margin-bottom: 0.25rem; }}
        .author {{ font-size: 0.85rem; color: #d97706; margin-top: 0; margin-bottom: 0.8rem; font-family: sans-serif; }}
        .summary {{ font-size: 0.85rem; color: #94a3b8; line-height: 1.5; font-family: sans-serif; }}
        .paper-link {{ display: inline-block; margin-top: 0.75rem; color: #38bdf8; text-decoration: none; font-size: 0.85rem; font-family: sans-serif; }}
        .paper-link:hover {{ text-decoration: underline; }}
        .time {{ color: #475569 !important; font-size: 0.75rem !important; margin-top: 1rem !important; font-family: sans-serif; }}
    </style>
</head>
<body>
    <header>
        <h1>Cutting-Edge Romanticism</h1>
        <p.subtitle>An autonomous engine contemplating live arXiv physics papers through the awe, sublime light, and organic infinity of Romantic period art.</p>
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
    print(f"🎭 Romantic Translation -> '{concept['romantic_title']}'")
    
    svg_art = arm_artist(concept)
    print("🎨 Romantic Artist Arm: Rendered sublime visual composition.")
    
    arm_publisher(concept, svg_art)
    print("📢 Publisher Arm: Updated web gallery with paper citation & artwork.")
    print("🐙 Central Brain: Cycle complete. Sleeping...")