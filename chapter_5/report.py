def get_description():
	"""Return random weather, just like the pros"""

	from random import choice

	possibilites = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']

	return choice(possibilites)