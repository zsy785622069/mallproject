from django.shortcuts import render, HttpResponse
from django.views import View
from home.models import Order

# 1. 订单列表
def order_index(request):
    order_data = Order.objects.all()
    return render(request, 'myadmin/order_admin/order_index.html',{'order_data':order_data})

# 2. 订单详情
def order_detail(request,detail_id):
    order_detail = Order.objects.get(id=detail_id)
    print(order_detail)
    return render(request, 'myadmin/order_admin/order_detail.html',{'order_detail':order_detail})

# 3. 订单修改
class OrderUpdate(View):
    def get(self, request, update_id):
        order_up = Order.objects.get(id=update_id)
        return render(request, 'myadmin/order_admin/order_update.html', {'order_up': order_up})

    def post(self, request):
        order_tu = ('address', 'addname', 'addcode', 'order_id', 'status', 'addphone')
        for i in order_tu:
            if not request.POST.get(i):
                return HttpResponse('<script>alert("字段不正确, 请重新添加");location.href="/myadmin/order_update/%s"</script>'%request.POST.get('order_id'))

        try:
            order_data = Order.objects.get(id=request.POST.get('order_id'))
            order_data.address = request.POST.get('address')
            order_data.addname = request.POST.get('addname')
            order_data.addcode = request.POST.get('addcode')
            order_data.status = request.POST.get('status')
            order_data.addphone = request.POST.get('addphone')
            order_data.save()
        except:
            return HttpResponse('<script>alert("字段不正确, 请重新添加");location.href="/myadmin/order_update/%s"</script>' % request.POST.get('order_id'))
        return HttpResponse('<script>alert("修改成功");location.href="/myadmin/order_index"</script>')


'''
a = {
    'address': '123123123', 
    'addname': '12312123', 
    'addcode': '1123', 
    'order_id': '12', 
    'status': '2', 
    'addphone': '12312123'
}


def order_update(request,update_id):
    order_up = Order.objects.get(id=update_id)
    return render(request, 'myadmin/order_admin/order_update.html', {'order_up': order_up})
'''







