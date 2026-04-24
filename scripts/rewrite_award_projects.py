import os

base = "/Users/s.shreeramsankar/Desktop/portfolio"

# ─── AWARD DETAIL PAGE ───────────────────────────────────────────────────────
award_page = r"""---
import '../../styles/global.css';

export function getStaticPaths() {
  return ['3ducate', 'siteiq', 'pinpoint'].map(slug => ({ params: { slug } }));
}

function getAwardData(slug: string) {
  const d: Record<string, any> = {
    '3ducate': {
      title: '3Ducate', headline: 'AR Anatomical Platform Wins First Place at HawkHack 2025',
      award: '1st Place', hackathon: 'HawkHack 2025', date: 'January 2025', location: 'Raleigh, NC',
      tags: ['Python', 'AR', 'Computer Vision', 'Generative AI'], category: 'EDTECH & AR',
      overview: '3Ducate layers augmented reality over anatomical models with AI explanations on demand. Led a four-member team to first place at HawkHack 2025 among 30 competing teams.',
      problem: 'Medical education relies on textbooks and 2D diagrams. Students struggle to understand 3D anatomy without expensive physical models or cadaver lab access.',
      solution: 'An AR system that detects surfaces in real-time and overlays detailed anatomical models. Students tap any structure to receive a Gemini-powered natural language explanation instantly.',
      impact: 'First place prize among 30 teams. Invitation to pitch at Carolina LaunchPad. Recognized for innovation and technical execution by industry judges.',
      features: [
        { title: 'Real-time Surface Detection', desc: 'Uses ARKit/ARCore to anchor models precisely onto physical surfaces.' },
        { title: 'AI-Powered Explanations', desc: 'Gemini API generates contextual explanations for any selected anatomical structure on demand.' },
        { title: 'Multi-Model Library', desc: 'Complete library from skeletal to muscular and vascular systems.' },
        { title: 'Judges Awarded', desc: 'First place for innovation and technical execution among all 30 submissions.' },
      ],
      techStack: { 'Frontend': ['React Native', 'ARKit', 'ARCore'], 'AI / ML': ['Google Gemini API', 'OpenCV'], 'Backend': ['Python', 'FastAPI'], 'Infrastructure': ['GCP Cloud Run', 'Firebase'] },
    },
    'siteiq': {
      title: 'SiteIQ', headline: 'Autonomous AI Agent Wins 3rd Place at Anti-Slopathon 2026',
      award: '3rd Place', hackathon: 'Anti-Slopathon', date: 'March 2026', location: 'New York, NY',
      tags: ['Python', 'Geospatial APIs', 'Generative AI'], category: 'REAL ESTATE & AI',
      overview: 'SiteIQ fuses geospatial mapping, live transit data, and Generative AI to produce structured real estate investment reports — automating analysis from hours down to under 3 seconds.',
      problem: 'Real estate investors make high-stakes decisions on incomplete information. Analyzing transit access, zoning, demographics, and market comps takes days across multiple specialist tools.',
      solution: 'SiteIQ ingests live NYC transit feeds, zoning data, and property records into a unified geospatial pipeline. An autonomous reasoning agent issues a binary Invest/Avoid verdict with a structured supporting report.',
      impact: '3rd place at Anti-Slopathon among NYC-based AI builders. Recognized for real-world applicability and depth of technical implementation by judges including industry professionals.',
      features: [
        { title: 'Live Data Ingestion', desc: 'Real-time NYC transit APIs, zoning records, and property market feeds via GCP Pub/Sub.' },
        { title: 'Autonomous Reasoning Agent', desc: 'LLM-based agent with tool access for data querying, calculation, and report generation.' },
        { title: 'Structured Report Output', desc: 'Every verdict ships with a JSON report enabling full audit traceability.' },
        { title: 'Sub-3 Second Analysis', desc: '92% verdict alignment with expert investors at under 3 seconds per property.' },
      ],
      techStack: { 'AI / Agents': ['LLM Reasoning Agent', 'Google Gemini API', 'RAG'], 'Data': ['GCP Pub/Sub', 'BigQuery', 'Geospatial APIs'], 'Frontend': ['React', 'Mapbox GL'], 'Backend': ['Python', 'FastAPI'] },
    },
    'pinpoint': {
      title: 'Pin Point', headline: 'Decentralized Anti-Deepfake Protocol Wins Best Use of Solana at QuackHacks',
      award: 'Best Use of Solana', hackathon: 'QuackHacks', date: 'February 2026', location: 'Online',
      tags: ['On-device ML', 'Solana', 'Blockchain', 'Computer Vision'], category: 'WEB3 & SECURITY',
      overview: 'Pin Point immutably stamps location-verified media on-chain with on-device ML filtering, creating an unforgeable audit trail against deepfake proliferation. Shipped end-to-end in 24 hours.',
      problem: 'Deepfake technology enables fabrication of video and audio evidence, eroding trust in digital media. Centralized verification authorities are single points of failure.',
      solution: 'Pin Point runs ML filtering on-device before capturing, stamps each piece of media with GPS data, and anchors the hash to the Solana blockchain for trustless, immutable verification.',
      impact: 'Best Use of Solana award at QuackHacks. Recognized for novel application of blockchain for anti-deepfake verification. Smart contracts live on Solana mainnet.',
      features: [
        { title: 'On-Device ML Authenticity Filter', desc: 'Detects manipulation artifacts before capture, preventing tampered media from entering the pipeline.' },
        { title: 'GPS Cryptographic Anchoring', desc: 'Media is bound to precise GPS coordinates and timestamp before Solana submission.' },
        { title: 'Immutable On-Chain Record', desc: 'Solana ledger stores the evidence hash with no central authority required.' },
        { title: 'Shipped in 24 hours', desc: 'Complete end-to-end implementation from concept to Solana mainnet deployment in one hackathon session.' },
      ],
      techStack: { 'Blockchain': ['Solana', 'Anchor Framework', 'Web3.js'], 'AI / ML': ['TensorFlow Lite', 'On-device CV'], 'Mobile': ['React Native', 'Expo'], 'Backend': ['Python', 'FastAPI'] },
    },
  };
  return d[slug];
}

const { slug } = Astro.params;
const award = getAwardData(slug);
if (!award) return Astro.redirect('/');
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content={`${award.title} — ${award.overview}`} />
  <title>{award.title} — The Shreeram Chronicle</title>
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,700&family=Playfair+Display+SC:wght@400;700;900&family=IBM+Plex+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" />
</head>
<body class="bg-paper">

  <nav class="sticky top-0 z-50 bg-paper border-b-2 border-ink no-print">
    <div class="max-w-5xl mx-auto px-4 flex items-center justify-between h-9">
      <div class="flex items-center gap-4">
        <a href="/awards" class="font-mono text-caption uppercase tracking-widest text-ink hover:text-ink-light transition-colors">← All Awards</a>
        <span class="text-ink-faded hidden sm:block">·</span>
        <span class="font-mono text-caption text-ink-faded hidden sm:block">{award.category}</span>
      </div>
      <a href="/" class="font-mono text-caption uppercase tracking-widest text-ink-faded hover:text-ink transition-colors hidden md:block">Home</a>
    </div>
  </nav>

  <main class="max-w-5xl mx-auto px-4 sm:px-6 pb-24">

    <!-- HERO SECTION -->
    <header class="pt-10 pb-8 border-b-2 border-ink">
      <div class="flex items-start justify-between gap-4 mb-4 flex-wrap">
        <span class="section-label">{award.category}</span>
        <span class="font-mono text-caption text-ink border border-ink px-3 py-1 text-xs">{award.hackathon}</span>
      </div>
      <div class="mb-4 pb-4 border-b-2 border-ink">
        <p class="font-display font-black text-ink" style="font-size: clamp(3rem, 8vw, 6rem); line-height: 1;">{award.award}</p>
      </div>
      <h1 class="font-display font-bold text-ink leading-tight mb-4 text-balance" style="font-size: clamp(1.5rem, 3.5vw, 2.5rem);">{award.headline}</h1>
      <p class="font-serif italic text-body-print text-ink-light mb-6 max-w-3xl text-lg">{award.overview}</p>
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-0 border-t-2 border-b-2 border-ink py-3">
        {[{label:'Award',value:award.award},{label:'Hackathon',value:award.hackathon},{label:'Date',value:award.date},{label:'Location',value:award.location}].map((m: any, i: number) => (
          <div class={`px-4 text-center ${i < 3 ? 'border-r border-ink' : ''}`}>
            <p class="font-mono text-caption text-ink-faded uppercase tracking-wider mb-0.5">{m.label}</p>
            <p class="font-serif font-bold text-ink text-sm">{m.value}</p>
          </div>
        ))}
      </div>
      <div class="flex flex-wrap gap-2 mt-4">
        {award.tags.map((tag: string) => <span class="font-mono text-caption border border-ink px-2 py-0.5 text-ink text-xs">{tag}</span>)}
      </div>
    </header>

    <!-- IMAGE CAROUSEL -->
    <section class="py-8 border-b-2 border-ink">
      <p class="section-label mb-4">Project Gallery</p>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
        {[0,1,2].map((i: number) => (
          <div class="w-full h-56 bg-column-bg border-2 border-ink flex items-center justify-center">
            <span class="font-mono text-xs text-ink-faded">[ Upload Image {i+1} ]</span>
          </div>
        ))}
      </div>
    </section>

    <!-- PROBLEM / SOLUTION -->
    <section class="py-8 border-b-2 border-ink">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
        <div class="md:border-r border-ink pr-0 md:pr-8 pb-8 md:pb-0">
          <div class="rule-thick mb-4"></div>
          <p class="section-label font-bold mb-3">The Problem</p>
          <p class="font-serif text-body-print text-ink-light leading-relaxed">{award.problem}</p>
        </div>
        <div class="pl-0 md:pl-8 pt-8 md:pt-0 border-t md:border-t-0 border-ink">
          <div class="rule-thick mb-4"></div>
          <p class="section-label font-bold mb-3">The Solution</p>
          <p class="font-serif text-body-print text-ink-light leading-relaxed">{award.solution}</p>
        </div>
      </div>
    </section>

    <!-- IMPACT -->
    <section class="py-8 border-b-2 border-ink bg-column-bg -mx-4 sm:-mx-6 px-4 sm:px-6">
      <div class="rule-thick mb-4"></div>
      <p class="section-label font-bold mb-3">Award Impact</p>
      <p class="font-serif text-body-print text-ink-light leading-relaxed max-w-3xl">{award.impact}</p>
    </section>

    <!-- FEATURES -->
    <section class="py-8 border-b-2 border-ink">
      <div class="flex items-center gap-3 mb-6">
        <span class="section-label font-bold">Key Features</span>
        <div class="flex-1 border-t border-ink"></div>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {award.features.map((f: any, i: number) => (
          <div class="border-2 border-ink p-5 bg-paper">
            <p class="font-mono text-caption text-ink-faded mb-2">0{i+1}</p>
            <p class="font-display font-bold text-ink mb-2">{f.title}</p>
            <p class="font-serif text-body-print text-ink-light text-sm">{f.desc}</p>
          </div>
        ))}
      </div>
    </section>

    <!-- TECH STACK -->
    <section class="py-8 border-b-2 border-ink">
      <div class="flex items-center gap-3 mb-6">
        <span class="section-label font-bold">Tech Stack</span>
        <div class="flex-1 border-t border-ink"></div>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
        {Object.entries(award.techStack).map(([cat, techs]: [string, any]) => (
          <div>
            <p class="font-mono text-caption uppercase tracking-widest text-ink-faded mb-3 border-b border-ink pb-1">{cat}</p>
            <div class="flex flex-wrap gap-2">
              {(techs as string[]).map((t: string) => <span class="font-mono text-caption border-2 border-ink px-3 py-1 text-ink text-xs">{t}</span>)}
            </div>
          </div>
        ))}
      </div>
    </section>

    <!-- FOOTER NAV -->
    <section class="pt-8 flex items-center justify-between flex-wrap gap-4">
      <a href="/awards" class="font-mono text-caption uppercase tracking-widest border-2 border-ink px-6 py-3 hover:bg-ink hover:text-paper transition-all">← All Awards</a>
      <a href="/" class="font-mono text-caption uppercase tracking-widest border-2 border-ink px-6 py-3 hover:bg-ink hover:text-paper transition-all">Back to Portfolio</a>
    </section>

  </main>
</body>
</html>
"""

# ─── PROJECTS LISTING PAGE (updated) ────────────────────────────────────────
projects_listing = r"""---
import '../../styles/global.css';

const projects = [
  {
    slug: '3ducate', headline: 'AR Anatomical Platform with Generative AI Contextual Explanations',
    deck: '3Ducate layers augmented reality over anatomical models, with an AI layer that explains any structure in natural language on demand.',
    tags: ['Python', 'AR', 'Computer Vision', 'Generative AI'], award: '1st Place — HawkHack 2025', col: 'EDTECH & AR', date: 'Jan 2025',
  },
  {
    slug: 'siteiq', headline: 'Autonomous AI Agent Delivering Invest/Avoid Verdicts on NYC Real Estate',
    deck: 'SiteIQ fuses geospatial mapping, live transit data, and generative AI to produce structured investment reports in seconds.',
    tags: ['Python', 'Geospatial APIs', 'Generative AI'], award: '3rd Place — Anti-Slopathon', col: 'REAL ESTATE & AI', date: 'Mar 2026',
  },
  {
    slug: 'pinpoint', headline: 'Decentralized Anti-Deepfake Protocol Anchoring Physical Reality on Solana',
    deck: 'Pin Point immutably stamps location-verified media on-chain with on-device ML filtering.',
    tags: ['On-device ML', 'Solana', 'Blockchain'], award: 'Best Use of Solana — QuackHacks', col: 'WEB3 & SECURITY', date: 'Feb 2026',
  },
  {
    slug: 'piggilytics', headline: 'AI Financial Platform Generating Video Explainers of Your Spending Behavior',
    deck: 'Piggilytics AI automates statement parsing, builds live dashboards, and produces AI-narrated video breakdowns.',
    tags: ['Python', 'Flask', 'PyTorch', 'Gemini API'], award: null, col: 'FINTECH', date: 'Nov 2024',
  },
  {
    slug: 'dealscout', headline: 'Full-Stack Price Comparison App from Figma Wireframe to Azure Production in Two Weeks',
    deck: 'Deal Scout proves that disciplined Agile sprints and modern cloud tooling can compress deployment timelines by 10x.',
    tags: ['React', 'Python', 'Azure'], award: null, col: 'E-COMMERCE', date: 'Aug 2023',
  },
  {
    slug: 'covpred', headline: 'End-to-End Epidemiology & Genomics Analytics Platform Built as Year-Long Thesis',
    deck: 'CovPred integrates public health, DNA, and research datasets with AI-generated reports and epidemic-spread dashboards.',
    tags: ['Python', 'CDC APIs', 'Gemini API', 'Bioinformatics'], award: null, col: 'RESEARCH', date: 'May 2024',
  },
];
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="All Projects — Shreeram Sankar's AI & Full-Stack Engineering Work" />
  <title>All Projects — The Shreeram Chronicle</title>
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,700&family=Playfair+Display+SC:wght@400;700;900&family=IBM+Plex+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" />
</head>
<body class="bg-paper">

  <nav class="sticky top-0 z-50 bg-paper border-b-2 border-ink no-print">
    <div class="max-w-7xl mx-auto px-4 flex items-center justify-between h-9">
      <div class="flex items-center gap-6">
        <a href="/" class="font-mono text-caption uppercase tracking-widest text-ink hover:text-ink-light transition-colors">← Back Home</a>
        <span class="text-ink-faded">·</span>
        <span class="font-mono text-caption uppercase tracking-widest text-ink-faded">All Projects</span>
      </div>
    </div>
  </nav>

  <main class="max-w-7xl mx-auto px-4 sm:px-6 pb-24">

    <!-- HEADER -->
    <header class="pt-8 border-b-2 border-ink mb-10">
      <div class="rule-thick mb-4"></div>
      <h1 class="font-display font-black uppercase leading-tight text-ink mb-4" style="font-size: clamp(2.5rem, 7vw, 5rem);">
        All Projects
      </h1>
      <p class="font-serif italic text-body-print text-ink-light mb-6 max-w-2xl">
        Complete portfolio of shipped projects — from rapid hackathon prototypes to year-long production systems. Each represents an end-to-end delivery from conception to deployment.
      </p>
      <div class="flex items-center gap-4 pb-6 flex-wrap">
        <span class="font-mono text-caption text-ink-faded">{projects.length} projects</span>
        <div class="flex-1 border-t border-ink"></div>
        <span class="font-mono text-caption text-ink-faded">Most Recent First</span>
      </div>
    </header>

    <!-- PROJECTS GRID -->
    <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {projects.map((project, i) => (
        <article class="border-2 border-ink bg-paper flex flex-col hover:border-ink-light transition-all">
          <!-- Image Placeholder -->
          <div class="w-full h-48 bg-column-bg border-b-2 border-ink flex items-center justify-center">
            <span class="font-mono text-xs text-ink-faded">[ Project Image ]</span>
          </div>

          <!-- Content -->
          <div class="p-5 flex flex-col flex-1">
            <div class="flex items-start justify-between gap-2 mb-2">
              <span class="section-label text-ink">{project.col}</span>
              <span class="font-mono text-caption text-ink-faded text-xs whitespace-nowrap">{project.date}</span>
            </div>

            {project.award && (
              <span class="font-mono text-caption text-ink border border-ink px-2 py-0.5 text-xs mb-3 w-fit">{project.award}</span>
            )}

            <h3 class="font-display font-bold text-ink leading-tight mb-2 text-balance" style="font-size: 1.1rem;">
              {project.headline}
            </h3>

            <p class="font-serif italic text-body-print text-ink-light mb-4 text-sm flex-1">
              {project.deck}
            </p>

            <div class="flex flex-wrap gap-1 mb-4">
              {project.tags.map((tag: string) => (
                <span class="font-mono text-caption text-ink border border-ink px-1.5 py-0.5 text-xs">{tag}</span>
              ))}
            </div>

            <a href={`/project/${project.slug}`} class="font-mono text-caption uppercase tracking-wider text-ink border-b-2 border-ink hover:text-ink-light transition-colors inline-block mt-auto">
              View Project →
            </a>
          </div>
        </article>
      ))}
    </section>

    <!-- FOOTER CTA -->
    <section class="mt-12 pt-8 border-t-2 border-ink text-center">
      <a href="/" class="font-mono text-caption uppercase tracking-widest border-2 border-ink px-6 py-3 hover:bg-ink hover:text-paper transition-all duration-200 inline-block">
        ← Back to Portfolio
      </a>
    </section>

  </main>
</body>
</html>
"""

files = {
    "src/pages/award/[slug].astro": award_page,
    "src/pages/projects/index.astro": projects_listing,
}

for path, content in files.items():
    full_path = os.path.join(base, path)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Written {path}: {len(content.splitlines())} lines")

print("Done!")
