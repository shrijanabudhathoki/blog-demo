import { defineConfig } from 'vite'

export default defineConfig(({ command }) => ({
  const base = process.env.VITE_BASE_PATH || '/';
  server: {
    base,
    host: '0.0.0.0',
    port: 5173,
  },
}))
