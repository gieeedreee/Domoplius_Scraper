# Domoplius_Scraper
 This package is able to scrape website www.domoplius.lt. 
 There are created functions that take argument (number of samples) and outputs pandas DataFrames are created.
 The following information about the apartments for sale is scraped: 
  - title; 
  - area of flat;
  - number of rooms;
  - year of construction;
  - floor;
  - price.
 

Install the package into the Google Collab's env using pip:

! pip install git+https://github.com/gieeedreee/Domoplius_Scraper.git

from scraper.scrape import Scraper
scraper = Scraper()
