from PIL import Image
from PIL import ImageFilter

with Image.open("perrito.png") as pic_original:
    pic_original.show()

    pic_gray = pic_original.convert("L")
    pic_gray.save("perrito2.png")
    pic_gray.show()


    pic_up = pic_gray.transpose(Image.ROTATE_90)
    pic_up.save("Perrito_de_lado.png")
    pic_up.show()

    print("tamaño: ", pic_original.size)
    print("formato: ", pic_original.format)
    print("tipo: ", pic_original.mode)