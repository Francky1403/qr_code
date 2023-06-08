import qrcode

code_QR = input("entrez le texte ou lien pour creer votre code QR\n")
nom_QR = input("entrez le nom de votre image en .png ou .jpg\n")

code_qr = qrcode.QRCode(
    version=3,
    box_size=5,
    border=5
)

code_qr.add_data(code_QR)
code_qr.make(fit=True)
img = code_qr.make_image(fill_color= 'white', back_color = 'black')
img.save(nom_QR)