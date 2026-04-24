import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  output: 'static',
  site: 'https://ramysandy.github.io',
  base: '/shreeram_portfolio',
  build: {
    assets: 'assets'
  }
});
