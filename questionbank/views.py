from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, View, DetailView 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse




subject_id = ''

# Create your views here.

class QuestionListView(View):

	def get(self, request, *args, **kwargs):
		questions = Question.objects.all()
		context = {'questions': questions}
		r


class IndexView(View):

	def get(self,request, **kwargs):
		subjects = Subject.objects.all()
		return render(request, "index.html",{ 'subjects': subjects})

class SubjectDetailView(View):

	def get(self,request, **kwargs):
		chapters = Subject.objects.all().filter(id=self.kwargs['pk']).select_related()
		print(request.META.get('HTTP_REFERER'))
		context = { 'chapters': chapters , 'prevurl':request.META.get('HTTP_REFERER') }
		return render(request,'chapter.html',context)



class ChapterDetailView(View):


	def get(self,request,**kwargs):
		questions = Chapter.objects.all().filter(id=self.kwargs['pk']).select_related()
		print(request.META.get('HTTP_REFERER'))
		context = { 'questions': questions ,'prevurl':request.META.get('HTTP_REFERER') }
		return render(request,'questions.html', context)

class QuestionDetailView(View):


	def get(self,request, **kwargs):
		question = Question.objects.all().filter(id=self.kwargs['pk'])
		print(request.META.get('HTTP_REFERER'))
		context = { 'question': question ,'prevurl':request.META.get('HTTP_REFERER') }
		return render(request, 'question.html',context)


class LoginView(View):


	def get(self,request):
		return redirect('/')

	def post(self,request):
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect('/home')
			else:
				error = 'Invalid username or password'
				return render(request, 'index.html' , {'error': error})
				return redirect('/')


class LogoutView(View):

	def get(self,request):
		logout(request)
		return redirect('/home')



		
