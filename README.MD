
## Start a project
```
scrapy startproject tutorial
```
## Generate an spider
```
scrapy genspider example example.com
```

## Run links extracto spider
cd into the project directory and run the following
```
scrapy runspider spiders/twelveminuteslinks.py  -o links.json --nolog
```
`runspider spiders/twelveminuteslinks.py` => will run the `runspider` command and will use the `spiders/twelveminuteslinks.py` file.
`-o links.json` `-o` means the output file and the `links.json` is the output filename or full path
`--nolog` will prevent the spider to show each results on the console

## Run full content extractor
```
scrapy runspider spiders/twelveminutes.py -o summaries.json --nolog
```

this will extract the full content by reading the links file and scraping all teh content for each one

