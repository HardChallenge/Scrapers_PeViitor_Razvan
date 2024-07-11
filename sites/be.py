from src.scraper import Scraper
from src.validate_city import validate_city


from selenium import webdriver
from bs4 import BeautifulSoup


class Be(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=options)

        page = 1
        jobs = []
        prev_response = None

        while True:
            response = BeautifulSoup(
                self.get_selenium(
                    driver, link=f"{self.url}/be-shaping-the-future?page={page}"
                ),
                "lxml",
            )
            response_jobs = response.find_all("div", class_="media-body")
            if response_jobs == prev_response:
                break

            jobs.extend(response_jobs)
            prev_response = response_jobs
            page += 1

        for job in jobs:
            location = job.find("span", class_="text-secondary").text.strip()
            if location:
                print(location)
                city = [i.strip() for i in location.split(",")][0]

                city = validate_city(city)

                if city == "Romania":
                    city = "București"
                elif city is None:
                    continue

                job_title = job.find("h5").text.strip()
                link = f'{self.url}{job.find("a", class_="text-secondary")["href"]}'

                self.push_job(job_title, link, city)


be = Be(
    "Be",
    "https://www.careers-page.com",
    "https://manatal-backend-public-assets.s3.amazonaws.com/media/career_portal_logo_direct_upload/8338a5ba-a93a-411c-af26-dbffadfb8ebb_Be_STF_side.jpg",
)

be.get_jobs()
be.push_peviitor()
