import qrcode as qr
img = qr.make("https://www.youtube.com")
img.save("youtube QRcode.png")