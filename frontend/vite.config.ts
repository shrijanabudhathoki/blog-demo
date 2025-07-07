// vite.config.ts
import { defineConfig } from 'vite'

export default defineConfig({
  base: '/blog-demo/',  // <-- Add this: your repo name with slashes
  server: {
    host: '0.0.0.0',
    port: 5173,
  },
})