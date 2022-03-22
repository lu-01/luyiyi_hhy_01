from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# 导入与所需数据相关的模型
from .models import Topic, Entry   

# 导入表单
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
	"""学习笔记的主页"""
	# render()根据视图提供的数据渲染响应
	return render(request, 'learning_logs/index.html')

# login_required ： 检查用户是否已登陆，登录才运行topics(),未登录重定向到登陆页面
@login_required     # 装饰器：在运行topics()前先运行  login_required 
def topics(request):
	"""显示所有主题"""
	# 查询数据库，筛选用户自己的所有主题，按date_added属性排序
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')  
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	"""显示单个主题及所有条目"""
	topic = Topic.objects.get(id=topic_id)
	
	# 确认请求的主题属于当前用户
	if topic.owner != request.user:
		raise Http404 
	
	entries = topic.entry_set.order_by('-date_added')  # 降序排列
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""添加新主题"""
	if request.method != 'POST':  	# 未提交数据，创建一个新表单
		form = TopicForm()
	else: 							# 处理POST提交数据
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
	
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""在特定主题添加新条目"""
	topic = Topic.objects.get(id=topic_id)  # 获取正确的主题
	
	if request.method != 'POST':  	# 未提交数据，创建一个新表单
		form = EntryForm()
	else: 							# 处理POST提交数据
		form = EntryForm(data=request.POST)
		if form.is_valid():	
			new_entry = form.save(commit=False)		# 暂不保存到数据库 
			new_entry.topic = topic    				# 设置关联主题
			new_entry.save()						# 保存到数据库
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
	
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	"""编辑既有条目"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	
	# 确认请求的主题属于当前用户
	if topic.owner != request.user:
		raise Http404 
	
	if request.method != 'POST':
		# 初次请求使用当前条目填充表单
		form = EntryForm(instance=entry)
	else:
		# 处理POST提交数据
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return  HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
	
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)




