from PIL import Image
import glob ,os

#m = Image.init()

size = 128,128

for infile in glob.glob("*.png"):
    file,ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbanil(size)
    im.save(file + ".thumbnail","JPEG")

print("exit")