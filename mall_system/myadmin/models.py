from django.db import models

# 会员管理
class Users(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    sex = models.CharField(max_length=3, null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=64)
    pic = models.CharField(max_length=128, default='/static/public/pics/user.png')
    status = models.IntegerField()
    addtime = models.DateTimeField(auto_now_add=True)
    delete_data = models.CharField(max_length=2, default='1') # 1 为数据没有删除, 0 为数据已经删除


