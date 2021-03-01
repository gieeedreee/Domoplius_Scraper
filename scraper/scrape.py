import requests
from bs4 import BeautifulSoup
import pandas as pd
import math


class Scraper:
    """
    The class Scraper scrapes all apartments for sale from website www.domoplius.lt
    """
    def __init__(self, header: dict = {"User-Agent": "Mozilla/5.0"}):
        """
        Inits Scraper Class
        :param header: information of the browser
        """
        self.header = header

    def get_url(self, url: str) -> requests:
        """
        Get response from given url.
        :param url: url of website for scraping.
        :return: response
        """
        try:
            response = requests.get(url, headers=self.header)
        except requests.exceptions.RequestException as e:
            print(e)
            exit()
        return response

    def get_page_number(self, number_of_items: int) -> int:
        """
        Returns the number of pages according to required number of samples. Round up the page number to bigger side.
        :param number_of_items: number of items required to scrape.
        :return: number of pages
        """
        items_per_page = 30
        page_number = number_of_items / items_per_page
        return math.ceil(page_number)

    def collect_information(self, number_of_items: int) -> pd.DataFrame or None:
        """
        Download all information from html at given url to the local filesystem:
        title, area of flat, number of rooms, year of construction, floor, price.
        :param number_of_items: number of items required to scrape.
        :return: dataframe
        """
        title, area, room, year, floor, price = ([] for i in range(6))
        try:
            for page_no in range(0, self.get_page_number(number_of_items)):
                req = self.get_url(
                    f"https://domoplius.lt/skelbimai/butai?action_type=1&page_nr={page_no}&slist=109410160")
                soup = BeautifulSoup(req.text, 'html.parser')
                listings = soup.find_all("div", {"class": ["cntnt-box-fixed"]})

                for item in listings:
                    area.extend([value.text.strip(" m²") for value in item.find_all("span", {"title": "Buto plotas (kv. m)"})])
                    room.extend([value.text.strip(" kamb.") for value in item.find_all("span", {"title": "Kambarių skaičius"})])
                    year.extend([value.text.strip(" m.") for value in item.find_all("span", {"title": "Statybos metai"})])
                    floor.extend([value.text.strip(" a.") for value in item.find_all("span", {"title": "Aukštas"})])
                    title.extend([value.text.strip(" ") for value in item.find_all("h2", {"class": "title-list"})])
                    price.extend([value.text.strip("Kaina: ") for value in item.find_all("p", {"class": "fl"})])

            return pd.DataFrame({
                "title": title,
                "area": area,
                "room": room,
                "floor": floor,
                "year": year,
                "price": price,
            })

        except AttributeError:
            return None

    def write_to_csv(self, number_of_items) -> None:
        """
        Write dataframe to csv file.
        :param number_of_items: number of items required to scrape.
        :return: csv file.
        """
        all_information = self.collect_information(number_of_items)
        pd.DataFrame(all_information).to_csv("../scraped_information.csv",
                                             header=['Title', 'Area', 'Room', 'Floor', 'Year', 'Price'],
                                             index=False)
        return None
