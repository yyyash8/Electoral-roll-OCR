#!/usr/bin/env python
# coding: utf-8

# [ ]:


from PIL import Image
from pytesseract import image_to_string
import pytesseract
import numpy as np
import pandas as pd
import PIL
import cv2


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# **UNINSTALL AND REINSTALL**
# 
# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-20180621.exe
# 
# 
# Uninstall previously stalled tesseract application and reinstall it with above link.

# [ ]:


#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


# **ORIGINAL**

# [ ]:


im = Image.open("C:/Users/yyyas/Desktop/91-120/AC0420091_Page_01.jpg")
im


# **Rescaling**

# [ ]:


basewidth = 1700
wpercent = (basewidth / float(im.size[0]))
size = int((float(im.size[1]) * float(wpercent)))
imz = im.resize((basewidth, size), PIL.Image.ANTIALIAS)
imz


# **Making Image Binary**

# [ ]:


im = cv2.bilateralFilter(np.array(imz,dtype=np.uint8),9,75,75)
#imb = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#ims  = Image.fromarray(imb)   


# [ ]:


im = cv2.adaptiveThreshold(np.array(imz,dtype=np.uint8), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 11)
im = Image.fromarray(im)
im


# **Things required to be extracted**
# 
# 1. Vidhan Sabha name
# 2. Part No/Bhag Sankhya
# 3. Details of part and polling area/
# 4. No. and name of polling station
# 5. Male/Female/Total
# 6. File Name

# [ ]:


crop_rectangle_vs = (705, 110, 1100, 202)
cropped_im_vs = im.crop(crop_rectangle_vs)
crop_rectangle_bs = (1462, 110, 1550, 205)
cropped_im_bs = im.crop(crop_rectangle_bs)
crop_rectangle_mg = (830, 737, 1010, 770)
cropped_im_mg = im.crop(crop_rectangle_mg)
crop_rectangle_psn = (159, 1550, 1050, 1630)
cropped_im_psn = im.crop(crop_rectangle_psn)
crop_rectangle_psa = (170, 1670, 1125, 1725)
cropped_im_psa = im.crop(crop_rectangle_psa)
crop_rectangle_male = (820, 1965, 955, 2050)
cropped_im_male = im.crop(crop_rectangle_male)
crop_rectangle_fem = (1020, 1965, 1175, 2050)
cropped_im_fem = im.crop(crop_rectangle_fem)
crop_rectangle_tot = (1400, 1965, 1565, 2050)
cropped_im_tot = im.crop(crop_rectangle_tot)
cropped_im_vs


# [ ]:


import glob
# To put only first page of pdfs, we will put all jpgs path whose file name is ending with '-01.jpg'
onlyfiles = glob.glob('C:/Users/yyyas/Desktop/91-120/*_01.jpg')

# We require file name for every file our code reads. To read that we will put file name from the path.
# For example, when I read onlyfiles list I have created above, it shows paths such as
# 'C:/Users/yyyas/Downloads/AC0020001\\\ **AC0020001**-01.jpg'
# 
# Here we require highlighted text. To get that we will split the string with respect to '\\\'. Our O/P will be a list as follows.
# 
# ['C:/Users/yyyas/Downloads/AC0020001','**AC0020001**-01.jpg']
# 
# Then we will take second part of the list('**AC0020001**-01.jpg') and split it by '-'. Our O/P will be a list as follows.
# 
# ['**AC0020001**',01.jpg']
# 
# Here first item of the list is our requirement.



def img_to_txt(x):
    s = x.split('\\')
    s = s[1].split("-")[0]
    im = Image.open(x)
    basewidth = 1700
    wpercent = (basewidth / float(im.size[0]))
    size = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((basewidth, size), PIL.Image.ANTIALIAS)
    im = cv2.bilateralFilter(np.array(im,dtype=np.uint8),9,75,75)
#    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = cv2.adaptiveThreshold(np.array(im,dtype=np.uint8), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 11)
    im = Image.fromarray(im)
    cropped_im_vs = im.crop(crop_rectangle_vs)
    c_vs = image_to_string(cropped_im_vs,config='-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM --psm 6')
    cropped_im_bs = im.crop(crop_rectangle_bs)
    c_bs = image_to_string(cropped_im_bs,config='-c tessedit_char_whitelist=0123456789 -psm 6')
    cropped_im_psn = im.crop(crop_rectangle_psn)
    c_psn = image_to_string(cropped_im_psn,config='--psm 6')
    cropped_im_psa = im.crop(crop_rectangle_psa)
    c_psa = image_to_string(cropped_im_psa,config='-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM --psm 6')
    cropped_im_male = im.crop(crop_rectangle_male)
    c_male = image_to_string(cropped_im_male,config='-c tessedit_char_whitelist=0123456789 --psm 6')
    cropped_im_fem = im.crop(crop_rectangle_fem)
    c_fem = image_to_string(cropped_im_fem,config='-c tessedit_char_whitelist=0123456789 --psm 6')
    cropped_im_tot = im.crop(crop_rectangle_tot)
    c_tot = image_to_string(cropped_im_tot,config='-c tessedit_char_whitelist=0123456789 --psm 6')
    return c_vs,c_bs,c_psn,c_psa,s,c_male,c_fem,c_tot



vidhnsbha = []
bhag_snkhya = []
PS_name = []
PS_add = []
file_name = []
male = []
female = []
total = []
for i in onlyfiles:
    a,b,d,e,s,m,f,o = img_to_txt(i)
    vidhnsbha.append(a)
    bhag_snkhya.append(b)
    PS_name.append(d)
    PS_add.append(e)
    file_name.append(s)
    male.append(m)
    female.append(f)
    total.append(o)




import numpy as np
front_pange = pd.DataFrame(np.column_stack([vidhnsbha, bhag_snkhya,PS_name,PS_add,male,female,total,file_name]), 
                               columns=['vidhan_sabha', 'bhag_sankhya','PS_name','PS_add','male','female','total','file_name'])





front_pange.head(10)





#front_pange.to_csv("front_page1.csv",index = False)
front_pange.to_excel("front_page12.xlsx",index = False)





front_pange.head()








