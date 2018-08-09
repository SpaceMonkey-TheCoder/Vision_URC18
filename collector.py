import numpy.core.multiarray
import cv2
import numpy as np
import urllib.request
import os

def new_images():
    pos_im = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09416076'
    pos_im_url = urllib.request.urlopen(pos_im).read().decode()

    if not os.path.exists('neg_new'):
        os.makedirs('neg_new')

    n = 1883

    for i in pos_im_url.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg_new/"+str(n)+'.jpg')
            img = cv2.imread("neg_new/"+str(n)+'.jpg', cv2.IMREAD_GRAYSCALE)
            ri = cv2.resize(img, (400,400))
            cv2.imwrite("neg_new/"+str(n)+'.jpg', ri)
            n += 1

        except Exception as e:
            print(str(e))

def create_info():
    for file_type in ['neg_new']:

        for img in os.listdir(file_type):
            if file_type == 'neg_new':
                line = file_type+'/'+img+'\n'
                with open('bg_new.txt','a') as f:
                    f.write(line)
            elif file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)

def im_res():
    img = cv2.imread('pos/22.jpg')
    img = cv2.resize(img, (50,50))
    cv2.imwrite("pos/22.jpg", img)

#im_res()
create_info()
#new_images()
