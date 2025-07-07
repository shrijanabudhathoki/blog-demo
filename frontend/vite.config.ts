import { defineConfig } from 'vite'

export default defineConfig(({ command }) => ({
  base: command === 'serve' ? '/' : '/blog-demo/', // replace 'blog-demo' with your repo name
  server: {
    host: '0.0.0.0',
    port: 5173,
  },
}))