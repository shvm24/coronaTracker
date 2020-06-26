# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:15:35 2020

@author: shivamchadha
"""
import smtplib
import requests
from bs4 import BeautifulSoup
class Corona:   
    def email(self,containers):
        self.containers=containers
        rec_list =  ['shvm24@gmail.com','ruchisweet4@gmail.com', 'reachout2shivam@gmail.com','taresh003@gmail.com']
        connection = smtplib.SMTP('smtp.gmail.com' , 587)
        connection.ehlo()
        connection.starttls()
        connection.login('reachout2shivam@gmail.com','*****')
        connection.sendmail('reachout2shivam@gmail.com',
                            rec_list,
                            'India coronavirus Counter has increased'+ 
                            'Be Cautious while going out'+ str(containers))        
        connection.quit()
        return containers;     
    def coronaCounter(self,oldCounter):   
        self.oldCounter = oldCounter;            
        url = "https://worldometers.info/coronavirus/country/india/"
        content = requests.get(url)
        htmlContent = content.content
        soup = BeautifulSoup(htmlContent,'html.parser')
        container = soup.find(("div"), ["maincounter-number"]).get_text() 
        containers=int(container.replace(",",''))
        if (containers > oldCounter):
            newCount=co.email(containers) 
            oldCounter = newCount   
        return oldCounter


oldCounter=0        
co = Corona()
oldCounter= co.coronaCounter(oldCounter)
print(oldCounter)
