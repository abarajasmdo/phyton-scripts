import sys
import easygui
import os.path

codigo = easygui.fileopenbox()
values_file = open(codigo).read().split("\n")
titles = values_file.pop(0).split(",")
titles.pop(0)
titles.pop(0)
values=[]
for val in values_file:
    pval=val.split(",")
    pval.pop(0)
    fileid=pval.pop(0)
    filename = fileid
    if int(fileid) < 100000:
        filename = "0" + fileid
    if int(fileid) < 10000:
        filename = "00" + fileid
    if int(fileid) < 1000:
        filename = "000" + fileid
    if int(fileid) < 100:
        filename = "0000" + fileid
    if int(fileid) < 10:
        filename = "00000" + fileid
    f=open("pres/pres_" + filename + ".prp", "w+")
    i=0
    for prss in pval:
        f.write(titles[i] + " = " + prss + "\n")
        i=i+1
    f.close()
