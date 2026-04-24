import os
os.chdir('/Users/s.shreeramsankar/Desktop/portfolio')

import glob

pages = glob.glob('src/pages/**/*.astro', recursive=True)
dup = 'const base = import.meta.env.BASE_URL;\nconst base = import.meta.env.BASE_URL;'
single = 'const base = import.meta.env.BASE_URL;'

for filepath in pages:
    with open(filepath, 'r') as f:
        content = f.read()
    if dup in content:
        content = content.replace(dup, single)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed duplicate in {filepath}")

print("Done!")


files_changes = {
    'src/pages/index.astro': [
        ("import '../styles/global.css';", "import '../styles/global.css';\nconst base = import.meta.env.BASE_URL;"),
        ('href="/favicon.svg"', 'href={`${base}favicon.svg`}'),
        ('href="/blogs"', 'href={`${base}blogs`}'),
        ('src="/hero-image.png"', 'src={`${base}hero-image.png`}'),
        ('href={`/work/${job.slug}`}', 'href={`${base}work/${job.slug}`}'),
        ('href={`/award/${p.slug}`}', 'href={`${base}award/${p.slug}`}'),
        ('href={`/project/${p.slug}`}', 'href={`${base}project/${p.slug}`}'),
        ('href="/projects"', 'href={`${base}projects`}'),
    ],
    'src/pages/projects/index.astro': [
        ("import '../../styles/global.css';", "import '../../styles/global.css';\nconst base = import.meta.env.BASE_URL;"),
        ('href="/favicon.svg"', 'href={`${base}favicon.svg`}'),
        ('href="/"', 'href={base}'),
        ('src={project.thumb}', 'src={`${base}${project.thumb.slice(1)}`}'),
        ('href={`/project/${project.slug}`}', 'href={`${base}project/${project.slug}`}'),
    ],
    'src/pages/blogs/index.astro': [
        ("import '../../styles/global.css';", "import '../../styles/global.css';\nconst base = import.meta.env.BASE_URL;"),
        ('href="/favicon.svg"', 'href={`${base}favicon.svg`}'),
        ('href="/"', 'href={base}'),
        ('href={`/blog/${blog.slug}`}', 'href={`${base}blog/${blog.slug}`}'),
    ],
    'src/pages/project/[slug].astro': [
        ("import '../../styles/global.css';", "import '../../styles/global.css';\nconst base = import.meta.env.BASE_URL;"),
        ('href="/favicon.svg"', 'href={`${base}favicon.svg`}'),
        ('href="/projects"', 'href={`${base}projects`}'),
        ('href="/"', 'href={base}'),
        ('src={img}', 'src={`${base}${img.slice(1)}`}'),
    ],
    'src/pages/award/[slug].astro': [
        ("import '../../styles/global.css';", "import '../../styles/global.css';\nconst base = import.meta.env.BASE_URL;"),
        ('href="/favicon.svg"', 'href={`${base}favicon.svg`}'),
        ('href="/"', 'href={base}'),
        ('src={img}', 'src={`${base}${img.slice(1)}`}'),
    ],
    'src/pages/work/[slug].astro': [
        ("import '../../styles/global.css';", "import '../../styles/global.css';\nconst base = import.meta.env.BASE_URL;"),
        ('href="/favicon.svg"', 'href={`${base}favicon.svg`}'),
        ('href="/"', 'href={base}'),
    ],
    'src/pages/blog/[slug].astro': [
        ("import '../../styles/global.css';", "import '../../styles/global.css';\nconst base = import.meta.env.BASE_URL;"),
        ('href="/favicon.svg"', 'href={`${base}favicon.svg`}'),
        ('href="/"', 'href={base}'),
        ('href="/blogs"', 'href={`${base}blogs`}'),
    ],
}

for filepath, changes in files_changes.items():
    with open(filepath, 'r') as f:
        content = f.read()
    for old, new in changes:
        count = content.count(old)
        content = content.replace(old, new)
        print(f"{filepath}: '{old[:40]}' -> replaced {count}x")
    with open(filepath, 'w') as f:
        f.write(content)

print("Done!")
