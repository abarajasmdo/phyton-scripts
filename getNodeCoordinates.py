import sys
import easygui

path = easygui.fileopenbox()

with open (path) as input_file:
    info_lines=input_file.read().split("N,")[0].split("NBLOCK")[1].split("\n")
    data_lines=[]
    node_info={}
    for line in info_lines:
        data_lines.append(line.split())
    data_lines.pop(0)
    data_lines.pop(0)
    data_lines.pop()
    f=open("nodeCoordinates.inp", "w+")
    for data in data_lines:
        a="nmodif," + str(data[0]) + "," + str(data[3]) + "," + str(data[4]) + "," + str(data[5]) + "\n"
        f.write(a)
    f.close()
