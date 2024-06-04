from src.scraper import Scraper
from src.county import add_diacritics_to_county
from src.validate_city import validate_city

import re


class Tenaris(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        JOBS_LINK = "https://recruitment.tenaris.com/search/?createNewAlert=false&q=&locationsearch=Romania"
        RECRUITMENT_LINK = "https://recruitment.tenaris.com"
        split_pattern = re.compile(r"[,]+")

        startRow = 0
        limit = 15

        response = self.get_link_soup(f"{JOBS_LINK}&startrow={startRow}")
        jobs = response.find_all("tr", class_="data-row")

        while True:

            for job in jobs:
                REMOTE = "on-site"
                title_link_bundle = job.find("span", class_="jobTitle hidden-phone")
                title = title_link_bundle.text.strip()
                link = f'{RECRUITMENT_LINK}{title_link_bundle.find("a")["href"]}'

                location_bundle = job.find("span", class_="jobLocation").text.strip()
                raw_city, raw_county, _ = [
                    item.strip() for item in split_pattern.split(location_bundle)
                ]
                county = add_diacritics_to_county(raw_county)
                city = validate_city(raw_city)

                if city is None:
                    city = raw_city

                if county is None:
                    county = raw_county

                self.push_job(title, link, city, county=county, remote=REMOTE)

            startRow += limit
            response = self.get_link_soup(f"{JOBS_LINK}&startrow={startRow}")
            jobs = response.find_all("tr", class_="data-row")

            if len(jobs) != limit:
                break


tenaris = Tenaris(
    "Tenaris",
    "https://www.tenaris.com/en",
    "https://rmkcdn.successfactors.com/0719b88e/22a8d4d9-4d65-4798-be5a-7.png",
)

tenaris.get_jobs()
tenaris.push_peviitor()
