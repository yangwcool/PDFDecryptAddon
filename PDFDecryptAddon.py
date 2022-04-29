# -*- coding:utf-8 -*-
#
# this script MUST work with PDF Password Remover (www.verypdf.com)
# HOW TO USE:
# put this script into root dir of PDF Password Remover.
# creat a shortcut of this script to shell:sendto dir.
# right click the PDF file and sendto the shortcut.
# the decrypt PDF file will be created in the PDF dir, ehose file name is ended width _jiemi.
# by WANG 2022/3/25

import sys
import os

filePath = sys.argv[1]#传入的文件路径

filePath_head = os.path.split(filePath)[0]#文件路径
filePath_tail = os.path.split(filePath)[1]#文件名

fileName = os.path.splitext(filePath_tail)[0]#文件名
fileName_ext = os.path.splitext(filePath_tail)[1]#文件扩展名

print(" filePath is: %s\n filePath_head is: %s\n fileName is: %s\n" % (filePath,filePath_head,fileName))

if fileName_ext.lower() != ".pdf":
    print("this is not a PDF file")
    os.system("pause")

cmdComander = r'pdfdecrypt.exe -i "{0}" -o "{1}{2}{3}_jiemi.pdf"'.format(filePath,filePath_head,"\\",fileName)
# cmdComander = "pdfdecrypt.exe -i " + "\"" + filePath + "\"" + " -o " + "\"" +filePath_head+ "\\" + fileName + "\"" + "_jiemi.pdf"
os.system(cmdComander)

print("\nEnd of All\n")

os.system("pause")
