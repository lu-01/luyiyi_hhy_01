from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	"""用于添加主题的表单"""
	class Meta:
		"""告诉Django根据哪个模型创建表单，以及表单中包含哪些字段"""
		model = Topic      		# 根据Topic模型创建表单
		fields = ['text']       # 表单中包含text字段
		labels = {'text': ''}   # 不要为text字段生成标签
		
class EntryForm(forms.ModelForm):
	"""用于添加条目的表单"""
	class Meta:
		"""告诉Django根据哪个模型创建表单，以及表单中包含哪些字段"""
		model = Entry      		# 根据Entry模型创建表单
		fields = ['text']       # 表单中包含text字段
		labels = {'text': ''}   # 不要为text字段生成标签
		widgets= {'text': forms.Textarea(attrs={'cols': 80})}  # 将文本区域的宽度设置为80列，默认40列
