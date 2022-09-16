# A鎖の226番目のアミノ酸であるSerからXÅ以内に位置する残基をリストアップせよ。
# なお残基間距離はCβ原子間の距離として求めよ。
# ただし、xとして任意の値を指定できるようにせよ。また、GlyはCβ原子を持たないため、Cα原子で代用せよ。

import math
a=input("任意:  ")  #数値入力
def length(x1,y1,z1,x2,y2,z2):
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return dist

file=open('2tbv.cif','r')

list_CB_x=[]
list_CB_y=[]
list_CB_z=[]
list_Ami=[]
list_dist=[]

for line_CB in file:
    if line_CB.startswith("ATOM"):
        line_CB=" ".join(line_CB.split())
        if " A 1 " in line_CB:
            if "CB" in line_CB:
                if " 226 " in line_CB:
                
            # if " A 1 " in line_CB:
                    # print(line_CB)
        #         if " 226 " in line_CB:
    #    if "ATOM" and "CB" in line_CB:
            #   print(line_CB)
    #     if "THE" not in line_CB:

    #         print(line_CB)
        #     if " A 1 " in line_CB:
        #         if " 226 " in line_CB:

                    CB_A_x1=float(line_CB.split()[10])
                    CB_A_y1=float(line_CB.split()[11])
                    CB_A_z1=float(line_CB.split()[12])

                else:
                    CB_A_x2=float(line_CB.split()[10])
                    CB_A_y2=float(line_CB.split()[11])
                    CB_A_z2=float(line_CB.split()[12])
                    Ami=line_CB.split()[5]

                    list_CB_x.append(CB_A_x2)
                    list_CB_y.append(CB_A_y2)
                    list_CB_z.append(CB_A_z2)
                    list_Ami.append(Ami)

            elif "CA" in line_CB:  #Gly用

                # if " A 1 " in line_CB:
                if " GLY " in line_CB:



                        GLY_A_x=float(line_CB.split()[10])
                        GLY_A_y=float(line_CB.split()[11])
                        GLY_A_z=float(line_CB.split()[12])
                        AmiG=line_CB.split()[5]

                        list_CB_x.append(GLY_A_x)
                        list_CB_y.append(GLY_A_y)
                        list_CB_z.append(GLY_A_z)
                        list_Ami.append(AmiG)
    l=len(list_Ami)
    i=0
else:
    for x in list_CB_x:
        dist=length(CB_A_x1,CB_A_y1,CB_A_z1,list_CB_x[i],list_CB_y[i],list_CB_z[i])
        list_dist.append(dist)
        i+=1

        if i==(l+1):
            break
for i in list_dist:
    if i <= float(a):
        print(list_Ami[list_dist.index(i)],":",i)
        
file.close()
