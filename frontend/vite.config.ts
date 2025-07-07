import { defineConfig } from 'vite'

export default defineConfig(({ command }) => ({
  base: command === 'serve' ? '/' : '/blog-demo/', 
  server: {
    host: '0.0.0.0',
    port: 5173,
  },
}))