import { defineConfig } from 'vite'

const base = process.env.VITE_BASE_PATH || '/';
export default defineConfig(({ command }) => ({
  server: {
    base,
    host: '0.0.0.0',
    port: 5173,
  },
}))
