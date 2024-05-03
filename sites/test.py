import sys, os

sys.path.append(os.path.dirname(os.getcwd()))

from src.scraper import Scraper


class Ascom(Scraper):

    def __init__(self, company_name, url, logo_url):
        super().__init__(company_name, url, logo_url)

    def get_jobs(self):

        response = self.get_soup()
        jobs = response.find_all(
            "li",
            class_="block-grid-item border border-block-base-text border-opacity-15 min-h-[360px] items-center justify-center rounded overflow-hidden relative z-career-job-card-image",
        )

        for job in jobs:
            title = job.find("span", class_="text-block-base-link company-link-style")[
                "title"
            ]
            link = job.find("a")["href"]

            soup_job_type = self.get_link_soup(link)
            job_type = soup_job_type.find(
                "dl",
                class_="md:max-w-[70%] mx-auto text-md gap-y-0 md:gap-y-5 flex flex-wrap flex-col md:flex-row company-links",
            ).text.split()[-1]

            self.get_jobs_dict(title, link, "Cluj-Napoca", job_type)

        return self.jobs_list


ascom = Ascom(
    company_name="ascom",
    url="https://career.ascom.com/jobs?country=Romania&location=RO+Cluj-Napoca&query=",
    logo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Logo_Ascom.svg/800px-Logo_Ascom.svg.png",
)
ascom.get_jobs()
print(ascom.jobs_list)
ascom.push_peviitor()
