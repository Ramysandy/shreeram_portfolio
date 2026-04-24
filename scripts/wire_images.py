import os, shutil

base = "/Users/s.shreeramsankar/Desktop/portfolio"
dest = os.path.join(base, "public/images/projects")
os.makedirs(dest, exist_ok=True)

# ── Copy & rename images ────────────────────────────────────────────────────
copies = [
  ("projects/3ducate/1745894215333.jpeg", "3ducate-1.jpeg"),
  ("projects/3ducate/1745894215417.jpeg", "3ducate-2.jpeg"),
  ("projects/3ducate/1745894215724.jpeg", "3ducate-3.jpeg"),
  ("projects/3ducate/1745894221098.jpeg", "3ducate-4.jpeg"),
  ("projects/Siteiq/Site IQ (5).jpg", "siteiq-1.jpg"),
  ("projects/Siteiq/Site IQ (6).jpg", "siteiq-2.jpg"),
  ("projects/Siteiq/Site IQ (7).jpg", "siteiq-3.jpg"),
  ("projects/Siteiq/Site IQ (8).jpg", "siteiq-4.jpg"),
  ("projects/pinpoint/Pin Point (2).jpg", "pinpoint-1.jpg"),
  ("projects/pinpoint/Pin Point (3).jpg", "pinpoint-2.jpg"),
  ("projects/pinpoint/Pin Point (4).jpg", "pinpoint-3.jpg"),
  ("projects/piglittics/gallery.jpg",     "piggilytics-1.jpg"),
  ("projects/piglittics/gallery (1).jpg", "piggilytics-2.jpg"),
  ("projects/piglittics/gallery (2).jpg", "piggilytics-3.jpg"),
  ("projects/piglittics/gallery (3).jpg", "piggilytics-4.jpg"),
  ("projects/dealscout/Screenshot 2026-04-24 at 2.54.58 PM.png", "dealscout-1.png"),
  ("projects/dealscout/Screenshot 2026-04-24 at 2.55.24 PM.png", "dealscout-2.png"),
  ("projects/dealscout/Screenshot 2026-04-24 at 2.55.38 PM.png", "dealscout-3.png"),
  ("projects/dealscout/Screenshot 2026-04-24 at 2.55.51 PM.png", "dealscout-4.png"),
  ("projects/covpred/Screenshot 2026-04-24 at 2.57.58 PM.png", "covpred-1.png"),
  ("projects/covpred/Screenshot 2026-04-24 at 2.58.10 PM.png", "covpred-2.png"),
  ("projects/covpred/Screenshot 2026-04-24 at 2.58.21 PM.png", "covpred-3.png"),
  ("projects/covpred/Screenshot 2026-04-24 at 2.58.33 PM.png", "covpred-4.png"),
  ("projects/covpred/Screenshot 2026-04-24 at 2.58.41 PM.png", "covpred-5.png"),
  ("projects/veridion/gallery.jpg",     "veridion-x-1.jpg"),
  ("projects/veridion/gallery (1).jpg", "veridion-x-2.jpg"),
  ("projects/veridion/gallery (2).jpg", "veridion-x-3.jpg"),
  ("projects/visionsentialai/gallery (3).jpg", "visionsentinel-1.jpg"),
  ("projects/visionsentialai/gallery (4).jpg", "visionsentinel-2.jpg"),
  ("projects/visionsentialai/gallery (5).jpg", "visionsentinel-3.jpg"),
]

for src_rel, dst_name in copies:
    src_path = os.path.join(base, src_rel)
    dst_path = os.path.join(dest, dst_name)
    shutil.copy2(src_path, dst_path)
    print(f"  copied {dst_name}")

print(f"\n{len(copies)} images copied to public/images/projects/\n")

# ── Image arrays per slug ────────────────────────────────────────────────────
img = {
  "3ducate":        ["/images/projects/3ducate-1.jpeg","/images/projects/3ducate-2.jpeg","/images/projects/3ducate-3.jpeg","/images/projects/3ducate-4.jpeg"],
  "siteiq":         ["/images/projects/siteiq-1.jpg","/images/projects/siteiq-2.jpg","/images/projects/siteiq-3.jpg","/images/projects/siteiq-4.jpg"],
  "pinpoint":       ["/images/projects/pinpoint-1.jpg","/images/projects/pinpoint-2.jpg","/images/projects/pinpoint-3.jpg"],
  "piggilytics":    ["/images/projects/piggilytics-1.jpg","/images/projects/piggilytics-2.jpg","/images/projects/piggilytics-3.jpg","/images/projects/piggilytics-4.jpg"],
  "dealscout":      ["/images/projects/dealscout-1.png","/images/projects/dealscout-2.png","/images/projects/dealscout-3.png","/images/projects/dealscout-4.png"],
  "covpred":        ["/images/projects/covpred-1.png","/images/projects/covpred-2.png","/images/projects/covpred-3.png","/images/projects/covpred-4.png","/images/projects/covpred-5.png"],
  "visionsentinel": ["/images/projects/visionsentinel-1.jpg","/images/projects/visionsentinel-2.jpg","/images/projects/visionsentinel-3.jpg"],
  "veridion-x":     ["/images/projects/veridion-x-1.jpg","/images/projects/veridion-x-2.jpg","/images/projects/veridion-x-3.jpg"],
}

# ── Update project/[slug].astro ──────────────────────────────────────────────
slug_path = os.path.join(base, "src/pages/project/[slug].astro")
with open(slug_path) as f:
    src = f.read()

# Unique overview anchors per project — inject images array just before each
unique_overview = {
  "3ducate":        "      overview: '3Ducate layers augmented reality",
  "siteiq":         "      overview: 'SiteIQ fuses geospatial mapping",
  "pinpoint":       "      overview: 'Pin Point immutably stamps",
  "piggilytics":    "      overview: 'Piggilytics automates bank",
  "dealscout":      "      overview: 'Deal Scout aggregates prices",
  "covpred":        "      overview: 'CovPred integrates public health",
  "visionsentinel": "      overview: 'VisionSentinel AI gives first",
  "veridion-x":     "      overview: 'VERIDION-X is a gig economy",
}

for slug_key, imgs in img.items():
    arr_str = "['" + "','".join(imgs) + "']"
    old_ov = unique_overview[slug_key]
    if old_ov not in src:
        print(f"WARNING: anchor not found for {slug_key}")
        continue
    src = src.replace(old_ov, f"      images: {arr_str},\n" + old_ov)
    print(f"  injected images[] for {slug_key}")

# Replace static carousel with dynamic one
old_carousel = """    <!-- IMAGE CAROUSEL -->
    <section class="border-b-2 border-ink" data-carousel>
      <div class="relative overflow-hidden" style="height:480px;">
        <div class="carousel-track flex h-full" style="transition:transform 0.5s ease-in-out;">
          <div class="carousel-slide flex-shrink-0 w-full h-full bg-column-bg flex items-center justify-center">
            <span class="font-mono text-sm text-ink-faded">[ Image 01 ]</span>
          </div>
          <div class="carousel-slide flex-shrink-0 w-full h-full bg-column-bg flex items-center justify-center">
            <span class="font-mono text-sm text-ink-faded">[ Image 02 ]</span>
          </div>
          <div class="carousel-slide flex-shrink-0 w-full h-full bg-column-bg flex items-center justify-center">
            <span class="font-mono text-sm text-ink-faded">[ Image 03 ]</span>
          </div>
        </div>
        <button class="carousel-prev absolute left-3 top-1/2 -translate-y-1/2 z-10 border-2 border-ink bg-paper w-12 h-12 flex items-center justify-center font-mono text-2xl leading-none hover:bg-ink hover:text-paper transition-all">&#8249;</button>
        <button class="carousel-next absolute right-3 top-1/2 -translate-y-1/2 z-10 border-2 border-ink bg-paper w-12 h-12 flex items-center justify-center font-mono text-2xl leading-none hover:bg-ink hover:text-paper transition-all">&#8250;</button>
        <div class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">
          <button class="carousel-dot w-2.5 h-2.5 bg-ink transition-opacity" style="opacity:1"></button>
          <button class="carousel-dot w-2.5 h-2.5 bg-ink transition-opacity" style="opacity:0.3"></button>
          <button class="carousel-dot w-2.5 h-2.5 bg-ink transition-opacity" style="opacity:0.3"></button>
        </div>
        <div class="absolute bottom-4 right-4 font-mono text-xs text-ink bg-paper border border-ink px-2 py-1">
          <span class="carousel-counter">01 / 03</span>
        </div>
      </div>
    </section>"""

new_carousel = """    <!-- IMAGE CAROUSEL -->
    <section class="border-b-2 border-ink" data-carousel data-count={project.images.length}>
      <div class="relative overflow-hidden" style="height:480px;">
        <div class="carousel-track flex h-full" style="transition:transform 0.5s ease-in-out;">
          {project.images.map((img: string, i: number) => (
            <div class="carousel-slide flex-shrink-0 w-full h-full">
              <img src={img} class="w-full h-full object-cover" alt={`${project.title} screenshot ${i + 1}`} />
            </div>
          ))}
        </div>
        <button class="carousel-prev absolute left-3 top-1/2 -translate-y-1/2 z-10 border-2 border-ink bg-paper w-12 h-12 flex items-center justify-center font-mono text-2xl leading-none hover:bg-ink hover:text-paper transition-all">&#8249;</button>
        <button class="carousel-next absolute right-3 top-1/2 -translate-y-1/2 z-10 border-2 border-ink bg-paper w-12 h-12 flex items-center justify-center font-mono text-2xl leading-none hover:bg-ink hover:text-paper transition-all">&#8250;</button>
        <div class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">
          {project.images.map((_: any, i: number) => (
            <button class="carousel-dot w-2.5 h-2.5 bg-ink transition-opacity" style={i === 0 ? 'opacity:1' : 'opacity:0.3'}></button>
          ))}
        </div>
        <div class="absolute bottom-4 right-4 font-mono text-xs text-ink bg-paper border border-ink px-2 py-1">
          <span class="carousel-counter">01 / {String(project.images.length).padStart(2, '0')}</span>
        </div>
      </div>
    </section>"""

if old_carousel in src:
    src = src.replace(old_carousel, new_carousel)
    print("  carousel section updated to dynamic")
else:
    print("WARNING: carousel section not found")

src = src.replace(
    "    var total = 3, cur = 0;",
    "    var total = parseInt(carousel.dataset.count || '3'), cur = 0;"
)
print("  JS total updated to dynamic")

with open(slug_path, "w") as f:
    f.write(src)
print(f"\nproject/[slug].astro: {len(src.splitlines())} lines")

# ── Update projects/index.astro ──────────────────────────────────────────────
idx_path = os.path.join(base, "src/pages/projects/index.astro")
with open(idx_path) as f:
    idx = f.read()

# Add thumb: field to each project entry — anchor on unique deck text
thumb_map = {
  "veridion-x":     ("/images/projects/veridion-x-1.jpg",    "deck: 'A gig economy for fraud"),
  "visionsentinel": ("/images/projects/visionsentinel-1.jpg", "deck: 'VisionSentinel runs YOLOv8"),
  "3ducate":        ("/images/projects/3ducate-1.jpeg",       "deck: '3Ducate layers augmented reality"),
  "siteiq":         ("/images/projects/siteiq-1.jpg",         "deck: 'SiteIQ fuses geospatial mapping"),
  "pinpoint":       ("/images/projects/pinpoint-1.jpg",       "deck: 'Pin Point immutably stamps"),
  "piggilytics":    ("/images/projects/piggilytics-1.jpg",    "deck: 'Piggilytics AI automates statement"),
  "dealscout":      ("/images/projects/dealscout-1.png",      "deck: 'Deal Scout proves that disciplined"),
  "covpred":        ("/images/projects/covpred-1.png",        "deck: 'CovPred integrates public health"),
}

for slug_key, (thumb, deck_start) in thumb_map.items():
    if deck_start not in idx:
        print(f"WARNING: deck anchor not found for {slug_key}")
        continue
    start = idx.find(deck_start)
    end = idx.find("',\n", start) + 3
    deck_line = idx[start:end]
    replacement = deck_line + f"    thumb: '{thumb}',\n"
    idx = idx.replace(deck_line, replacement)
    print(f"  thumb added to {slug_key} in listing")

# Replace image placeholder div with real img
old_ph = """          <!-- Image Placeholder -->
          <div class="w-full h-48 bg-column-bg border-b-2 border-ink flex items-center justify-center">
            <span class="font-mono text-xs text-ink-faded">[ Project Image ]</span>
          </div>"""

new_ph = """          <!-- Thumbnail -->
          <div class="w-full h-48 border-b-2 border-ink overflow-hidden bg-column-bg">
            {project.thumb
              ? <img src={project.thumb} class="w-full h-full object-cover" alt={project.headline} />
              : <div class="w-full h-full flex items-center justify-center"><span class="font-mono text-xs text-ink-faded">[ Image ]</span></div>
            }
          </div>"""

if old_ph in idx:
    idx = idx.replace(old_ph, new_ph)
    print("  listing card thumbnail updated")
else:
    print("WARNING: listing placeholder not found")

with open(idx_path, "w") as f:
    f.write(idx)
print(f"\nprojects/index.astro: {len(idx.splitlines())} lines")
print("\nAll done!")
