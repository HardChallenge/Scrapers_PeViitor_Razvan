from src.scraper import Scraper
from src.validate_city import validate_city

import re


class Carrefour(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        page = 1
        paged_url = f"{self.url}?page={page}"

        response = self.get_link_soup(paged_url)
        jobs = [
            item.find_parent("a")
            for item in response.find_all("div", class_="box-style")
        ]

        while jobs:
            if page > 1:
                paged_url = f"{self.url}?page={page}"
                response = self.get_link_soup(paged_url)
                jobs = [
                    item.find_parent("a")
                    for item in response.find_all("div", class_="box-style")
                ]

            for job in jobs:
                # titlu*, link*, locatie*, remote (on-site)
                title = job.find("div", class_="carousel-title").text.strip()
                link = job["href"]
                raw_locations = re.split(
                    r"[,./\s]+", job.find("div", class_="location").text.strip()
                )[1:]

                locations = []

                if (result := validate_city(" ".join(raw_locations))) is not None:
                    locations.append(result)

                locations = (
                    [
                        (result := validate_city(item))
                        for item in raw_locations
                        if result is not None
                    ]
                    if len(locations) == 0
                    else locations
                )

                locations = (
                    list(set(locations)) if len(locations) != 0 else ["București"]
                )

                self.push_job(title, link, locations)

            page += 1


carrefour = Carrefour(
    "Carrefour",
    "https://carrefour.ro/corporate/cariere/cauta",
    "https://carrefour.ro/corporate/images/careers/logo.png",
)

carrefour.get_jobs()
carrefour.push_peviitor()
