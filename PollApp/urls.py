from django.urls import path
from . import views

urlpatterns=[
	
	path('',views.QuestionsListView.as_view(), name='home'),
	path('<int:pk>/', views.QuestionsDetailsView.as_view(), name='details'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:pk>/vote/', views.VoteView.as_view(), name='vote')

]