import requests
import WebTestBase
class OnlineTest(WebTestBase.BaseTest):
    # Test som kollar ifall hemsidan är fungerande och
    # tillgänglig från internet.
    def test_website_up_and_running(self):
        response = requests.get(self.WEBSITE_URL)
        self.assertEqual(response.status_code, 200)

