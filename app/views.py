import requests
import webbrowser
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
	return render(request,'index.html')