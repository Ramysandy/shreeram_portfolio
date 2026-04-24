# Shreeram Portfolio

A premium static portfolio built with Astro and Tailwind CSS using the **2026 Vintage Broadsheet** aesthetic.

## Setup

```bash
npm install
npm run dev      # Development server at http://localhost:4321
npm run build    # Static build → dist/
npm run preview  # Preview the build
```

## Deployment (GitHub Pages — Free Tier)

1. Push to a GitHub repo
2. Go to **Settings → Pages**
3. Set Source to **GitHub Actions**
4. Create `.github/workflows/deploy.yml` (see below)

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist/
      - uses: actions/deploy-pages@v4
```

## Structure

```
src/
  pages/index.astro     # Full single-page layout
  styles/global.css     # Tailwind base + custom print styles
public/
  favicon.svg
tailwind.config.mjs
astro.config.mjs
```
