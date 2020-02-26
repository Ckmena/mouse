<<<<<<< HEAD
#Steps Scrapy
1. create the file 
2. create requirements text file - scrapy and pymongo
3. command line :  pip3 install -r requirements.txt 
4. start a project command line : scrapy startproject movies_cms
5. set up items 
6. set up spiders : in spider folder create a file ""_spider.py 
7. seting spider 
in command line go to dc first _cms folder 
8. command line : scrapy crawl movie -t json -o - > items.json " it will create a json file with the imfo we ask for  
=======
# Install dependencies
```
pip3 install -r requirements.txt
```

# Common CLs

### Init a new project
```
scrapy startproject movies_cms
```

### Run Spider for the project `movies_cms`
```
cd movies_cms
scrapy crawl movie -t json -o - > items.json 
```
>>>>>>> ed9496ec1e9ce0fefed0130b68d501b860798112
