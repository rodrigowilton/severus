from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


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
		return HttpResponse('Usuário ou senha inválidos')


	return redirect('/')


