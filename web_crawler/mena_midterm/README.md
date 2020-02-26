#Steps Scrapy

1. create the folder (mena_midterm) and cd to that folder in terminal 
2. in the folder create requirements.text file - scrapy and pymongo <that's what we need for now>
3. to install the dependencis in terminal command line :  pip3 install -r requirements.txt 
4. in start a project command line : scrapy startproject "name of your project" ex. programs_fanshawe"
5. set up items.py in spiders folder 
    here you import scrapy 
    and set up de model of the scraped items - json will export them like this like a schema 

6. set up spiders : in spider folder create a file ""_spider.py ex. program_spider.py 
7. seting spider 
    import scrapy 
    import the crawler rule
    import link extractor which allow us to extrat from multiple pages 
    import the model (from items)

    we name our spider 
    tell it what it is going to crawl  specifying the domain to be crawl and the starting url to by crawl

    we assign the rule assignin what we crawl and wwhat do we want back 
    defining what taget do me need based on our model with css selector we target exactly what we need 

    then we yield it to allow us to extract all the items 


8.in command line go to dc the first project folder  
9. command line : scrapy crawl movie -t json -o - > items.json " it will create a json file with the imfo we ask for  
