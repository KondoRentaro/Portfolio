# B鎖(Chain B)の幾何重心を求めよ。
# なお幾何重心の座標は、鎖を構成する残基のCα原子の座標の平均として求めることとする。

import statistics  #平均値を計算するモジュール

file=open('2tbv.cif','r')
x_list=[]
y_list=[]
z_list=[]

for i in file:
    if i.startswith("ATOM"):
        if "CA" in i:
            if " B " in i:
                x_list.append(float(i.split()[10]))
                y_list.append(float(i.split()[11]))
                z_list.append(float(i.split()[12]))

x=statistics.mean(x_list)
y=statistics.mean(y_list)
z=statistics.mean(z_list)

print('(x,y,z)=(%f,%f,%f)' (x,y,z))
file.close()
