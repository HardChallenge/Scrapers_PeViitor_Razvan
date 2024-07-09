from src.validate_city import validate_city
from src.scraper import Scraper


class eSolutions(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        response = self.get_link_soup(f"{self.url}/careers")
        jobs = response.find("div", class_="col-12 mt-3").find_all(
            "div", class_="careers-wrapper mb-3"
        )

        for job in jobs:
            title = job.find("div", class_="job-title").text.strip()
            link = f'{self.url}{job.find("a", class_="primary-button")["href"]}'

            # Location not specified, HQ is in București
            location = "București"
            remote = job.find("a", class_="job-tag").text.strip().lower()

            self.push_job(title, link, location, remote=remote)


eSolutions = eSolutions(
    "eSolutions",
    "https://www.esolutions.tech",
    "https://www.esolutions.tech/icons/esol.svg",
)

eSolutions.get_jobs()
eSolutions.push_peviitor()
