import requests
import WebTestBase
class OnlineTest(WebTestBase.BaseTest):
    # Test to make sure the website is up and running and
    # available to the internet
    def test_website_up_and_running(self):
        response = requests.get(self.WEBSITE_URL)
        self.assertEqual(response.status_code, 200)

