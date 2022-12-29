#This program scrapes the SOC handbook page and notifies me via email if the text "Handbooks Coming Soon" on the webpage changes in any way
#This change is then assumed to be that the handbook is avialable.
#This program is meant to be run via Windows task scheduler. 
#Help was found from the book "Automate the boring stuff with python" by Al Sweigart. 
# Ayden Smith
# Dec. 28, 2022

import requests, bs4, ezgmail

#Access the SOC webpage 
res = requests.get("https://handbook.cs.utah.edu/")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#print(soup)
def CheckIfSDHandbookIsAdded():
    try:
        #Scrape the element that contains selector for the "Handbooks coming soon" text
        elems = soup.select('body > div > div.row > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > ul > li > ul > li:nth-child(1) > p');
        #The text was changed so assume the handbook is avialable
        if(elems[0].getText() != "Handbooks Coming Soon"):
            ezgmail.send('aysmith17@gmail.com', 'Big News', 'The SD handbook is avialable!')
        elif(elems[0].getText() == "Handbooks Coming Soon"):
            ezgmail.send('aysmith17@gmail.com', 'No Big News', 'The SD handbook is not avialable')
    except:
        #The selector was changed or removed so assume the handbook is avialable
        ezgmail.send('aysmith17@gmail.com', 'Big News', 'The SD handbook is avialable!')



CheckIfSDHandbookIsAdded()
