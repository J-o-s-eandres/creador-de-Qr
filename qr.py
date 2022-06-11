import qrcode #importamos la libreria a utilizar

input = 'direccion ' #el input (o cualquier nombre que deseen) sera la direccion a donde queremos ingresar mediante el qr

qr= qrcode.QRCode(version=5,box_size=10,border=5)#version para el tamaño , box_size para cantidad de pixeles y border para el borde del qr

qr.add_data(input) #le pasamos la data que queremos que se muestre al ser escaneado el qr

qr.make(fit=True)#crear el qr


img= qr.make_image(fill='black',back_color='white')#crear la imagen del qr, fill para la forma del codigo qr en la imagen,  back para el fondo

img.save('nombre.jpg')#guardamos la imagen en la carpeta donde estamos