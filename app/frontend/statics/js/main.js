const form = document.getElementById('calc-form');
const resultadoDiv = document.getElementById('resultado');
const themeToggle = document.getElementById('theme-toggle');
const exportarBtn = document.getElementById('btn-exportar');
const selectFormato = document.getElementById('formato-export');

// Detectar base URL (útil para localhost o ngrok)
const apiBase = window.location.origin;

// Guardar última data generada
let ultimaData = null;

// Cambio de tema
themeToggle.addEventListener('click', () => {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', newTheme);
});

// Envío del formulario de cálculo
form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const data = {
    capital_inicial: parseFloat(document.getElementById('capital').value),
    tasa_interes_anual: parseFloat(document.getElementById('tasa').value),
    anios: parseInt(document.getElementById('anios').value),
    tipo_capitalizacion: document.getElementById('capitalizacion').value,
    aportes_periodicos: document.getElementById('aportes').value
      ? parseFloat(document.getElementById('aportes').value)
      : null,
    cada_cuanto_aporta: document.getElementById('frecuencia').value || null
  };

  try {
    const response = await fetch(`${apiBase}/api/v1/calcular`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Error en la solicitud: ${errorText}`);
    }

    const result = await response.json();
    console.log(result);
    ultimaData = data;

    resultadoDiv.innerHTML = `
      <p><strong>Capital Final:</strong> ${result.capital_final}</p>
      <p><strong>Ganancia Total:</strong> ${result.ganancia_total}</p>
    `;
  } catch (error) {
    resultadoDiv.innerHTML = `<p style="color:red;">Error: ${error.message}</p>`;
    console.error('Error al realizar la solicitud:', error);
  }
});

// Exportar resultado
exportarBtn.addEventListener('click', async () => {
  console.log(ultimaData)
  if (!ultimaData) {
    resultadoDiv.innerHTML = '<p style="color:red;">Error: Primero debes realizar un cálculo.</p>';
    return;
  }

  const formato = selectFormato.value;
  const query = new URLSearchParams({ descargar: true }).toString();

  try {
    const response = await fetch(`${apiBase}/api/v1/calcular/${formato}?${query}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(ultimaData)
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Error al exportar: ${errorText}`);
    }

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `resultado.${formato === 'excel' ? 'xlsx' : 'csv'}`;
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
  } catch (err) {
    resultadoDiv.innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
    console.error('Error al exportar:', err);
  }
});
