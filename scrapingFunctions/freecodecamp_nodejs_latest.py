from utils import RequestService
from bs4 import BeautifulSoup
import logging

class FreeCodeCampNodeJSLatest():

    identifier = "freecodecamp-nodejs-latest"

    def __init__(self):
        self.url = "https://medium.com/tag/nodejs/latest/"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".postArticle.postArticle--short")
        
        for eachData in data:
            try :
                    data = {
                             "label" : eachData.find('div',class_='section-content').h3.string,
                             "link" : eachData.find('div',class_='postArticle-content').parent.attrs['href'],
                             "identifier" : self.identifier,
                             "tags" : ["nodejs"]
                     }
                    self.posts.append(data)
            except Exception as e:
                logging.error("Error while parsing data",str(e))
                continue

        return self.posts

