from django.shortcuts import render

from .models import phoneNumber

def index(request):
	latest_phoneNumber_list = phoneNumber.objects.order_by('-id')[:5]
	return render(request, 'phoneBook/list.html', {'latest_phoneNumber_list': latest_phoneNumber_list})

def detail(request, Pnumber_id):
	try:
		a = phoneNumber.objects.get( id = Pnumber_id)
	except:
		raise Http404("Номер не найден!")

	return render(request, 'phoneBook/detail.html', {'PhoneNumber: a'})