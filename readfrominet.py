import time
import argparse
import urllib3
import bs4

start_time = time.time()


parser = argparse.ArgumentParser(description = "Read from URL")
parser.add_argument("myurl")
parser.add_argument("tofind")

args = parser.parse_args()
myurl = args.myurl
tofind = args.tofind

#webbrowser.open_new(myurl)
#print("myurl: " + myurl)


i = 0
lines = []
http = urllib3.PoolManager()
#page = http.request('GET', myurl)
#textfile = page.data
page = http.urlopen('GET',myurl)
text = page.data
text2 = page.encode('ascii', 'ignore').decode('ascii')
print(text2)
soup = bs4.BeautifulSoup(text2, 'html5lib')

#soup = bs4.BeautifulSoup(page.data.decode('utf-8','ignore'),'html5lib')
print(soup.prettify())
#lines = page.readlines()

#if tofind in textfile:
#	print(tofind + " ist in " + myurl + " enthalten.")
#	print("Zeilenzahl: ", len(lines))
#	while i != len(lines):
#		if tofind in lines[i]:
#			print("Text found in line " + str((i+1)))
#		i += 1
#else:
#	print("Habe '" + tofind + "' nicht in " + myurl + " gefunden.")

#page = requests.get(myurl)
#print(page.text)
page.close()

print("--- %s seconds ---" % (time.time() - start_time))
exit()
