from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from practitioner.models import Practitioner
from doctor.models import Patient
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from forms import MyRegistrationForm


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	print (request.POST)
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	group = request.POST.get('group1','Patient')
	if group=='Patient':
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/accounts/loggedin')
		
	if group=='Practitioner':
		if Practitioner.objects.get(User_ID = username) == Practitioner.objects.get(Password = password) and Practitioner.objects.get(User_ID = username):
			args = {}
			arg_temp = {}
			arg_temp['get_id'] = Practitioner.objects.get(User_ID = username)
			args['patients'] = Patient.objects.filter( Doctor_Visited_Id = arg_temp['get_id'].id )
			link = arg_temp['get_id'].id
			return HttpResponseRedirect('/doctor/%s/all/' % link)
	else:
		return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
	return render_to_response('loggedin.html', {'full_name':request.user.first_name, 'username':request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')


def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		handle = open('D:/Dropbox/pythonprojects/www.hospital1.com/counter.txt', 'r+')
		count = int(handle.read())
		handle.close()
		if form.is_valid():
			temp = request.POST.get('username','')
			form.setID('s'+str(count+1))
			trans = 's'+str(count+1)
			form.setName(temp)
			handle1 = open('D:/Dropbox/pythonprojects/www.hospital1.com/counter.txt', 'w')
			handle1.write(str(count+1))
			handle1.close()
			print "SUCCESS"
			form.save()
			return render_to_response('register_success.html', {'username':trans})
	args={}
	args.update(csrf(request))
	args['form']=MyRegistrationForm()
	return render_to_response('register.html', args)
