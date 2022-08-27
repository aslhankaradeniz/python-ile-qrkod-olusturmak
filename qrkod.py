"""
import qrcode
img=qrcode.make("manyakişko") #bura da qr kod a çevirmek istediğimiz eklenir
img.save("qr.png")#qr kodunu resim formatında kaydeder
"""
import qrcode
code= qrcode.QRCode(
    version=4,# boyut tanımlar 1'den 40'a kadar yapılabilir
    box_size=50,#piksel olarak boyut belirler
    border=3#kenar boşluk

)
code.add_data("https://drive.google.com/file/d/1p9KderddX5T6HFZeANCwMrjx6oW7NW7-/view?usp=sharing")
code.make(fit=True)#version'a göre boyuta sığması için True dedik
image=code.make_image(fill_color="black",back_color="white")
image.save("qr.png")