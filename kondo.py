# Chain Cの残基番号 1(MET) から12Å以内に位置するChain Eの残基の番号をリストアップしてください。
# ただし、残基間の距離はCα原子間の距離とします。

import math

file=open('model1.pdb','r')

list_CA_x=[]
list_CA_y=[]
list_CA_z=[]
list_number=[]  #残基番号のリスト
list_dist=[]

def length(x1,y1,z1,x2,y2,z2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return distance  #二点間の距離の公式

def main():
    cal()
    up()
    
def cal():
    for line_CA in file:
        if "CA" in line_CA:
            line_CA=" ".join(line_CA.split())  #空白をつなげる
            if " C " in line_CA:
                if " 1 " in line_CA:
                    CA_A_x1=float(line_CA.split()[6])
                    CA_A_y1=float(line_CA.split()[7])
                    CA_A_z1=float(line_CA.split()[8])  #Cの1の座標を抽出

            if " E " in line_CA:
                CA_A_x2=float(line_CA.split()[6])
                CA_A_y2=float(line_CA.split()[7])
                CA_A_z2=float(line_CA.split()[8])  #Eの座標を抽出
                number=line_CA.split()[5]   #Eの残基の番号を抽出  

                list_CA_x.append(CA_A_x2)
                list_CA_y.append(CA_A_y2)
                list_CA_z.append(CA_A_z2)
                list_number.append(number)   #Eの座標、残基の番号をリストに格納

                l=len(list_number)  #iが要素以上になったら止まるようにするやつ
                i=0 #Eの座標の1番目から順番に式に入れるためのやつ

    else:
        for x in list_CA_x:  #listはなんでもいい
            dist=length(CA_A_x1,CA_A_y1,CA_A_z1,list_CA_x[i],list_CA_y[i],list_CA_z[i])
            list_dist.append(dist)  #Cの1番目とEの距離をリストに格納
            i+=1
        
            if i==(l+1):  
               break

def up():
    for i in list_dist:
        if i <= float(12):
            print(list_number[list_dist.index(i)])

if __name__ == '__main__':
    main()


file.close()
