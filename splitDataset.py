import os
import random




trainval_percent = 0.9      #训练集和验证集的比例
train_percent = 0.9          #训练集比例
xmlfilepath = 'datasets/annotation/xmls' #标签
txtsavepath = 'datasets/images'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)   #标签数
list = range(num)      #索引列表
tv = int(num * trainval_percent)    # 训练集加验证集的数量
tr = int(tv * train_percent)         # 训练集的数量
trainval = random.sample(list, tv)   #随机抽样，选取训练集加验证集的索引和训练集的索引
train = random.sample(trainval, tr)


# 创建用于保存数据集划分后文件列表的文件
ftrainval = open('datasets/ImageSets/trainval.txt', 'w')
ftest = open('datasets/ImageSets/test.txt', 'w')
ftrain = open('datasets/ImageSets/train.txt', 'w')
fval = open('datasets/ImageSets/val.txt', 'w')

# 遍历索引列表，根据索引将文件名写入相应的文件列表中
for i in list:
    name = total_xml[i][:-4] + '\n' # 获取文件名（去除后缀）
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
