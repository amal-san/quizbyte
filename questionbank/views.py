from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.

class QuestionListView(View):

	def get(self, request, *args, **kwargs):
		questions = Question.objects.all()
		context = {'questions': questions}
		return render(request, "test.html", context=context)





class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'name': 'reinout'}