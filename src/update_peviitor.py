import requests
import os
import json
import time


class UpdatePeViitor:
    POST_URL = "https://api.peviitor.ro/v5/add/"
    LOGO_URL = "https://api.peviitor.ro/v1/logo/add/"
    TOKEN_URL = "https://api.peviitor.ro/v5/get_token/"

    def __init__(self):
        self.POST_HEADER = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.get_token()}",
        }

        self.LOGO_HEADER = {
            "Content-Type": "application/json",
        }

    def get_token(self):
        token_endpoint = "https://api.peviitor.ro/v5/get_token/"

        token = requests.post(
            token_endpoint, json={"email": "chichiraurazvan@yahoo.com"}
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
            print(post_request_to_server.text)

    def update_logo(self, id_company: str, logo_link: str):

        data = json.dumps([{"id": id_company, "logo": logo_link}])
        response = requests.post(self.LOGO_URL, headers=self.LOGO_HEADER, data=data)

        if response.status_code != 200:
            print(f"Error updating {id_company} logo")
            print(response.text)
