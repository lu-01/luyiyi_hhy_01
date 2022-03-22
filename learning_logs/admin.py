from django.contrib import admin

# Register your models here.

# 导入注册的模型
from learning_logs.models import Topic, Entry   

# 注册，让Django通过管理网站管理我们的模型
admin.site.register(Topic)		
admin.site.register(Entry)
