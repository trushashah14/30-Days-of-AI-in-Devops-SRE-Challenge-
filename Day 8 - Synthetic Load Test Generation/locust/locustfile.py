import json
from locust import HttpUser, task, between
import random
import os

data_file = os.environ.get("DATA_FILE", "synthetic_requests.json")

with open(data_file) as f:
    requests = json.load(f)

class SyntheticUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost"  # Set your API base URL here

    @task
    def send_request(self):
        req = random.choice(requests)
        self.client.request(req["method"], req["endpoint"])