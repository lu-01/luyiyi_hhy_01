from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
	"""注销用户"""
	logout(request)   # 注销
	return HttpResponseRedirect(reverse('learning_logs:index'))  # 重定向到主页

def register(request):
	"""注册新用户"""
	if request.method != 'POST':
		# 显示空的注册表单
		form = UserCreationForm()
	else:
		# 处理填写好后的表单
		form = UserCreationForm(data=request.POST)
		
		if form.is_valid():  # 如果数据有效，将用户名和密码的散列值保存到数据库
			new_user = form.save()
			# 让用户自动登录，在重定向到主页
			authenticate_user = authenticate(username=new_user.username, 
										password=request.POST['password1'])
			login(request, authenticate_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
	
	context = {'form': form}
	return render(request, 'users/register.html', context)
		
	
