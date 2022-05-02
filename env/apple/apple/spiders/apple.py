import scrapy                 # import the scrapy library


class AppleSpider(scrapy.Spider):            # create AppleSpider  class
    name = 'apple'                             # need this name for running the spider on command line
    allowed_domains = ['www.politico.com']      # need this for website we headed to
    start_urls = ['https://www.politico.com/search?s=&userInitiated=true&q=APPLE+STOCKS']   # need this for getting the specific things from the website

    def parse(self, response):
        '''the funtion specify css selectior of the things we need from each article and then grab them '''
        for article in response.css('article.story-frag.format-ml'):
            yield{
                'Title' : article.css('img').attrib['alt'],            # get title of articles
                'Link'  : article.css('a').attrib['href'],             #get link of articles
                'Intro' :  article.css('div.tease').css('p::text').get(), # get short intro of articles
                'Category' : article.css('p.category::text').get(),           #get the category the article falls
                'DateandTime': article.css('time').attrib['datetime'],       # get the date and time of that particular article

   }


        for button in response.css('a.button'):    # find all the button css selectors
            if button.css('::text').get()  == 'Next page »':     # on each page check if button has next page on them
                 next_page = button.attrib['href']                # if yes, get it link
                 print(" \n Next Page:" + next_page + "\n" )       #   print(the link out)
                 yield response.follow(next_page, callback = self.parse)   #move to the next page
