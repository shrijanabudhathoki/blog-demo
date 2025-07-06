// https://vite.dev/config/
// vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  base: '/blog-demo/',
  plugins: [react()],
})