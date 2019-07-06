################################################################################################
from PIL import Image, ImageDraw
import time
import os
import hashlib
import imagehash


def compare_images(input_image, output_image):
  # compare image dimensions (assumption 1)
  if input_image.size != output_image.size:
    return False

  rows, cols = input_image.size

  # compare image pixels (assumption 2 and 3)
  for row in range(rows):
    for col in range(cols):
      input_pixel = input_image.getpixel((row, col))
      output_pixel = output_image.getpixel((row, col))
      if input_pixel != output_pixel:
        return False

  return True

print('*** Program Started ***')

# image_font_path = 'imagepath_input = '/home/conquistador/code/github/python-01-utilities/image/fonts/'
image_path_input = '/Users/mwaqar/shenanigans/CSE_Puzzle_Challenge_12/'
image_path_output = '/Users/mwaqar/shenanigans/CSE_Puzzle_Challenge_12/out/'
image_name_input = 'flags_en.png'

######################################################

im = Image.open(image_path_input + image_name_input)
im_width, im_height = im.size
print('im.size', im.size)

######################################################
size_of_one_flag=10;

w=(im_width/37)
h=(im_height/37)

###################################################### LOOPER

# for j in range(0,37):
#     for i in range(0,37):
#         print ("j: ", j," i: ",i)
#         print (w*i, h*j, w+w*i ,h+h*j)
#         print ("----")
#         # im = im.crop((100*j,100*i ,100+100*i,100+100*j))  # (left, upper, right, lower)-tuple.
#         im2 = im.crop((w*i, h*j, w+w*i ,h+h*j))
#
#         image_name_output = str(j)+"_"+str(i)+'.png'
#         im2.save(image_path_output + image_name_output)
#         del(im2)
#         print('im.size', im.size)
#         # time.sleep(10)


#######################################..
############### Left half of the image
# im = im.crop((0, 0, (im_width/37) ,(im_height/37)))  # (left, upper, right, lower)-tuple.
# im = im.crop((w*0, h*1, w+w*0 ,h+h*1))
# image_name_output = 'flags_en_t1.png'
# im.save(image_path_output + image_name_output)
# print('im.size', im.size)

#################################


# for or_i in os.listdir("out/"):
# uni=0;
# UNI=[]
# for or_j in range(0,37):
#     print ("or_j: ", or_j)
#     UNI.append(uni)
#     uni=0
#     for or_i in range(1):
#         print ("or_i: ", or_i)
#         for j in range(0,37):
#             # print ("j: ", j)
#             for i in range(0,37):
#                 original = Image.open("out/"+str(or_j)+"_"+str(or_i)+'.png')
#                 possible_duplicate = Image.open("out/"+str(j)+"_"+str(i)+'.png')
#
#                 if (compare_images(original, possible_duplicate)==True):
#                     uni= uni+1
#
# print("COUNT: ",uni)
# print(UNI)



#############3 Many counter
Uni=[]
Uni_hash=[]
no=0
no1=0
Uni.append("out/0_0.png")

image_file = Image.open("out/0_0.png")
# print (str(imagehash.dhash(image_file)))
Uni_hash.append(str(imagehash.dhash(image_file)))

for u in Uni:
    for i in range(37):
        print ("i: ",i)
        for j in range(37):
            # print ("j: ",j)
            original = Image.open(u)
            pd="out/"+str(j)+"_"+str(i)+".png"
            possible_duplicate = Image.open(pd)
            if (compare_images(original, possible_duplicate)==True):
                pd_hash = (str(imagehash.dhash(possible_duplicate)))
                if pd_hash not in Uni_hash:
                    Uni.append(possible_duplicate)
                    print (Uni)
                    print ("============= appended")
                    no=no+1
                    print ("no: ",no)
            else:
                print ("++++++")
                no1=no1+1
            print ("no: ",no)
            print ("no1: ",no1)
            del(original)
            del(possible_duplicate)

    print("TOTAL UNIQUE BOIS: ", len(Uni))
print(Uni)
### HASHING
# # Loading an image file into memory and calculating it's hash value.
# image_file = open('data/cat_grumpy_orig.png').read()
# hashlib.md5(image_file).hexdigest()
#     # '3e1f6e9f2689d59b9ed28bcdab73455f'

print('*** Program Ended ***')
