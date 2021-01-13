# Missions_to_Mars
## CONTENTS
* [WEB SCRAPING](#web-scraping)
* [MISSIONS TO MARS](#missions-to-mars)
* [ETL](#ETL)
* [FLASK AND JINJA](#flask-and-jinja)

## Web Scraping
   The Internet is full of data; but it is unfortunate that most of this data does not come in readily useable forms such as .csv files. To get around this, data analysts have developed several tools like APIs to obtain information online. However, many sites do not have these convenient API services. For such purposes, Python developers have developed libraries like Beautiful Soup to facilitate "scraping" information directly off webpages. Web scraping is done by reducing a webpage to its HTML components; then iextracting the information of interest through the targeteting of HTML tags. This can be relatively simple as most content is conveniently marked by specific tags. 
   However, as the use of Javascript and non-HTML languages has risen in contemporary web development, scraping has become complicated by a multiplicity of tags burying desired information. Much of the data on the Internet has been placed outside the reach of inexperienced scrapersrelying on simple scraping methods. Developers who use web scrapinf have kept pace with these new methods of thwarting web scrapers. Among them are libraries such as Splinter, Chrome Webdriver, and time that each facilitate different methods of scraping. scraping. 
  
## Missions to Mars
This project is fairly straightforward. Web scraping is used to scrape four different webpages for information: (1) the NASA Mars News site to get the latest news about NASA Mars missions, (2) the JPL Image Gallery for its Featured Image,(3) the Mars Space Facts Page to extract a table containing facts about Mars, and (4) the USGS Mars Astrogeology site to obtain images of Mars from four different angles. 

The first demonstrates the use of HTML tags to locate and obtain specific information on a webpage.
The second demonstrates the use of Splinter, among other techniques to navigate through multiple pages
The third shows the use of pandas to scrape information in table form. 
The fourth combined Python functionalities like list comprehensions and for-loops to obtain URLs embedded in HTML tags then use said URLs to reach secondary pages where images can be scraped. 

## ETL
ETL is an acronym for Extract, Transform, Load. This is a general term describingthe process of extracting data from a source, then performing operations to transform it into a useable form, then loading it into a destination (e,g. a database). This project is an example of all three in operation. Data is extracted from different webpages using web scraping, transformed using Python functions, then loaded onto MongoDB. This ETL pipeline also works in reverse with data extracted from Mongo DBl then transformed and loaded onto a webpage using Jinja via Flask. 

## Flask and Jinja
Flask asks as a central hub for the flow of information from front-end to back-end. It can facilitate the direct extraction of information from primary sources, directs that information to a database, call stored information from a database, and direct information to a webpage.  In this project, it performs all three with Jinja, a web rendering extension that enables ETL pipelines to be made through Flask.Flask directs the extraction and transformation of data from designated sources to be loaded into a database; then later calls the information from the database to be directed to a second destination, in this case, a webpage that updates its data when its sources update their data.  


