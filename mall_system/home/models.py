from django.db import models

# 订单表
class Order(models.Model):
    uid = models.ForeignKey('myadmin.Users') # 订单用户的 id
    address = models.CharField(max_length=128)  # 用户收获地址
    addname = models.CharField(max_length=32)  # 用户收获姓名
    addphone = models.CharField(max_length=11)  # 用户收获手机号
    addcode =  models.IntegerField()  # 用户收获邮编
    total_price = models.FloatField() # 订单总价
    total_number = models.IntegerField() # 订单物品数量
    status = models.IntegerField() # 订单状态  0 为订单完成 1 为正在支付  2 支付完成发货
    addtime = models.DateTimeField(auto_now_add=True)

# 订单详情表
class OrderInfo(models.Model):
    orderid = models.ForeignKey("Order") # 订单 id
    gid = models.ForeignKey('myadmin.Goods')  # 商品id
    num = models.IntegerField()  # 商品数量
    # price = models.FloatField()  # 商品总价









