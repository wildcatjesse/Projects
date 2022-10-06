print('\nJesse Garcia\n'
      'CYBV 473\n'
      'Scripting Assignment 9\n'
      'October 2nd, 2022\n')

import os
import requests
from bs4 import BeautifulSoup



def title1():
    title = soup.title.string
    return title

def images(url):
    images = soup.findAll('img')
    for eachimage in images:
        try:
            imgURL = eachimage['src']
            print(imgURL)
            if imgURL[0:4] != 'http':
                imgURL = url+imgURL
            #dealing with the path
            response = requests.get(imgURL)
            imageName = os.path.basename(imgURL)

            with open(imageName, 'wb') as outFile:
                outFile.write(response.content)
        except Exception as err:
            print(imgURL, err)
            continue

def urlsScrape():
    siteLinks = set()
    base = url
    links = soup.findAll('a')
    for each in links:
        new = each.get('href')
        if not new:
            continue
        if 'http' not in new:
            new = base+new
        if not base in new:
            continue
        if new not in siteLinks:
            siteLinks.add(new)
    for entry in siteLinks:
        print(entry)


if __name__ == '__main__':

    '''Main program'''
    try:
        url = 'https://casl.website'
        page = requests.get(url)   # retrieve web-page
        soup = BeautifulSoup(page.text, 'html.parser')
        print('\n\n The website we are scraping is', url)
        print('\n\n The title of the page is', title1())
        print('\n\n Extracting Images from website and storing them in', os.getcwd())
        images(url)
        print('\n\nHere are some urls from the website')
        urlsScrape()
    except Exception as err:
        print(err)
print('\n\nScript is done')

#%%
