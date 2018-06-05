import sys
import easygui
import os.path

path = easygui.fileopenbox()
extension = os.path.splitext(path)[1].split(".")[1]

codigo = easygui.fileopenbox()
values_file = open(codigo).read().split("\n")
values_file.pop(0)
values_file.pop()
values=[]
for val in values_file:
    values.append(val.split(","))


with open (path) as input_file:
    info_lines=input_file.read().replace("R5.0\n", "").split("/GOPR,")[0].split("SFE,")
    info_lines.pop(0)
    data_lines=[]
    for line in info_lines:
        if "PRES,2," not in line:
            data_lines.append(line.split(","))
    f=open("pres_" + extension + ".inp", "w+")
    for val in values:
        for data in data_lines:
            if int(val[1]) == int(data[0]):
                ceros="00"
                if int(val[0]) > 9:
                    ceros="0"
                if int(val[0]) > 99:
                    ceros=""
                a=str("SF,BSUR" + ceros + val[0]) + ",PRES," + str(data[4].split()[0]) + "\n"
                f.write(a)
    f.close()
