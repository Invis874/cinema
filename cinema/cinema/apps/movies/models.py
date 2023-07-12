from django.db import models

class Hall(models.Model):
	hall_title = models.CharField('Название зала', max_length = 50)
	quantity_pc = models.IntegerField('Количество мест')

	def __str__(self):
		return self.hall_title

	class Meta:
		verbose_name = 'Зал'
		verbose_name_plural = 'Залы'

class Film(models.Model):
	film_title = models.CharField('Название фильма', max_length = 50)
	producer = models.CharField('Режиссер', max_length = 100)
	duration = models.TimeField('Продолжительность')

	def __str__(self):
		return self.film_title

	class Meta:
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильмы'

class Session(models.Model):
	hall = models.ForeignKey(Hall, on_delete = models.CASCADE)
	film = models.ForeignKey(Film, on_delete = models.CASCADE)
	time_s = models.TimeField('Время')
	ticket_price = models.FloatField('Цена билета')

	def __str__(self):
		return f'{self.hall} = {self.film} - {self.time_s}'

	class Meta:
		verbose_name = 'Сеанс'
		verbose_name_plural = 'Сеансы'

class Tickets(models.Model):
	session = models.ForeignKey(Session, on_delete = models.CASCADE)
	place = models.IntegerField('Место')

	def __str__(self):
		return f'Его место - {self.place}'

	class Meta:
		verbose_name = 'Билет'
		verbose_name_plural = 'Билеты'