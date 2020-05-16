import os

path = r'C:\Users\Administrator\Desktop\财务分析与决策'
for file in os.listdir(path):
    #在指定的文件夹中寻找，删除后三位是xml的文件
    tail = os.path.join(path,file)[-3:]
    # 删除文件的条件
    if tail == 'xml':
        print('准备删除{}'.format(file))
        remove_target = os.path.join(path,file)
        #删除语句的写法：os.remove(path)，path指的是文件的绝对路径
        os.remove(remove_target)
        print('成功')
