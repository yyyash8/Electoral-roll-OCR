# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:47:43 2019

@author: yyyas
"""
#from PIL import Image
import pytesseract
from pytesseract import image_to_string
import numpy as np
import pandas as pd
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

#left part is the right part in paint and right part is left part in paint
#565:598 is on y axis and 645:745 is on x axis
#img2=img2[565:598,645:770]

import glob
# To put only first page of pdfs, we will put all jpgs path whose file name is ending with '-01.jpg'
onlyfiles = glob.glob('C:/Users/yyyas/Desktop/91-120/*_01.jpg')

def img_to_txt(x):
    print(x)
    s = x.split('\\')
    s = s[1].split("-")[0]
    img2=cv2.imread(x)
    basewidth = 1700
    wpercent = (basewidth / float(img2.shape[1]))
    size = int((float(img2.shape[0]) * float(wpercent)))
    img2 = cv2.resize(img2,(basewidth,size),interpolation=cv2.INTER_LINEAR)
    kernel = np.ones((1, 1), np.uint8)
    img2=cv2.dilate(img2,kernel,iterations = 1)
    img2 = cv2.bilateralFilter(img2,9,75,75)
    cropped_im_vs = img2[110:202,705:1100]
    cropped_im_bs = img2[110:205,1462:1550] 
    cropped_im_psn = img2[1550:1630, 159:1050]
    cropped_im_psa = img2[1670:1725, 170:1125]
    cropped_im_male = img2[1965:2050, 820:955]
    cropped_im_fem = img2[1965:2050, 1020:1175]
    cropped_im_tot = img2[1965:2050, 1400:1565]
    c_vs = image_to_string(cropped_im_vs,config='-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM --psm 6')
    c_bs = image_to_string(cropped_im_bs,config='-c tessedit_char_whitelist=0123456789 -psm 6')
    c_psn = image_to_string(cropped_im_psn,config='--psm 6')
    c_psa = image_to_string(cropped_im_psa,config='-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM --psm 6')
    c_male = image_to_string(cropped_im_male,config='-c tessedit_char_whitelist=0123456789 --psm 6')
    c_fem = image_to_string(cropped_im_fem,config='-c tessedit_char_whitelist=0123456789 --psm 6')
    c_tot = image_to_string(cropped_im_tot,config='-c tessedit_char_whitelist=0123456789 --psm 6')
    print(c_bs)
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

front_page = pd.DataFrame(np.column_stack([vidhnsbha, bhag_snkhya,PS_name,PS_add,male,female,total,file_name]), 
                               columns=['vidhan_sabha', 'bhag_sankhya','PS_name','PS_add','male','female','total','file_name'])
#front_page.head(10)
#front_page.to_csv("front_page1.csv",index = False)
front_page.to_excel("front_page123.xlsx",index = False)

#front_page.head()

#c_psn = image_to_string(cropped_im_psn,config='--psm 6')
#c_psn
