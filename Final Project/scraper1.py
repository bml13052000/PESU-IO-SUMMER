import lxml
import csv 
import bs4 as bs
import urllib.request

places=[]
read=urllib.request.urlopen('https://karki23.github.io/Weather-Data/assignment.html').read()
src=bs.BeautifulSoup(read,'lxml')
for i in src.find_all('a'):
    places.append(i.get('href'))

listA=[]
for i in places:
    updatedurl='https://karki23.github.io/Weather-Data/'+i
    sauce=urllib.request.urlopen(updatedurl).read()
    srccode=bs.BeautifulSoup(sauce,'lxml')
    table=srccode.find_all('table')
    th=srccode.find_all('th')
    thdata=[i.text for i in th]
    for row in table:
            table_row=row.find_all('tr')
            for data in table_row:
                table=data.find_all('td')
                row=[i.text for i in table]
                listA.append(row)
    with open('data.csv','w') as writefile:
        csvwriter=csv.writer(writefile)
        csvwriter.writerow(thdata)
    with open('data.csv','a') as writefile:
        for x in listA:
                csvwriter=csv.writer(writefile)
                csvwriter.writerow(x)
