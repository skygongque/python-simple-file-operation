import os
import shutil

# move files from source path to destination path 
# 从源路径下的所有文件移动到目标路径
def moveFiles(sourcePath, destPath):
    fileList = os.listdir(sourcePath)
    for file in fileList:
        tail = file[-3:]
        # 移动文件的条件
        if tail == 'xml':
            print('移动文件',file)
            filePath = os.path.join(sourcePath, file)
            #print(filePath + ' to ' + destPath)
            shutil.move(filePath, destPath)    

sourcePath = r"C:\Users\Administrator\Desktop\瑞秋（Rachel）英语 音标 美式英语发音课程【Rachel's English】机翻中英字幕"
destPath =r"C:\Users\Administrator\Desktop\瑞秋（Rachel）英语 音标 美式英语发音课程【Rachel's English】机翻中英字幕\弹幕"

moveFiles(sourcePath, destPath)

'''
filePath = os.path.join(sourcePath, file)
                print(filePath + ' to ' + destPath)	
                #shutil.move(filePath, destPath)
'''
