# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    images_link='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07804323'
    image_urls=urllib.request.urlopen(images_link).read().decode()
    
    if not os.path.exists('not-hotdog'):
        os.makedirs('not-hotdog')
    
    pic_num=898
    
    for i in image_urls.split('\n'):
        print(i)
        try:
            urllib.request.urlretrieve(i,"not-hotdog/"+str(pic_num)+'.jpg')
            pic_num+=1
        except Exception as e:
            print(str(e))
