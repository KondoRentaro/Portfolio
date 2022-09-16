#A鎖の226番目のアミノ酸であるSerから4Å以内に位置する残基をリストアップせよ。
#なお残基間距離はCα原子間の距離として求めよ。

import math

def length(x1,y1,z1,x2,y2,z2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return distance

file=open('2tbv.cif','r')

list_CA_x=[]
list_CA_y=[]
list_CA_z=[]
list_Ami=[] #アミノ酸の名前
list_dist=[]

for line_CA in file:
    if "ATOM" and "CA" in line_CA:
        if "THE" not in line_CA:
            line_CA=" ".join(line_CA.split()) #空白をつなげる
            if " A 1 " in line_CA:
                if " 226 " in line_CA:
                    CA_A_x1=float(line_CA.split()[10])
                    CA_A_y1=float(line_CA.split()[11])
                    CA_A_z1=float(line_CA.split()[12])  #Aの226番目の座標を抽出

                else:
                    CA_A_x2=float(line_CA.split()[10])
                    CA_A_y2=float(line_CA.split()[11])
                    CA_A_z2=float(line_CA.split()[12])  #ifで定義されたAの226番目以外の座標を抽出
                    Ami=line_CA.split()[5]  #アミノ酸のアルファベットを抜き出し

                    list_CA_x.append(CA_A_x2)
                    list_CA_y.append(CA_A_y2)
                    list_CA_z.append(CA_A_z2)
                    list_Ami.append(Ami)  
                    
                    l=len(list_Ami)  #iが要素以上になったら止まるようにする
                    i=0  #Eの座標の1番目から順番に式に入れる
else:
    for x in list_CA_x:  #listはなんでもいい
        dist=length(CA_A_x1,CA_A_y1,CA_A_z1,list_CA_x[i],list_CA_y[i],list_CA_z[i])  
        list_dist.append(dist)  #Cの1番目とそれ以外の座標の距離をリストに格納
        i+=1

        if i==(l+1):
            break
for i in  list_dist:
     if i <= float(4):
        print(list_Ami[list_dist.index(i)],":",i)  #4Å以下の残基を表示
file.close()
                    
                                                
