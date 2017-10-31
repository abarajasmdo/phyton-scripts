import sys

with open ("RLIST.txt") as input_file:
    info_lines=input_file.read().split("\n REAL CONSTANT")
    data_lines=[]
    real={}
    for line in info_lines:
        data_lines.append(line.split("\n"))
    data_lines.pop(0)
    for data in data_lines:
        sizedata=data[0].split()
        sizedata.pop(4)
        sizedata.pop(2)
        sizedata.pop(0)
        datainfo=data[1].split()
        if int(sizedata[1])>1:
            real[int(sizedata[0])].extend(datainfo)
        else:
            real[int(sizedata[0])]=datainfo
    f=open("realValues.csv", "w+")
    f.write("Real,Real Values\n")
    for k,v in real.items():
        a= str(",".join(x for x in v))
        f.write(str(k) + "," + a + "\n")
    f.close()
