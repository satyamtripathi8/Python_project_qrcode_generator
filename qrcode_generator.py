import qrcode 
import img  # as ---> alias
qr=qrcode.QRCode(
    version=6,
    box_size=8,
    border=3
)
data = '''
Name: Satyam Tripathi
Age: 19
College: JIET(Jodhpur)(1st Year)
Branch: CSC(AIML)'''
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(
    fill = "black",back = "white"
)
img.save("Satyam.png")