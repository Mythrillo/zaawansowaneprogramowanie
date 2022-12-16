import requests
import random

from locust import HttpUser, task


API_BASE_URL = "https://rbk97v.deta.dev"
API_KEY = requests.get(f"{API_BASE_URL}/api_key").json().get("apiKey")
IMAGE = open("./image_for_locust_test.jpg", "rb").read()


class SimpleApiUser(HttpUser):
    @task
    def random_prime_endpoint(self):
        self.client.get(f"/prime/{random.randint(1, 9223372036854775807)}")

    @task
    def choosen_prime_endpoint(self):
        self.client.get("/prime/2837874123774824")

    @task
    def invert_picture_endpoint(self):
        self.client.post(
            "/picture/invert",
            files=[("picture", ("image_for_locust_test.jpg", IMAGE, "image/jpeg"))],
        )

    @task
    def time_endpoint(self):
        self.client.get(f"/time?api_key={API_KEY}")
