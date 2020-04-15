from django.contrib import admin
from .models import Stutable
from django.utils.safestring import mark_safe




# Register your models here.
class StuAdmin(admin.ModelAdmin):
    site_header = '管理系统'  # 此处设置页面显示标题
    site_title = '人员信息'  # 此处设置页面头部标题

    # 正序排列，如果需要按相反顺序，在前面加-号，如ordering = ("-id", )
    # ordering = ('username','create_time')
    search_fields = ['title']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    # list_editable 设置默认可编辑字段
    # list_editable = ['username']
    # def image_data(self, obj):
    #     return mark_safe(u'<img src="%s" width="100px"/>' % obj.head_img.url)
    #
    # readonly_fields = ('image_data',)  # 必须加这行 否则访问编辑页面会报错
    # image_data.short_description = u'头像'
    list_display = ('username', 'email',  'gender', 'mobile', 'password_hash', 'image_img', 'head_img','create_time')




admin.site.register(Stutable, StuAdmin)