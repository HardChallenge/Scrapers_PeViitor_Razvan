import requests
import os
import json
import time


class UpdatePeViitor:
    POST_URL = "https://api.peviitor.ro/v5/add/"
    LOGO_URL = "https://api.peviitor.ro/v1/logo/add/"
    TOKEN_URL = "https://api.peviitor.ro/v5/get_token/"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36"

    def __init__(self):
        self.POST_HEADER = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.get_token()}",
            "User-Agent": self.USER_AGENT,
        }

        self.LOGO_HEADER = {
            "Content-Type": "application/json",
            "User-Agent": self.USER_AGENT,
        }

    def get_token(self):
        token = requests.post(
            self.TOKEN_URL,
            json={"email": "chichiraurazvan@yahoo.com"},
            headers={"User-Agent": self.USER_AGENT},
        )

        return token.json()["access"]

    def update_jobs(self, company_name: str, data_jobs: list):

        # time sleep for SOLR indexing
        time.sleep(0.2)

        post_request_to_server = requests.post(
            self.POST_URL, headers=self.POST_HEADER, data=json.dumps(data_jobs)
        )

        if post_request_to_server.status_code != 200:
            print(f"Error updating {company_name} jobs")

    def update_logo(self, id_company: str, logo_link: str):

        data = json.dumps([{"id": id_company, "logo": logo_link}])
        response = requests.post(self.LOGO_URL, headers=self.LOGO_HEADER, data=data)

        if response.status_code != 200:
            print(f"Error updating {id_company} logo")
