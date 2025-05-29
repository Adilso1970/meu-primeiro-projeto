// frontend/src/App.jsx
import { useEffect, useState } from 'react';
import { getHealth } from './services/api';

function App() {
  const [health, setHealth] = useState('carregando…');
  const [error, setError] = useState(null);

  useEffect(() => {
    getHealth()
      .then(text => setHealth(text))
      .catch(err => setError(err.message));
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: 'sans-serif' }}>
      <h1>Health check do Back-end</h1>
      {error
        ? <p style={{ color: 'red' }}>Erro: {error}</p>
        : <p>Resposta: <strong>{health}</strong></p>
      }
    </div>
  );
}

export default App;
