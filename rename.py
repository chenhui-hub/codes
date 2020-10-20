# -*- coding:utf8 -*-

import os

class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        self.path = "C:/Users/Administrator/Desktop/111"
        self.path1 = "C:/Users/Administrator/Desktop/333" 
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path1), '1-'+ str(i) + '.jpg')
                try: 
                    os.rename(src, dst)           #重命名文件/目录
                    #print 'converting %s to %s ...' % (src, dst)
                    i = i + 1
                except:
                    continue
        #print 'total %d to rename & converted %d jpgs' % (total_num, i)

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
