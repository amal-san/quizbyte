from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField



EASY = 'btn-success'
MEDIUM = 'btn-warning'
HARD = 'btn-danger'


CHOICES = [ (EASY,'EASY'), (MEDIUM,'MEDIUM'),(HARD,'HARD')]



class Question(models.Model):
	question_number = models.FloatField(_("Question's Number"),unique=True)
	question_description = models.TextField(_("Question's Description"),max_length=10000)
	question_answer = models.TextField(_("Question's answer"),max_length=10000)
	question_attr = models.CharField(_("Toughness"),max_length=12,choices=CHOICES,default=EASY)


	def __str__(self):
		return str(self.question_number)

	def get_absolute_url(self):
		return reverse('question_detail', args=[str(self.pk)])



class Chapter(models.Model):
	chatper_number = models.IntegerField(_("Chapter's Number"),unique=True)
	chapter_name = models.CharField(_("Chapter's Name"),max_length=100)
	chapter_summary = models.TextField(_("Chapter's Summary"),max_length=10000)
	chapter_questions = models.ManyToManyField(Question)


	def __str__(self):
		return self.chapter_name


class Subject(models.Model):
	subject_number = models.IntegerField(_("Subject's Number"),unique=True)
	subject_name = models.CharField(_("Subject's Name"),max_length=100)
	subject_chapters = models.ManyToManyField(Chapter)

	def __str__(self):
		return self.subject_name





