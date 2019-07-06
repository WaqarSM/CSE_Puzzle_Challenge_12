################################################################################################
from PIL import Image, ImageDraw
import time
import os
import hashlib
import imagehash

def is_in_dic(input_image_name, table):
    # unique_table =['41162b290c290800', '12960e080c0c0800', '203e064a080c0800', '08071e080c0c0800', '480e0f2c080c0800', '11930e090c0c0800', '010693090c090800', '091e0b090c090800', '02160e080c0c0800', '081e072c080c0800', '22360e480c0c0800', '180e2f0c080c0800', '081e060a080c0800', '42162e280c2c0800', '0016872c080c0800', '28970e080c0c0800', '48073e280c2c0800', '2036074c080c0800', '41132e290c2c0800', '02069e080c0c0800', '28079e080c0c0800', '28270e480c0c0800', '01161b090c090800', '1a0c082f06080c00', '21360b490c090800', '4016272c082c0800', '401e362a082c0800', '109e060a080c0800', '01131e090c0c0800', '0000000000000000', '21330e490c0c0800', '260c080e1c0c0800', '2d080c0a0c0c0800', '091b0e090c0c0800', '01060b090c090800', '1096070c080c0800']
    img = Image.open(input_image_name)
    if str(imagehash.dhash(img)) in table:
        return True
    del(img)
    return False

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
#
# Uni=[]
# Uni_hash=[]
# no=0
# no1=0
# Uni.append("out/0_0.png")
#
# image_file = Image.open("out/0_0.png")
# # print (str(imagehash.dhash(image_file)))
# Uni_hash.append(str(imagehash.dhash(image_file)))
#
#
# for i in range(37):
#     # print ("i: ",i)
#     for j in range(37):
#         pd="out/"+str(j)+"_"+str(i)+".png"
#         img = Image.open(pd)
#         Uni_hash.append(str(imagehash.dhash(img)))
#         del(img)
#
#
# mylist = Uni_hash
# unique = [x for i, x in enumerate(mylist) if i == mylist.index(x)]
#
# print(Uni_hash)
# print("\n\nUnique: \n")
# print(unique)
# print("Size: ", len(unique))
#


##############
unique_table =['41162b290c290800', '12960e080c0c0800', '203e064a080c0800', '08071e080c0c0800', '480e0f2c080c0800', '11930e090c0c0800', '010693090c090800', '091e0b090c090800', '02160e080c0c0800', '081e072c080c0800', '22360e480c0c0800', '180e2f0c080c0800', '081e060a080c0800', '42162e280c2c0800', '0016872c080c0800', '28970e080c0c0800', '48073e280c2c0800', '2036074c080c0800', '41132e290c2c0800', '02069e080c0c0800', '28079e080c0c0800', '28270e480c0c0800', '01161b090c090800', '1a0c082f06080c00', '21360b490c090800', '4016272c082c0800', '401e362a082c0800', '109e060a080c0800', '01131e090c0c0800', '0000000000000000', '21330e490c0c0800', '260c080e1c0c0800', '2d080c0a0c0c0800', '091b0e090c0c0800', '01060b090c090800', '1096070c080c0800']
dic=[]

for i in range(37):
    print ("i: ",i)
    for j in range(37):
        pd="out/"+str(j)+"_"+str(i)+".png"
        if is_in_dic(pd, unique_table):
            dic.append(pd)
            unique_table.remove(str(imagehash.dhash(Image.open(pd))))

print (dic)
print("Size: ", len(dic))

dic = ['out/0_0.png', 'out/1_0.png', 'out/2_0.png', 'out/3_0.png', 'out/5_0.png', 'out/6_0.png', 'out/7_0.png', 'out/8_0.png', 'out/10_0.png', 'out/11_0.png', 'out/12_0.png', 'out/17_0.png', 'out/22_0.png', 'out/26_0.png', 'out/2_1.png', 'out/21_1.png', 'out/23_1.png', 'out/30_1.png', 'out/0_2.png', 'out/10_2.png', 'out/20_2.png', 'out/31_2.png', 'out/34_4.png', 'out/11_6.png', 'out/13_6.png', 'out/14_6.png', 'out/31_7.png', 'out/5_11.png', 'out/13_11.png', 'out/36_17.png', 'out/13_20.png', 'out/34_23.png', 'out/4_29.png', 'out/14_32.png', 'out/30_33.png', 'out/21_34.png']


# unique =['41162b290c290800', '12960e080c0c0800', '203e064a080c0800', '08071e080c0c0800', '480e0f2c080c0800', '11930e090c0c0800', '010693090c090800', '091e0b090c090800', '02160e080c0c0800', '081e072c080c0800', '22360e480c0c0800', '180e2f0c080c0800', '081e060a080c0800', '42162e280c2c0800', '0016872c080c0800', '28970e080c0c0800', '48073e280c2c0800', '2036074c080c0800', '41132e290c2c0800', '02069e080c0c0800', '28079e080c0c0800', '28270e480c0c0800', '01161b090c090800', '1a0c082f06080c00', '21360b490c090800', '4016272c082c0800', '401e362a082c0800', '109e060a080c0800', '01131e090c0c0800', '0000000000000000', '21330e490c0c0800', '260c080e1c0c0800', '2d080c0a0c0c0800', '091b0e090c0c0800', '01060b090c090800', '1096070c080c0800']
