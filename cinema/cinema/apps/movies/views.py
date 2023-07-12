from django.shortcuts import render
from django.http import HttpResponse
import django.utils.timezone as timezone
from datetime import timedelta, datetime

from django.conf import settings
from django.core.mail import send_mail, send_mass_mail

from .models import Hall, Film, Session, Tickets

#Отправка Email
def messages(em, place, time, price):
	datatuple = (
    	('Региcтрация брони в Кинотеатре', f'Здраствуйте, вами забронировано {place} место на {time},цена билета {price}, придите за 30 минут чтоб не потерять бронь. Ждем Вас :)', settings.EMAIL_HOST_USER, [em]),
    	('Сообщение связанное с сайтом', f'Было забронировано место, сообщение оправлено Клиенту', settings.EMAIL_HOST_USER, ['akulenko_874@mail.ru']),
	)
	send_mass_mail(datatuple)

def index(request):
	if request.POST:
		hall = int(request.POST.get("hall"))
		email = request.POST.get("email")
		place = int(request.POST.get("place"))

		Tickets.objects.create(session=Session.objects.get(id=hall), place=place)
		time = Session.objects.get(id=hall).time_s
		price = Session.objects.get(id=hall).ticket_price

		messages(email, place, time, price)

	today = timezone.localtime(timezone.now())
	print(today)

	x = [i for i in range(1, 50)]
	y = [i for i in range(1, 28)]
	sean7 = [i.place for i in Tickets.objects.all() if i.session_id == 7 ]
	sean1 = [i.place for i in Tickets.objects.all() if i.session_id == 1 ]
	sean2 = [i.place for i in Tickets.objects.all() if i.session_id == 2 ]
	sean8 = [i.place for i in Tickets.objects.all() if i.session_id == 8 ]

	return render(request, 'movies/index.html', {'x': x[:9], 'x1': x[9:18], 'x2': x[18:27],
		                                         'x3': x[27:38], 'x4': x[38:49], 'tickets1': sean1,
		                                         'tickets2': sean2, 'tickets7': sean7, 'tickets8': sean8})

def reservation(request, s_id, m_id):
	return render(request, 'movies/app.html', {'s': s_id,'m': m_id})