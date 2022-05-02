import scrapy   # give us access to scrappy library.
import json      # makes us work with Json smoothly

from scrapy.http import Request    # allow us to work with links


class ApplelinkSpider(scrapy.Spider):       # spider class template needed to work with scrappy
    name = 'applelink'                         # # need this name for running the spider on command line
    allowed_domains = ['www.politico.com']
    start_urls = []   # empty list to for adding specific urls from politico website

    with open("C:\\Users\\sangariej\\Desktop\\projectone1\\env\\apple\\apple\\spiders\\apple.json") as f:  # open the file in t
        data = json.load(f)        # convert a json  string to dictionary
        for i in data:             # loop through the dictionary
            temp = i['Link']       # use the key link to get the links of the articles
            start_urls.append(str(temp))   # append them as start Urls


    def parse(self, response):
        '''this function allows us to specify the css selectors and wrappers we need to find our texts from the artice'''
        wrapper = response.css('div.super-inner')   # a div wrapper that zooms our css selector into section
        yield {
                'date_time': wrapper.css('p.story-meta__timestamp').css('time::text').get(),   # allows us to get date and time of articles
               
                'Title': wrapper.css('div.summary').css('h1::text').get(),               # allows us to the titles of articles
                
                'Text': wrapper.css('article.content.layout-story').css('p::text').getall(),  # allows us to get all the texts in the artcle.
                
       }

       
