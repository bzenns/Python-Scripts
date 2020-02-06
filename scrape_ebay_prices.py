import re

import requests


html = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=Gameboy+Color+Red&_sacat=0&LH_TitleDesc=0&rt=nc&LH_Sold=1&LH_Complete=1').text

pattern = re.compile(r'"POSITIVE">[$]+(\d)+\.(\d{2})+')
matches = pattern.finditer(html)
prices = []
convert = []

#  Remove target string`
for match in matches:
    prices.append(match.group().replace('"POSITIVE">$', ''))

# Convert price from string to float
for price in prices:
    convert.append(float(price))

for _ in convert:
    print(_)

print('-' * 25)
print(f"Items sold: {len(convert)}")
print(f"Average Price: ${sum(convert) // len(convert)}")
print(f"Total: ${round(sum(convert), 2)}")
print('-' * 25)
print('stopped')