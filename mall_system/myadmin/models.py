from django.db import models

# 会员管理
class Users(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    sex = models.CharField(max_length=3, null=True) # 男 = 1, 女 = 0
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=64)
    pic = models.CharField(max_length=128, default='/static/public/pics/user.png')
    status = models.IntegerField()  # 普通用户 = 1 , 管理员用户 = 2 , 禁用用户 = 0
    addtime = models.DateTimeField(auto_now_add=True)
    delete_data = models.CharField(max_length=2, default='1') # 1 为数据没有删除, 0 为数据已经删除


# 商品分类表
class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField()
    path = models.CharField(max_length=32)



# 商品信息表
class Goods(models.Model):
    typeid = models.ForeignKey(to="Types", to_field='id')
    title = models.CharField(max_length=128)  # 商品名, 商品标题
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 商品价格
    storage = models.IntegerField()    # 商品库存
    pic = models.CharField(max_length=64)  # 商品图片
    info = models.TextField()  # 商品详情
    status = models.IntegerField()  # 1. 新品, 2. 热销, 3. 下架
    addmin = models.DateTimeField(auto_now_add=True)  # 添加数据的时间




