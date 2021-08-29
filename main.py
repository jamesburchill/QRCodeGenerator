import qrcode
URL = input('Enter a URL')
img = qrcode.make(URL)
# type(img)  # qrcode.image.pil.PilImage
fname = input('Enter a filenmame')
img.save(fname + ".png")