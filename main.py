import qrcode
import os

qr = qrcode.QRCode(box_size=10)

data = input('Введите путь для сохранения QR кода: ')
filename = input('Введите имя файл: ')
link = input('Ссылка на страницу с которой нужно связать: ')

qr.add_data(link)
image = qr.make_image()

os.chdir(data)
image.save(filename)
