from src.scraper import Scraper
from src.validate_city import validate_city

import re


class Sievo(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        response = self.get_soup(self.url)
        jobs = response.find_all("a", class_="c-item-career__overlay-link")

        for job in jobs:
            link = f"https://sievo.com{job['href']}"

            # example: "Open position in Senior Software Engineer in Bucharest, Romania"
            title_location_bundle = re.split(r"\s+", job["title"])
            title, location = (
                " ".join(title_location_bundle[3:-3]),
                title_location_bundle[-2:],
            )

            if location[1].lower().strip() != "romania":
                continue

            if (result := validate_city(location[0][:-1].strip())) is None:
                continue

            self.push_job(title, link, result, remote="Remote")


sievo = Sievo(
    "Sievo",
    "https://sievo.com/careers#openpositions",
    "https://fs.hubspotusercontent00.net/hubfs/3445609/sievo-website/assets/icons/sievo-logo.svg",
)

sievo.get_jobs()
sievo.push_peviitor()
