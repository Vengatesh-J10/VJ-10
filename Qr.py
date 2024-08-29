import qrcode
import image
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data="https://github.com/Vengatesh-J10"


qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill="black",back_color="white")
image.save("test.png")