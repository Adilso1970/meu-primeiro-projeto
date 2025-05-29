export const api = {
  getHealth: () => fetch(import.meta.env.VITE_API_URL + '/health'),
  // outros métodos...
}
