# Script para generar la imagen automáticamente
# Requiere instalar html2canvas o puppeteer

# Con Node.js y Puppeteer:
# npm install puppeteer

const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Configurar viewport exacto
  await page.setViewport({ width: 1200, height: 630 });
  
  // Cargar el HTML
  await page.goto(`file://${__dirname}/og-image-generator.html`);
  
  // Esperar que cargue completamente
  await page.waitForTimeout(1000);
  
  // Capturar screenshot
  await page.screenshot({ 
    path: 'og-image.jpg', 
    quality: 90,
    type: 'jpeg'
  });
  
  await browser.close();
  console.log('Imagen generada: og-image.jpg');
})();