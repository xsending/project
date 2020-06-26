allGuests = {'Alo': {'cakes': 2, 'chocolates': 7, 'apples': 2, 'snack': 4},
			 'Annie': {'apple pie': 3, 'ice cream': 5, 'beef': 2, 'chicken': 3},
			 'Yela': {'cakes': 2, 'beef': 5, 'chicken': 7, 'salad': 4},
			 'Belo': {'rice': 4, 'apple pie': 5, 'chocolates': 8, 'beef': 5}}


def brought_items(guests, item):
	total_items = 0
	for k, v in guests.items():
		total_items += v.get(item)
	return total_items


"""
function should show the item brought 
by whom and how many items there are
"""
