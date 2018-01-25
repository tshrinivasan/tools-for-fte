import sys
import urllib2
import BeautifulSoup
import commands
import uuid



url = raw_input("Enter URL of the ebook : ")

req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})

con = urllib2.urlopen(req)
soup = BeautifulSoup.BeautifulSoup(con)


book_name = raw_input("Enter book Name : ")


bookid = str(uuid.uuid4())




for meta in soup.findAll('meta', attrs={'property':'og:image'}):
	cover_image =  meta['content'].encode('utf-8')

gen_list = []
for genre in soup.findAll('span',  attrs={'class':'genres'}):
	for genres in genre.findAll('a'):
		gen_list.append(genres.contents[0])

gen = ",".join(gen_list)
gen = gen.encode('utf-8')





for links in soup.findAll('a', href=True):
	if "epub" in links['href']:
		epub_link =  links['href'].encode('utf-8')
	else:
		epub_link = "XXXXXXXX"

	if "authors" in links['href']:
		authors = (links.contents[0]).encode('utf-8')

xml_content = "\n\n" + "<book>" +"\n" + "<bookid>" + bookid + "</bookid>" + "\n" + "<title>" + book_name + "</title>" + "\n" 
xml_content = xml_content + "<author>" + authors + "</author>" + "\n"
xml_content = xml_content + "<image>" + cover_image + "</image>" + "\n"
xml_content = xml_content + "<link>" + url + "</link>" + "\n"
xml_content = xml_content + "<epub>" + epub_link + "</epub>" + "\n"
xml_content = xml_content + "<pdf />" + "\n"
xml_content = xml_content + "<category>" + gen + "</category>" + "\n"
xml_content = xml_content + "<date />" + "\n" + "<books />" + "\n"

print xml_content





if epub_link == "XXXXXXXX":
	print "\n\n\n Note: Add epub link yourself. Thanks \n\n\n"
