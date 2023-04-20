import qrcode

#criar um codigo QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# adcionar dados ao codigo QR

data = "https://www.youtube.com/"
qr.add_data(data)
qr.make(fit=True)

#Criar iamgem do codigo QR

img = qr.make_image(fill_color="black", back_color="white")

# salvar imagem em um arquivo

img.save("qr_code.png")