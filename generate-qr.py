#!/usr/bin/env python3
import qrcode

# URL de la landing page de Talleria
url = "https://kaysersozes.github.io/talleria/"

# Crear el código QR con configuración optimizada para impresión
qr = qrcode.QRCode(
    version=1,  # Tamaño del QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Máxima corrección de errores (30%)
    box_size=10,  # Tamaño de cada caja en píxeles
    border=4,  # Borde mínimo requerido
)

qr.add_data(url)
qr.make(fit=True)

# Crear imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar en alta resolución para impresión
img.save("talleria-qr.png")
print("✅ Código QR generado: talleria-qr.png")
print(f"📱 URL: {url}")
print("🖨️  Listo para imprimir en alta calidad")
