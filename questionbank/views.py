from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, View, DetailView 

# Create your views here.

class QuestionListView(View):

	def get(self, request, *args, **kwargs):
		questions = Question.objects.all()
		context = {'questions': questions}
		return render(request, "test.html", context=context)





class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		subjects = Subject.objects.all()
		return { 'subjects': subjects }

class SubjectDetailView(TemplateView):

	template_name = 'chapter.html'

	def get_context_data(self, **kwargs):
		chapters = Subject.objects.all().filter(id=self.kwargs['pk']).select_related()
		return { 'chapters': chapters }

class ChapterDetailView(TemplateView):

	template_name = 'questions.html'

	def get_context_data(self, **kwargs):
		questions = Chapter.objects.all().filter(id=self.kwargs['pk']).select_related()
		print(questions)
		return { 'questions': questions }

class QuestionDetailView(TemplateView):

	template_name = 'question.html'

	def get_context_data(self, **kwargs):
		question = Question.objects.all().filter(id=self.kwargs['pk'])
		print(question)
		return { 'question': question }