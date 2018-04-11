
#!/usr/bin/env python
#encoding: utf-8


def pierwiastek(x):
	try:
		result=x**0.5
	except (TypeError):
		print('Niepoprawny typ.')
	except (ValueError):
		print('Liczba nie moze byc ujemna')
	else:
            return result

print(pierwiastek(-7))
