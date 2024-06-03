from src.scraper import Scraper
from src.validate_city import validate_city

import re


class Atkins(Scraper):
    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def update_payload(self, offset, limit):
        return {
            "appliedFacets": {"Location_Country": ["f2e609fe92974a55a05fc1cdc2852122"]},
            "limit": limit,
            "offset": offset,
            "searchText": "",
        }

    def get_jobs(self):

        self.headers["Content-Type"] = "application/json"
        offset, limit = 0, 20
        payload = self.update_payload(offset, limit)

        POST_LINK = (
            "https://slihrms.wd3.myworkdayjobs.com/wday/cxs/slihrms/Careers/jobs"
        )

        split_pattern = re.compile(r"[,./\s]+")

        response = self.post_json_link(
            POST_LINK,
            headers=self.headers,
            json=payload,
        )

        while True:
            for job in response["jobPostings"]:
                title = job["title"]
                link = f"{self.url}{job['externalPath']}"
                locations = []

                for raw_location in split_pattern.split(job["locationsText"]):
                    result = validate_city(raw_location)
                    if result is not None:
                        locations.append(result)

                if not locations:
                    locations = ["București"]
                else:
                    locations = list(set(locations))

                self.push_job(title, link, locations, remote="hybrid")

            if not response["jobPostings"] or len(response["jobPostings"]) != limit:
                break

            offset += limit
            payload = self.update_payload(offset, limit)
            response = self.post_json_link(
                POST_LINK,
                headers=self.headers,
                json=payload,
            )


atkins = Atkins(
    "Atkins",
    "https://slihrms.wd3.myworkdayjobs.com/en-US/Careers",
    "https://slihrms.wd3.myworkdayjobs.com/Careers/assets/logo",
)

atkins.get_jobs()
atkins.push_peviitor()
