from src.scraper import Scraper
from src.validate_city import validate_city

import re


class VonConsulting(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        page = 1
        paged_url = f"{self.url}/page/{page}"

        response = self.get_link_soup(paged_url)
        jobs = response.find_all("div", class_="card-content black-text")

        while jobs:
            if page > 1:
                paged_url = f"{self.url}/page/{page}"
                response = self.get_link_soup(paged_url)
                jobs = response.find_all("div", class_="card-content black-text")

            for job in jobs:
                remote = "On-site"
                # titlu*, link*, locatie*, remote
                title = job.find("h3").text
                link = job.find("a")["href"]
                raw_locations = re.split(
                    r"[/\s,]+",
                    job.find("div", class_="job-location meta-item right").text.strip(),
                )

                locations = []
                for location in raw_locations:
                    low_location = location.lower()

                    if (res := validate_city(location)) is not None:
                        locations.append(res)
                    elif (
                        "remote" in low_location
                        or "full" in low_location
                        or "romania" in low_location
                    ):
                        remote = "Remote"
                        locations.append("Bucuresti")
                    elif "hybrid" in low_location:
                        remote = "Hybrid"
                        locations.append("Bucuresti")

                locations = list(set(locations))

                if locations:
                    self.push_job(title, link, locations, remote=remote)

            page += 1


# stryker_scraper.py POST REQUEST
# visa_scraper.py GET REQUEST
von_consulting = VonConsulting(
    company_name="VONCONSULTING",
    url="https://www.vonconsulting.ro/ro/jobs/",
    logo_url="https://www.vonconsulting.ro/wp-content/themes/vonconsulting.ro/images/logo-vonconsulting.png",
)

von_consulting.get_jobs()
von_consulting.push_peviitor()
