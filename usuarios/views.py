from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import Condominios


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        #user = authenticate(username=username, password=password)

        user = User.objects.filter(username=username).first()


        if user:
            auth_login(request, user)
            return redirect('app/index')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})




def cadastro(request):
	if request.method == "GET":
		return render(request, 'cadastro.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = User.objects.filter(username=username).first()

		if user:
			return HttpResponse('Usuário ja existe')

		user = User.objects.create_user(username=username, password=password)
		user.save()

		return HttpResponse(f"{username} ,Cadastrato com sucesso!")

	return render(request, 'login.html')


def login(request):
	if request.method == "GET":
		return render(request, 'login.html')

	user = User.objects.filter(username=request.POST.get('username')).first()

	if not user or not user.check_password(request.POST.get('password')):
		return redirect('/severus/login/')

	if user:
		request.session['user'] = user.id
		return redirect(f'/app/?username={request.session['user']}')


def logout(request):
	request.session.flush()
	return redirect('/severus/login')


