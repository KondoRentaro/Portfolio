# Chain Cの残基番号 1(MET、Cα原子)から x Å 以内に位置するChain Eの残基の番号をリストアップしてください。
# ただし、残基間の距離は y 原子間の距離とします。そして、xとy(CαかCβ)として任意の値を指定できるようにせよ。

import math

file=open('model1.pdb','r')

#CA
list_CA_x=[]
list_CA_y=[]
list_CA_z=[]
list_numberA=[]  #残基番号のリスト
list_atomA=[]
list_distA=[]

#CB
list_CB_x=[]
list_CB_y=[]
list_CB_z=[]
list_numberB=[]  
list_atomB=[]
list_distB=[]

a=input("任意:  ")  #残機間距離指定
b=input("任意:  ")  #CαかCβか指定

def length(x1,y1,z1,x2,y2,z2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return distance  #二点間の距離の公式

def main():
    cal()
    up()
    
def cal():
    for model in file:
        model=" ".join(model.split())  #空白をつなげる
        if " C " in model:
            if " 1 " in model: #Chain Cの残基番号1の情報抽出
                if "CA" in model:  
                    
                    CA_x1=float(model.split()[6])
                    CA_y1=float(model.split()[7])
                    CA_z1=float(model.split()[8])  #Cの1の座標を抽出

                if "CB" in model:
                    
                    CB_x1=float(model.split()[6])
                    CB_y1=float(model.split()[7])
                    CB_z1=float(model.split()[8])  #Cの1の座標を抽出
                
        if " E " in model:
            if " CA " in model: 
                
                CA_x2=float(model.split()[6])
                CA_y2=float(model.split()[7])
                CA_z2=float(model.split()[8])  #Eの座標を抽出
                numberA=model.split()[5]  #Eの残基の番号を抽出  
                atomA=model.split()[2]
                
                list_CA_x.append(CA_x2)
                list_CA_y.append(CA_y2)
                list_CA_z.append(CA_z2)
                list_numberA.append(numberA)   #Eの座標、残基の番号をリストに格納
                list_atomA.append(atomA)
            
            if " CB " in model: 

                CB_x2=float(model.split()[6])
                CB_y2=float(model.split()[7])
                CB_z2=float(model.split()[8])  
                numberB=model.split()[5]  
                atomB=model.split()[2]

                list_CB_x.append(CB_x2)
                list_CB_y.append(CB_y2)
                list_CB_z.append(CB_z2)
                list_numberB.append(numberB)   
                list_atomB.append(atomB)

                l1=len(list_numberA)  #iが要素以上になったら止まるようにするやつ
                l2=len(list_numberB)

                i=0 #Eの座標の1番目から順番に式に入れるためのやつ
                j=0

    else:
        for x in list_CA_x:  #listはなんでもいい
            diA=length(CA_x1,CA_y1,CA_z1,list_CA_x[i],list_CA_y[i],list_CA_z[i])
            list_distA.append(diA)  #Cの1番目とEの距離をリストに格納
            i+=1

            if i==(l1+1):  
               break

        for x in list_CB_x:
            diB=length(CB_x1,CB_y1,CB_z1,list_CB_x[j],list_CB_y[j],list_CB_z[j])
            list_distB.append(diB)  
            j+=1
        
            if j==(l2+1):  
               break

def up():
    for i in list_distA:
        if i <= float(a):
            if b == "CA":
                print(list_numberA[list_distA.index(i)],":",list_atomA[list_distA.index(i)],":",i)

    for j in list_distB:
        if j <= float(a):
            if b == "CB":
                print(list_numberB[list_distB.index(j)],":",list_atomB[list_distB.index(j)],":",j)

main()


file.close()



