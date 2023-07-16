from PIL import Image, ImageDraw, ImageFont

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = '#D0063E'
GREEN = '#33995B'
BLUE = '#557BC3'
WOW = '#CF9877'
EL = '#B3C5A5'
EL1 = '#679C63'
EL2 = '#5F8675'
EL3 = '#4F8587'

W, H = (200, 200)
RW, RH = (50, 50)
CELLS = 8


canvas = Image.new("RGB", (W, H), EL)
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype('arial.ttf', size=15)

draw.ellipse(xy=(149, 0, 199, 50), fill=EL1, width=4)
draw.ellipse(xy=(75, 75, 125, 125), fill=EL2, width=4)
draw.ellipse(xy=(0, 149, 50, 199), fill=EL3, width=4)

TEXT = 'PYTHON'
draw.text((65, 10), TEXT, font=font)

canvas.save('image_1.png', 'PNG')
canvas.show()


canvas = Image.new("RGB", (CELLS * RW, CELLS * RH), WOW)
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype('arial.ttf', size=15)

for x in range(CELLS):
    for y in range((x+1) % 2, CELLS, 2):
        draw.rectangle((x * RW, y * RW, (x + 1) * RW - 1, (y + 1) * RW - 1), fill=WHITE)

canvas.save('image_2.png', 'PNG')
canvas.show()


canvas = Image.new("RGB", (W, H), WHITE)
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype('arial.ttf', size=15)

draw.line((0, 0, W, H), fill=WHITE, width=5)
draw.line((W, 0, 0, H), fill=WHITE, width=5)

draw.rectangle((0, 0, RW, RH), fill=RED)
draw.rectangle((75, 75, 125, 125), fill=GREEN)
draw.rectangle((W - RW, H - RH, W, H), fill=BLUE)

draw.arc(xy=(15, 40, 165, 190), start=40, end=220, fill=WOW, width=4)
draw.polygon((W // 2, 0, 0, H, W, H), fill=WHITE, outline=WOW)

canvas.save('image_3.png', 'PNG')
canvas.show()
