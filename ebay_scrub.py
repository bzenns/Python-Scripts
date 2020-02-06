import re
import requests


# html = requests.get('https://www.ebay.com/sch/i.html?_nkw=game+boy+dmg&LH_Complete=1&LH_Sold=1&_pgn=1&rt=nc').text
html = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=game+boy+color&_sacat=0&LH_TitleDesc=0&LH_Complete=1&LH_Sold=1&_ipg=200&_pgn=1').text
status = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=game+boy+color&_sacat=0&LH_TitleDesc=0&LH_Complete=1&LH_Sold=1&_ipg=200&_pgn=1')

if status.status_code == 200:

	print("Searching prices, please wait...")

	pattern = re.compile(r"All Listings</span><span aria-label=\"\s\([0-9,]+\)")
	matches = pattern.finditer(html)
	all_listings = 0
	page = 1
	urls = []
	prices = []
	tally = []	

	for match in matches:
		all_listings = int(match.group().replace('All Listings</span><span aria-label=" (', '').replace(',', '').replace(')', ''))

		
	for i in range(all_listings // 200):
		
		html2 = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=game+boy+color&_sacat=0&LH_TitleDesc=0&LH_Complete=1&LH_Sold=1&_ipg=200&_pgn=" + str(page) + "&rt=nc").text
		page += 1
		
		urls.append(html2)




	for url in urls:
		pattern = re.compile(r'"POSITIVE">[$](\d,)?(\d)+\.(\d{2})+')	

		
		matches = pattern.finditer(str(url))
		for match in matches:
			prices.append(match.group().replace('"POSITIVE">$', '').replace(',', ''))



	for price in prices:
		tally.append(float(price))
		print(price)


	print('-' * 25)
	print(f"{len(tally)} listings sold.")
	print(f"Total: ${round(sum(tally), 2)}")
	print(f"Average price: ${sum(tally) // len(tally)}")
	print('-' * 25)
	print(f"Number of pages Found: {page}")

else:
	print(f"Search Failed. Try Again.")