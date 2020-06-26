inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def show_inventory(sample_inventory):
	print("Inventory: ")
	item_total = 0
	for k, v in sample_inventory.items():
		print(f"{v} {k}")
		item_total += v
	print(f"Total number of items: {item_total}")


def add_to_inventory(sample_inventory, loot):
	added_items = sample_inventory
	for item in loot:
		if item not in added_items:
			added_items[item] = 1
		else:
			added_items[item] += 1
	return added_items


inventory = add_to_inventory(inventory, dragon_loot)
show_inventory(inventory)
