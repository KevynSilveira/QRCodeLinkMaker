# pip install qrcode
import qrcode

image = qrcode.make("https://github.com/KevynSilveira") # Controi o qrcode
image.save("qr_code_github.png") # Salva ele