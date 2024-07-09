from src.scraper import Scraper
from src.validate_city import validate_city

import re


class Sabs(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        response = self.get_soup(self.url)
        jobs = response.find("div", class_="jobs-slider")

        for job in jobs:
            link = job.find("a", class_="case-box")["href"]
            title = job.find("div", class_="case-text").find("h4").text.strip()

            # Location not specified, HQ is in Iasi
            location = "Iași"

            self.push_job(title, link, location)


sabs = Sabs(
    "Sabs",
    "https://sabs.ro/careers",
    "https://www.sabs.ro/wp-content/uploads/2021/11/logo.svg",
)

sabs.get_jobs()
sabs.push_peviitor()
