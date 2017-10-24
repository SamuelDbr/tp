from PIL import Image 

def inversion_videoNB(img, xs, ys) :
    res = Image.new("L",img.size,"black")
    for y in range (0,ys):
        for x in range (0,xs):
            col=img.getpixel ((x,y))
            res.putpixel((x,y),255-col)
    return res


def plusClairNB(img,  xs,  ys) :
    res = Image.new("L",img.size,"black")
    #
    return res

def deriv1xNB(img,  sx,  sy) :
    res = Image.new("L",img.size,"black")
    #
    return res




