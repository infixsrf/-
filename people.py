class People():
	#В этом классе не будут пресутствовать getter's
	#Пропишим координаты человека в простанстве"
	_x = 0
	_y = 0

	#Возраст, имя, фамилия"
	_age = 0
	_name = "/0"
	_l_name = "/0"


	#Пишем методы для оперирования переменными
	def set_coordinates(self, x, y):
		f = 0
		while f == 0:
			if x <= 10 and x >= 0:
				if y <= 10 and y >= 0:
					self._x = x
					self._y = y
					f += 1
			else:
				print("У вас ошибка")
				print("Координаты не должны быть меньше 0 и больше 10")

	def set_age(self, age):
		try:
			age = int(age)
			if type(age) == type(0):
				if age <= 100:
				self._age = age
			else:
				print("У вас ошибка")
				print("в возрасте, он не должен превышать шкаллу в 100 лет")
		except Exception as e:
			print("У вас ошибка, вам нужно было ввести число, а не строку")
			
	def set_name(self, name):
		self._name = name

	def set_l_name(self, name):
		self._l_name = name

	#Вывод данный о пространстве
	def printf_coordinates(self):
		print("Ваши координаты:\n")
		print("Горизонтально = ", self._x)
		print("Вертикально = ", self._y)

	#Вывод основных данных
	def key_features(self):
		print("Возраст = ", self._age)
		print("Имя = ", self._name)
		print("Фамилия = ", self._l_name)