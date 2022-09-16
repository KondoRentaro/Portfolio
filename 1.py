# A鎖(Chain A)の102番目のアミノ酸であるGlyのCα原子と387番目の
# アミノ酸であるLeuのc原子との間の距離を求めよ。なお、単位はÅである。

import math

def length(x1,y1,z1,x2,y2,z2):
    d=math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2) #二点間の距離を求める公式
    return d
countline=0 #カウント0から始める
file=open('2tbv.cif','r')

for line in file:
    if line.startswith("ATOM"):
        if "CA" in line:  #ファイルの"CA"と"ATOM"の文字が入ってる行からfor文で回しカウント開始            
            countline+=1
            if countline==1:
                                
                    CA_A_x1=float(line.split()[10])
                    CA_A_y1=float(line.split()[11])
                    CA_A_z1=float(line.split()[12])
                    print(line)  #1カウント目で表示
            
            elif countline==287:
                    CA_A_x2=float(line.split()[10])
                    CA_A_y2=float(line.split()[11])
                    CA_A_z2=float(line.split()[12])



                    print(line)  #287カウント目で表示
                    
if __name__=='__main__': #関数定義
        dist=length(CA_A_x1,CA_A_y1,CA_A_z1,CA_A_x2,CA_A_y2,CA_A_z2)
        print(' %f Å' %(dist)) 

file.close()


