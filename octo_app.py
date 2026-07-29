import os
import random
import datetime
import math

# ==========================================
# ARM 1: THE VISION ARM (Generates Concept)
# ==========================================
THEMES = [
    {"name": "Cosmic Nebula", "palettes": [["#0f172a", "#312e81", "#581c87", "#38bdf8", "#f43f5e"]]},
    {"name": "Cybernetic Sunset", "palettes": [["#18181b", "#3f3f46", "#701a75", "#f43f5e", "#fbbf24"]]},
    {"name": "Deep Sea Luminescence", "palettes": [["#022c22", "#064e3b", "#0d9488", "#2dd4bf", "#f0fdf4"]]},
    {"name": "Solar Flare", "palettes": [["#450a0a", "#7f1d1d", "#dc2626", "#f97316", "#fef08a"]]},
    {"name": "Neon Midnight", "palettes": [["#030712", "#1e1b4b", "#4338ca", "#a855f7", "#ec4899"]]},
    {"name": "Emerald Canopy", "palettes": [["#052e16", "#14532d", "#16a34a", "#4ade80", "#fef08a"]]}
]

ADJECTIVES = ["Quantum", "Ethereal", "Harmonic", "Infinite", "Algorithmic", "Pulsing", "Radial", "Luminous", "Starlight", "Prismatic"]
NOUNS = ["Resonance", "Monolith", "Symphony", "Labyrinth", "Horizon", "Tesseract", "Drift", "Nexus", "Orbit", "Cascade"]

def arm_vision():
    theme = random.choice(THEMES)
    palette = random.choice(theme["palettes"])
    title = f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}"
    return {"theme": theme["name"], "palette": palette, "title": title}

# ==========================================
# ARM 2: THE ARTIST ARM (Renders Visuals)
# ==========================================
def arm_artist(concept):
    colors = concept["palette"]
    bg_color = colors[0]
    art_colors = colors[1:]
    
    width, height = 800, 800
    svg_elements = []
    
    center_x, center_y = width / 2, height / 2
    num_shapes = random.randint(16, 32)
    
    for i in range(num_shapes):
        color = random.choice(art_colors)
        opacity = round(random.uniform(0.25, 0.85), 2)
        shape_type = random.choice(["circle", "polygon", "ring", "line"])
        
        if shape_type == "circle":
            r = random.randint(20, 260)
            cx = center_x + random.randint(-220, 220)
            cy = center_y + random.randint(-220, 220)
            svg_elements.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{opacity}" />')
            
        elif shape_type == "polygon":
            points = []
            num_verts = random.randint(3, 6)
            base_r = random.randint(40, 220)
            off_x = center_x + random.randint(-180, 180)
            off_y = center_y + random.randint(-180, 180)
            
            for v in range(num_verts):
                angle = (2 * math.pi / num_verts) * v
                px = off_x + base_r * math.cos(angle) + random.randint(-25, 25)
                py = off_y + base_r * math.sin(angle) + random.randint(-25, 25)
                points.append(f"{px},{py}")
                
            pts_str = " ".join(points)
            svg_elements.append(f'<polygon points="{pts_str}" fill="{color}" opacity="{opacity}" />')
            
        elif shape_type == "ring":
            r = random.randint(60, 320)
            sw = random.randint(2, 14)
            svg_elements.append(f'<circle cx="{center_x}" cy="{center_y}" r="{r}" stroke="{color}" stroke-width="{sw}" fill="none" opacity="{opacity}" />')

        elif shape_type == "line":
            x1 = random.randint(50, 750)
            y1 = random.randint(50, 750)
            x2 = random.randint(50, 750)
            y2 = random.randint(50, 750)
            sw = random.randint(2, 8)
            svg_elements.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" opacity="{opacity}" />')

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    <rect width="{width}" height="{height}" fill="{bg_color}" />
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
    
    # Save raw SVG file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_code)
        
    # Format gallery card
    date_str = datetime.datetime.utcnow().strftime("%B %d, %Y - %H:00 UTC")
    
    html_card = f"""
        <div class="card">
            <div class="svg-container">{svg_code}</div>
            <div class="meta">
                <h2>{concept['title']}</h2>
                <p><strong>Theme:</strong> {concept['theme']}</p>
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
    <title>Octo-App Generative Art Gallery</title>
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; background: #090d16; color: #f8fafc; margin: 0; padding: 2rem; }}
        h1 {{ text-align: center; font-size: 2.5rem; margin-bottom: 0.5rem; color: #38bdf8; }}
        p.subtitle {{ text-align: center; color: #94a3b8; margin-bottom: 3rem; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 2rem; max-width: 1200px; margin: 0 auto; }}
        .card {{ background: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5); transition: transform 0.2s; }}
        .card:hover {{ transform: translateY(-4px); }}
        .svg-container {{ width: 100%; aspect-ratio: 1; }}
        .meta {{ padding: 1.25rem; }}
        .meta h2 {{ margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #f1f5f9; }}
        .meta p {{ margin: 0.25rem 0; color: #cbd5e1; font-size: 0.9rem; }}
        .time {{ color: #64748b !important; font-size: 0.8rem !important; margin-top: 0.75rem !important; }}
    </style>
</head>
<body>
    <h1>🐙 Octo-Art Engine</h1>
    <p class="subtitle">An autonomous multi-armed app generating hourly vector artwork.</p>
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
    print(f"👁️ Vision Arm: Concept selected -> '{concept['title']}' ({concept['theme']})")
    
    svg_art = arm_artist(concept)
    print("🎨 Artist Arm: Rendered new SVG masterpiece.")
    
    arm_publisher(concept, svg_art)
    print("📢 Publisher Arm: Updated live web gallery.")
    print("🐙 Central Brain: Cycle complete. Sleeping...")
