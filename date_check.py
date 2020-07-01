import re, pyperclip

date_regex = re.compile(r"((\d{2})(/)(\d{2})(/)(\d{4}))")

text = str(pyperclip.paste())

month = []
day = []
year = []
for groups in date_regex.findall(text):
	month.append(groups[3])
	day.append(groups[1])
	year.append(groups[5])

month_range_30 = ['04', '06', '09', '11']
month_range_31 = ['01', '03', '05', '07', '08', '10', '12']

for i in range(len(day)):
	if month[i] in month_range_31:
		if int(day[i]) > 31:
			print(f"Incorrect date: {month[i]}/{day[i]}/{year[i]}")
		else:
			print(f"{month[i]}/{day[i]}/{year[i]}")
	elif month[i] in month_range_30:
		if int(day[i]) > 30:
			print(f"Incorrect date: {month[i]}/{day[i]}/{year[i]}")
		else:
			print(f"{month[i]}/{day[i]}/{year[i]}")
	elif month[i] == '02':
		if int(day[i]) > 28:
			print(f"Incorrect date: {month[i]}/{day[i]}/{year[i]}")
		elif int(day[i]) <= 29:
			if int(year[i]) % 4:
				if int(year[i]) % 400:
					print(f"{month[i]}/{day[i]}/{year[i]}")
		else:
			print(f"{month[i]}/{day[i]}/{year[i]}")
