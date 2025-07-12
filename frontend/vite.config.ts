import { defineConfig } from 'vite'

const base = process.env.VITE_BASE_PATH || '/';
export default defineConfig(({ command }) => ({
  base,
  server: {
    host: '0.0.0.0',
    port: 5173,
  },
}))
