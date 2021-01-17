from PIL import Image
import matplotlib.pyplot as plt
import os
# def getFormt(path):
#     im = Image.open(path)
#     return (im.format, im.size[0],im.size[1])

def getFormt(img):
    return (img.format, img.size[0],img.size[1])

#print(getFormt("/Users/ma/Pictures/rail/1.png"))

def merge(path,column):
    images=getImage(path)
    num=len(images)
    fmt, width, height = getFormt(images[0])

    if num%column==0:
        row = num // column
    else:
        row = (num // column)+1

    target = Image.new('RGBA', (width * column+(2*column-1), height * row+2*(row-1)))  # result is column*row
    for i in range(column):
        for j in range(row):
            if (j*column+i)>(len(images)-1):
                break
            img=images[j*column+i]
            print(j*column+i,img.split())
            fmt, width, height = getFormt(img)
            if(len(img.split())==4):
              target.paste(img, (i*width+i*2,j*height+j*2, i*width+i*2+width, j*height+j*2+height),mask=img.split()[3])
            else:
                target.paste(img, (
                i * width + i * 2, j * height + j * 2, i * width + i * 2 + width, j * height + j * 2 + height))

    quality_value = 100
    target.save(os.path.join(path, "out_put."+fmt)  , quality=quality_value)




def getImage(path):
    pictures = ("png", "PNG", "jpg", "JPG")
    images = []
    for root, dirs, files in  os.walk(path):
        for name in files:
            if name.endswith(pictures):
              images.append(Image.open(os.path.join(root, name)))
    return images


#getImage("/Users/ma/Pictures/rail")
merge("~/Pictures/my_pics",4)#merge(path,columnNums)




