import re, requests

from bs4 import BeautifulSoup


html = requests.get('https://orangecounty.craigslist.org/d/software-qa-dba-etc/search/sof')
bsobj = BeautifulSoup(html.text, 'lxml')


# with open('cl_software_jobs.txt') as f:
#     htmltxt = f.readline()

# for title in bsobj.find_all(class_="result-title"):
#     print(f'{title.text}')

# for title in bsobj.find_all('span', {'class':'nearby'}):
#     print(f'{title.text}')

# -----------------GRABS URLS FROM CRAIGSLIST SOFTWARE EMPLOYMENT PAGE AND LOOPS THROUGH JOB DESCRIPTIONS----------------
pattern = re.compile(r'(https?)://[\w/.\-=^_+\'\?\%\&\.]+')
matches = pattern.finditer(str(bsobj))

links = set()
for match in matches:
    # print(match.group())
    links.add(match.group())

for link in links:
    html = requests.get(link)
    bsobj2 = BeautifulSoup(html.text, 'html5lib')
# ------------------------------------------------------------------------------------------------------------------------
    
    # ---------------BYPASS ATTRIBUTE ERROR----------------
    try:
        print(bsobj2.find(id='postingbody').get_text())
    except AttributeError as e:
        pass
    # -----------------------------------------------------

print(f"Listings Found: {len(links)}")
print(f"{'-' * 89 + 'done.'}")