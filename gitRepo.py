import sys
import requests
from bs4 import BeautifulSoup

def getRepos(userName):
	try :
		request=requests.get("https://github.com/"+userName+"?tab=repositories")
		soup=BeautifulSoup(request.text,"html.parser")
		count=0
		for i in soup.find_all("h3",{"class":"repo-list-name"}):
			a=i.contents[1]
			print('%-40s   %10s\n' % (a.string,"https://github.com"+str(a.get("href"))))
			count+=1

		print('Total Repositories :'+str(count))
	except Exception as exception:
		print(type(exception).__name__)

if not(len(sys.argv)==2):
	print("\nusage : python gitRepo.py 'username'\n")
else:
	if(sys.argv[1]=='-h' or sys.argv[1]=='--help'):
		print("\nusage : python gitRepo.py 'username'")
		print("Options and arguments (and corresponding environment variables):")
		print("-h     : print this help message and exit (also --help)\n")
	else:
		getRepos(sys.argv[1])