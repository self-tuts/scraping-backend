from utils import RequestService
from bs4 import BeautifulSoup
from celery import Task

class UbuntuBlog(Task):

    identifier = "ubuntu-blog"

    def __init__(self):
        self.url = "https://blog.ubuntu.com/"
        self.posts = []
        self.tags = ["linux","ubuntu"]

    def scrape(self):
        # creating url for each user
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select("h3.p-heading--four a")
        for eachData in data:
            data = {
                "label" : eachData.string,
                "link" : "{}{}".format(self.url[:-1],eachData.attrs['href']),
                "identifier" : self.identifier,
                "tags" : self.tags
            }
            self.posts.append(data)

        return self.posts

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context
