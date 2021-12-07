from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm


def index(request):
	return render(request, 'Stock_Tracker/index.html')


def trackers(request):
	if request.method == 'POST':
		form = TickerForm(request.POST)
		if form.is_valid():
			ticker = request.POST['ticker']
			return HttpResponseRedirect(ticker)
	else:
		form = TickerForm()
	return render(request, 'Stock_Tracker/tracker.html', {'form': form})

def ticker(request, tid):
	context = {}
	context['ticker'] = tid
	return render(request, 'Stock_Tracker/ticker.html', context)