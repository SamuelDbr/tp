#-*- coding: utf-8 -*-

######  #     #   ###     #       #     ######
#       ##    #  #   #                  #
#       # #   #   #      ##      ##     #
#####   #  #  #    #      #       #     #####
#       #   # #     #     #       #     #
#       #    ##  #   #    #       #     #
######  #     #   ###   #####   #####   ######

# 2017-2018
# ---------

import sys
import random

from PIL.Image import *


from effets_photom import *
from effets_geom import *
from filtrages import *


# /*!
#  \file tpimage.py
#  \author Pierre Tellier
#  \date  16/10/2017
#  \brief programme principal : test des fonctionnalités de manipulation d'image
# */



def main():
    argc=len(sys.argv)
    if argc<3 :
        print "usage : ", sys.argv[0], " fichier.png fichier.png"
        return
    
    random.seed()  #initialisation du générateur pseudo-aléatoire

    img1=open(sys.argv[1])
    (xsize,ysize) = img1.size
    print "Lecture OK ( H =", ysize, " L =", xsize,")"
    Image.show(img1)

    img2 = inversion_videoNB(img1, xsize, ysize)

    Image.show(img2)
    img2.save(sys.argv[2])

    img1.close()
    img2.close()


if __name__ == "__main__":
    main()





