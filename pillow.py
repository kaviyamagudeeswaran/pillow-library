from PIL import Image
filename="flower.jpeg"
img=Image.open(filename)
img=img.rotate(angle=60,expand=True,fillcolor="pink",center=(150,150))
img.show()
print(img)
