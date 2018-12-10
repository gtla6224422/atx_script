#coding=utf8
import os

#删除当前目录下pyc文件
def del_pyc():
    #print os.listdir('.')
    del_paths = [name for name in os.listdir('.') if name.endswith('.pyc') or name.endswith('.py~')]
    for del_path in del_paths:
        os.remove(del_path)
    #print os.listdir('.')