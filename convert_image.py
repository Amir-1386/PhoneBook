from PIL import Image, ImageChops, ImageDraw

def convert(input_image, output_image):
    im = Image.open(input_image).convert('RGBA')
    width, height = im.size
    
    x = abs(width - height) / 2
    if width > height:
        im = im.crop((x, 0, width - x, height))
    else:
        im = im.crop((0, x, width, height - x))
    im = im.resize((400, 400))
    
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)
    im.save(output_image)

