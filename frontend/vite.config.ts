import { defineConfig } from 'vite'

export default defineConfig(({ command }) => ({
  base: command === 'serve' ? '/' : '/blog-demo/',  // <-- Add your repo name here
  server: {
    host: '0.0.0.0',
    port: 5173,
  },
}))