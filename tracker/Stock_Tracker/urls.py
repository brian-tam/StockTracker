from django.urls import path

from . import views

app_name = 'Stock_Tracker'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	path('trackers/', views.trackers, name='trackers'),
	path('trackers/<str:tid>', views.ticker, name='ticker')
]