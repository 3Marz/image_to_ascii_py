import sys
from PIL import Image, ImageOps

img_path = sys.argv[1]

ascii_range =  " .:-=+*#%@"
#ascii_range = "$$$$@@@@BBBB%%%%8888&&&&WWWWMMMM####****oooaaaahhhkkkkbbbbddddppppqqqwwwwmmmZZZZOOOO000QQQLLLLCCCJJJJUUUUYYYYXXXXzzzccccvvvvuuuunnnnxxxrrrrjjjjfffftttt///||||(((()))1111{{{{}}}}[[[[]]]????----____++++~~~~<<<>>>>iiii!!!!lllIIII;;;;::::,,,,^^^````''''...    "[::-1]
#print(len(ascii_range))

im = Image.open(img_path)

sx = 0
sy = 0

if len(sys.argv) > 3:
	sx = int(sys.argv[2])
	sy = int(sys.argv[3])
else:
	sx = 90
	sy = 40
	
size = (sx, sy)

im = im.resize(size)
im = im.convert("L")

ascii_img = ""

for y in range(im.size[1]):
	for x in range(im.size[0]):
		pix = im.getpixel((x, y))

		#ascii_img += ascii_range[pix]

		if pix <= 25:
			ascii_img += ascii_range[0]
		elif pix <= 50:
			ascii_img += ascii_range[1]
		elif pix <= 75:
			ascii_img += ascii_range[2]
		elif pix <= 100:
			ascii_img += ascii_range[3]
		elif pix <= 125:
			ascii_img += ascii_range[4]
		elif pix <= 150:
			ascii_img += ascii_range[5]
		elif pix <= 175:
			ascii_img += ascii_range[6]
		elif pix <= 200:
			ascii_img += ascii_range[7]
		elif pix <= 225:
			ascii_img += ascii_range[8]
		else:
			ascii_img += ascii_range[9]



	ascii_img += "\n"


print(ascii_img)