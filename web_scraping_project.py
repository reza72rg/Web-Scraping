from bs4 import BeautifulSoup
import requests
import re
import mysql.connector

cnx=mysql.connector.connect(user='root',host='127.0.0.1',password='',
database="car",charset='utf8')


carname=input()
count=0
for j in range(1,50):
    r=requests.get('https://bama.ir/car/all-brands/all-models/all-trims?body=passenger-car&page={i}'.format(i=j))
    soup=BeautifulSoup(r.text,'html.parser')
    val=soup.findAll('div',attrs={'class':'listdata'})
    if count ==20:
        break
    for i in val:
        if (count==20):
            break
        names=i.find('h2',attrs={'itemprop':'name'})
        names=names.text.split()
        for h2tgs in names:
            namecheck=h2tgs.replace('،','')
            if namecheck == carname:
                car_place=i.find('span',attrs={'class':'provice-mobile'})
                karkard=i.find('p',attrs={'class','price hidden-xs'})
                # print('esme mashin :%s  makane mashin :%s  karkard :%s' %(names[1],car_place.text,karkard.text))
                count=count+1

                cursor=cnx.cursor()
                cursor.execute('INSERT INTO cars_information VALUES(\'%s\',\'%s\',\'%s\')' %(names[1],car_place.text,karkard.text))
                print("writed into db")
                cnx.commit()
                break

cnx.close()