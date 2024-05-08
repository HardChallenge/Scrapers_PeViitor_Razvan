from src.scraper import Scraper
from src.validate_city import validate_city

import re


class GFK(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        page = 1
        prev_length = -1
        jobs = []
        jobs_link = "https://www.gfk.com/careers/search-for-jobs?country_codes11=country_codesRO&sort=-publication_display_date&searchInput="
        while prev_length != len(jobs):
            prev_length = len(jobs)
            response = self.get_link_soup(f"{jobs_link}&page={page}")
            jobs = response.find_all(
                "a",
                class_="job_item",
            )
            page += 1

        for job in jobs:
            link = f"{self.url}{job['href']}"
            title = job.find("h6", class_="uk-margin-remove uk-text-bold").text.strip()
            locations = []

            for location in re.split(
                r"[\s,]+", job.find("div", {"uk-grid": ""}).find("p").text.strip()
            ):
                if (res := validate_city(location)) is not None:
                    locations.append(res)

            locations = (
                "Bucuresti" if not locations or len(locations) == 1 else locations
            )
            self.push_job(title, link, locations)


gfk = GFK(
    "GFK",
    "https://www.gfk.com",
    "https://www.gfk.com/hubfs/GfK_NIQ.svg",
)
gfk.get_jobs()
gfk.push_peviitor()
