# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:15:35 2020

@author: shivamchadha
"""
import smtplib
import requests
from bs4 import BeautifulSoup
url = "https://worldometers.info/coronavirus/country/india/"
content = requests.get(url)
htmlContent = content.content
soup = BeautifulSoup(htmlContent,'html.parser')
containers = soup.find(("div"), ["maincounter-number"]).get_text()
connection = smtplib.SMTP('smtp.gmail.com' , 587)
connection.ehlo()
connection.starttls()
connection.login('reachout2shivam@gmail.com','******')
connection.sendmail('reachout2shivam@gmail.com','shvm24@gmail.com',
                    'India coronavirus Counter'+containers)
connection.quit()

