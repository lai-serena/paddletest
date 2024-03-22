import os
import cv2

dirs=r"label"
names={}
fw_train=open("train.txt","w",encoding="utf-8")
fw_test=open("test.txt","w",encoding="utf-8")
fw_label=open("label_list.txt","w",encoding="utf-8")

for dir in os.listdir(dirs):
    if dir == "JPEGImages":
        path=os.path.join(dirs,dir)
        total_nums = len(os.listdir(path))
        i=1
        for file in os.listdir(path):
            full_name=file #全名
            name=os.path.splitext(file)[0] #去除文件后缀名
            if os.path.exists(os.path.join(path.replace("JPEGImages","Annotations"),name+".xml")):
                #划分训练测试数据集
                if i<total_nums*0.7:
                    fw_train.write("./JPEGImages/{} ./Annotations/{}.xml\n".format(full_name,name))
                else:
                    fw_test.write("./JPEGImages/{} ./Annotations/{}.xml\n".format(full_name, name))
                i+=1
fw_train.close()
fw_test.close()





