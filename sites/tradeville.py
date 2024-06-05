from src.scraper import Scraper
from src.validate_city import validate_city

import re


class Tradeville(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        JOBS_LINK = "https://tradeville.ro/cariere"
        split_pattern = re.compile(r"[,]+")
        counter = 1

        response = self.get_link_soup(JOBS_LINK)
        jobs = response.find_all("div", class_="accordion-item")

        for job in jobs:
            title_city_bundle = job.find(
                "button", class_="accordion-button"
            ).text.strip()
            title, city = [
                item.strip() for item in split_pattern.split(title_city_bundle)
            ]

            city = validate_city(city)
            if city is None:
                city = "București"

            hasHybrid, hasRemote = False, False

            job_remote_paragraph = job.find_all("div", class_="mb-5")[-2]
            for list_item in job_remote_paragraph.find_all("li"):
                lower_text = list_item.text.lower()
                if "remote" in lower_text:
                    hasRemote = True
                if any(word in lower_text for word in ["hybrid", "hibrid"]):
                    hasHybrid = True

            remote = "on-site"
            if hasRemote and hasHybrid:
                remote = ["remote", "hybrid"]
            elif hasHybrid:
                remote = "hybrid"
            elif hasRemote:
                remote = "remote"

            self.push_job(title, f"{JOBS_LINK}#{counter}", city, remote=remote)
            counter += 1


tradeville = Tradeville(
    "Tradeville",
    "https://tradeville.ro",
    "https://tradeville.ro/build/images/tradeville-logo.43a2dbcc.svg",
)

tradeville.get_jobs()
tradeville.push_peviitor()
