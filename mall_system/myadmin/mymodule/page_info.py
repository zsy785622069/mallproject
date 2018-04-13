#!/usr/bin/env python3


# V 1.3.
#   1). 解决了, 当总页数 <= 每页显示页数时 , 显示页数会少一个页码的问题

class  PageInfo(object):
    def __init__(self, current_page,per_page_num, all_count, base_url, get_url='' , page_range=9):
        """
        :param current_page: 当前页
        :param per_page_num: 每页显示的数据的条数
        :param all_count: 数据总条数
        :param base_url: 请求路径
        :param page_range: 显示页数, 标准网页页码数
        :param get_url : 用户除 p 参数之外提交的其他 get 参数, 用来拼接 url
        """
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = int(1)
        self.current_page = current_page
        self.per_page_num = per_page_num
        # 数据总条数 / 每页页数  如果 余数为 0 商就就是页数, 如果非零  页数就是 商 + 1
        quotient, remainder = divmod(all_count, per_page_num)
        if remainder != 0:
            self.all_page = quotient + 1   # all_page 总页数
        else:
            self.all_page = quotient
        self.base_url = base_url
        self.page_range = page_range
        self.get_url = get_url
        # 限制当前页的 范围
        if current_page < 1:
            self.current_page = 1
        elif current_page >self.all_page:
            self.current_page = self.all_page

    def start(self):
        return (self.current_page - 1) * self.per_page_num

    def end(self):
        return self.current_page * self.per_page_num

    def page_str(self):
        '''在 HTML 页面中显示页码信息'''
        page_list = []

        # 首页
        home_page = '<li><a href="%s?p=1%s">首页</a></li>'%(self.base_url, self.get_url)
        page_list.append(home_page)
        # 限制 上一页
        if self.current_page <=1:
            previous = '<li><a href="">上一页</a></li>'
        else:
            previous = '<li><a href="%s?p=%s%s">上一页</a></li>' %(self.base_url,self.current_page-1, self.get_url)
        page_list.append(previous)


        # 整个 大 if 的作用 : 使用 start 与 end 类限制页码的个数
        if self.all_page <= self.page_range:
            # 此 if 的 作用 : 当页码总数 <= 最大页码显示的个数, 时触发
            start = 1
            end = self.all_page
        else:
            # 区间用来进行p判断
            if self.current_page > int(self.page_range/2):
                if self.current_page >= self.all_page-int(self.page_range/2):
                    # 此 if 循环 : 当前页码 >= 最大页码-标准页码/2 时触发, 不然就会出现没有数据的假页码,
                    # 比如最大页码, 113 此时就会出现 114 , 114 就是假页码
                    start = self.all_page - self.page_range + 1 # 如果不加 1 页码数, 开始的页码就会是 标准页码多一个
                        # 这个时候开始生成为就应该是, 最大页码 - 标准页码 + 1 = 这时页面上的页码才是 标准页码个数
                    end = self.all_page + 1 # 最后一只能是 最大页码
                else:
                    start = self.current_page - int(self.page_range/2)
                    end = self.current_page + int(self.page_range/2)+1
            else:
                # 处理 首页的第几页
                start = 1 # 说明页码的开头必须是 1
                end = self.page_range + 1 #

        # 当总页数 <= 每页显示页数时, 显示页数会少一个页码, 所以要加 end + 1 就会多生成一个页码
        if  self.page_range >= self.all_page:
            end +=1

        # for i in range(1, self.all_page+1):
        for i in range(start, end):
            # for 的作用: 循环生成页码, 而页码的个数是在 self.page_range 中指定
            # start 与 end 是为了限制页码的个数

            # if 判断的 用途 , 为了实现, 只有在中间的 页码 才有  class="active" 属性
            if self.current_page == i:
                temp = '<li class="am-active"><a href="%s?p=%s%s">%s</a></li>'%(self.base_url, i, self.get_url, i)
            else:
                temp = '<li><a href="%s?p=%s%s">%s</a></li>' % (self.base_url, i, self.get_url, i)
            page_list.append(temp)

        # 限制 下一页
        if self.current_page >= self.all_page:
            next_page = '<li><a href="">下一页</a></li>'
        else:
            next_page = '<li><a href="%s?p=%s%s">下一页</a></li>' %(self.base_url,self.current_page+1, self.get_url)
        # 添加进列表
        page_list.append(next_page)


        # 尾页
        home_page = '<li><a href="%s?p=%s%s">尾页</a></li>'%(self.base_url, self.all_page, self.get_url)
        page_list.append(home_page)
        return ''.join(page_list)




# class  PageInfo(object):
#     def __init__(self, current_page,per_page_num, all_count, base_url, page_range=9):
#         """
#         :param current_page: 当前页
#         :param per_page_num: 每页显示的数据的条数
#         :param all_count: 数据总条数
#         :param base_url: 请求路径
#         :param page_range: 显示页数, 标准网页页码数
#         """
#         try:
#             current_page = int(current_page)
#         except Exception as e:
#             current_page = int(1)
#         self.current_page = current_page
#         self.per_page_num = per_page_num
#         # 数据总条数 / 每页页数  如果 余数为 0 商就就是页数, 如果非零  页数就是 商 + 1
#         quotient, remainder = divmod(all_count, per_page_num)
#         if remainder != 0:
#             self.all_page = quotient + 1   # all_page 总页数
#         else:
#             self.all_page = quotient
#         self.base_url = base_url
#         self.page_range = page_range
#         # 限制当前页的 范围
#         if current_page < 1:
#             self.current_page = 1
#         elif current_page >self.all_page:
#             self.current_page = self.all_page
#
#
#     def start(self):
#         return (self.current_page - 1) * self.per_page_num
#
#     def end(self):
#         return self.current_page * self.per_page_num
#
#     def page_str(self):
#         '''在 HTML 页面中显示页码信息'''
#         page_list = []
#
#         # 首页
#         home_page = '<li><a href="%s?p=1">首页</a></li>'%(self.base_url)
#         page_list.append(home_page)
#         # 限制 上一页
#         if self.current_page <=1:
#             previous = '<li><a href="">上一页</a></li>'
#         else:
#             previous = '<li><a href="%s?p=%s">上一页</a></li>' %(self.base_url,self.current_page-1)
#         page_list.append(previous)
#
#
#         # 整个 大 if 的作用 : 使用 start 与 end 类限制页码的个数
#         if self.all_page <= self.page_range:
#             # 此 if 的 作用 : 当页码总数 <= 最大页码显示的个数, 时触发
#             start = 1
#             end = self.all_page
#         else:
#             if self.current_page > int(self.page_range/2):
#                 if self.current_page >= self.all_page-int(self.page_range/2):
#                     # 此 if 循环 : 当前页码 >= 最大页码-标准页码/2 时触发, 不然就会出现没有数据的假页码,
#                     # 比如最大页码, 113 此时就会出现 114 , 114 就是假页码
#                     start = self.all_page - self.page_range + 1 # 如果不加 1 页码数, 开始的页码就会是 标准页码多一个
#                         # 这个时候开始生成为就应该是, 最大页码 - 标准页码 + 1 = 这时页面上的页码才是 标准页码个数
#                     end = self.all_page + 1 # 最后一只能是 最大页码
#                 else:
#                     start = self.current_page - int(self.page_range/2)
#                     end = self.current_page + int(self.page_range/2)+1
#             else:
#                 # 处理 首页的几页页
#                 start = 1 # 说明页码的开头必须是 1
#                 end = self.page_range +1 #
#
#         # for i in range(1, self.all_page+1):
#         for i in range(start, end):
#             # for 的作用: 循环生成页码, 而页码的个数是在 self.page_range 中指定
#             # start 与 end 是为了限制页码的个数
#
#             # if 判断的 用途 , 为了实现, 只有在中间的 页码 才有  class="active" 属性
#             if self.current_page == i:
#                 temp = '<li class="am-active"><a href="%s?p=%s">%s</a></li>'%(self.base_url, i, i)
#             else:
#                 temp = '<li><a href="%s?p=%s">%s</a></li>' % (self.base_url, i, i)
#             page_list.append(temp)
#
#         # 限制 下一页
#         if self.current_page >= self.all_page:
#             next_page = '<li><a href="">下一页</a></li>'
#         else:
#             next_page = '<li><a href="%s?p=%s">下一页</a></li>' %(self.base_url,self.current_page+1)
#         # 添加进列表
#         page_list.append(next_page)
#
#
#         # 尾页
#         home_page = '<li><a href="%s?p=%s">尾页</a></li>'%(self.base_url, self.all_page)
#         page_list.append(home_page)
#         return ''.join(page_list)
