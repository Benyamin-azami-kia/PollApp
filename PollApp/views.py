from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views import View
from . models import Questions
# Create your views here.



class QuestionsListView(ListView):
	model=Questions
	template_name='index.html'
	context_object_name='questions'



class QuestionsDetailsView(DetailView):
	model=Questions
	template_name='vote.html'
	context_object_name='question'



class ResultsView(DetailView):
	model=Questions
	template_name='result.html'
	context_object_name='question'



class VoteView(View):

	def post(self,request,pk):
		question=get_object_or_404(Questions, pk=pk)
		voted=question.choices_set.get(pk=request.POST['choice'])
		voted.vote+=1
		voted.save()
		return redirect('results', pk=question.id)
