import people

class Programmer(People):

	# кол-во языков программирования
	_i_language_prog = 0

	# опыт работы
	_i_experience = 0

	# скил прокраммировани в %
	_i_progr = 0

	# пропишим getter's и setter's
	def set_langauge_prog(self, n): # запрос на кол-во языков которые вы знаете
		x = 0
		n = int(n)
		while(x == 0):
			if n <= 15:
				self._i_language_prog = n
				x += 1
			else:
				print("Инициальзиция не удалась")
				print("Вы не можите выучить 15 языков на уровне профи, за всю свою жизнь")
				print("Повторите попытку...\n")
				n = input("\nВведите кол-во языков программирования: ")
				n = int(n)

	def langauge_prog(self): # возыращаем кол-во языков
		return self._i_language_prog


	def set_experience(self, e): # запрашиваем опыт работы
		x = 0
		x = int(x)
		while(x == 0):
			if e <= 60:
				self._i_experience = e
				x += 1
			else:
				print("Инициальзиция не удалась")
				print("Ваш опыт работы, не может быть больше 60 лет")
				print("Повторите попытку...\n")

	def experience(self): # возвращаем опыт работы
		return self._i_experience

	
	def set_progr(self, pr) # процентное соотношение скилла программирования
		x = 0
		x = int(x)
		while(x == 0):
			if pr <= 100:
				self._i_progr = pr
				x += 1
			else:
				print("Инициальзиция не удалась")
				print("Максимальное значение == 100%")
				print("Повторите попытку...\n")

	def progr(self): # возвращаем процентное соотношение скилла программирования
		return self._i_progr

	# сколько языков программирования вы знаете
	def languages_prog(self):
		if self._i_language_prog == 1 and _i_progr >= 70:
			pritn("Вы знаете 1 язык программирования")
		elif self._i_language_prog == 2 and _i_progr >= 70:
			pritn("Вы знаете 2 языка программирования")
		elif self._i_language_prog == 3 and _i_progr >= 70:
			pritn("Вы знаете 3 языка программирования")
		elif self._i_language_prog == 4 and _i_progr >= 70:
			pritn("Вы знаете 4 языка программирования")
		elif self._i_language_prog >= 5 and _i_progr >= 70:
			print("Да вы профи, вы знаете больше 5 языков программирования, браво!")

	# качество вашего кода
	def programming(self):
		if self._i_progr >= 85 and _i_experience >= 7:
			print("Я выполнил работ отлично!")
		elif self._i_progr >= 65 and _i_experience >= 4:
			print("Я выполнил свою работу хорошо!")
		elif self._i_progr >= 40 and _i_experience >= 1:
			("У меня получился тёмный - мутный код...")
		else:
			print("Мой код можно только выкинуть")

	# вывод основной инфомации
	def printf(self): 
		print("Кол-во языков программирования = ", _i_language_prog)
		print("Опыт работы = ", _i_experience, " лет")
		print("Скил прокраммировани в % = ", _i_progr)