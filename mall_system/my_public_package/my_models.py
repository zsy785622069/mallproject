#!/usr/bin/env python3
#  存放项目通用自定制的函数
import random
import time


def ramdom_num(c):
    '''
    产生随机数的函数
    :param c: 产生几个数字符的组合
    :return: 返回随机字符串
    '''
    num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    num2 = [random.choice(num) for i in range(c)]
    return ''.join(num2)

# 上传照片 函数
def filesload(request, image_dict_key, files_path):
    '''
        上传照片 函数
        :param request: request 请求体
        :param image_dict_key: 文件的key 值
        :param files_path: 文件存放的目录 , 例子 './static/myadmin/goods_images/'
        :return: 图片的相对路径. 如 :   /static/myadmin/goods_images/1.jpg
    '''

    # 接受上传的文件
    myfile = request.FILES.get(image_dict_key, None)

    # 生成 图片的路径 + 图片名
    # filename = "./static/myadmin/goods_images/" + ramdom_num(8) + str(time.time()) + '.' + myfile.name.split('.').pop()
    filename = files_path + ramdom_num(8) + str(time.time()) + '.' + myfile.name.split('.').pop()

    # 打开文件,写入
    with open(filename, "wb+") as f:
        for chunk in myfile.chunks():
            f.write(chunk)
    filename2 = filename.split(".", maxsplit=1)[1]
    return filename2


