from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	"""用户学习的主题"""
	text = models.CharField(max_length=200)   # 主题名
	
	# 记录日期的时间的数据，自动设置当前日期和时间
	date_added = models.DateTimeField(auto_now_add=True)
	
	# 建立到模型User的关系
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		"""存储用于管理模型的额外的信息"""
		verbose_name_plural = 'entries'   # 使用entries表示多个条目
		
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text[:50] + "..."
		
		
