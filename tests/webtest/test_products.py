import WebTestBase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class ProductTest(WebTestBase.BaseTest):
    # Test to make sure all products are present
    def test_products(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        products = driver.find_elements(By.CLASS_NAME, "product")

        if(len(products) > 0):
            # List with expected products, every list item is a product
            # Use this format [<product_name>, <product_price>, <product_id>]
            expected_products = [
                ["Bröllopsbuketter", 1199, 4],
                ["Höstbukett", 399, 6],
                ["Sommarbukett", 199, 3],
                ["Rosor 10-pack", 149, 8],
                ["Tulpaner 10-pack", 99, 9],
                ["Konsultation 30 min", 249, 10],
                ["Begravningskrans", 799, 5]
            ]

            # Checks if the products are less than expected
            if(len(products) < 7):
                self.fail("Not all products could be found.")
            else:
                for index in range(len(products)):
                    expected_product = expected_products[index]
                    expected_name = expected_product[0]
                    expected_price = expected_product[1]
                    expected_id = expected_product[2]

                    name = products[index].find_element(By.CLASS_NAME, "product-name").get_attribute("innerHTML")
                    price = products[index].find_element(By.CLASS_NAME, "price").get_attribute("innerHTML")
                    product_id = products[index].get_attribute("id")
                    product_img = products[index].find_element(By.CLASS_NAME, "product-image")

                    self.assertEqual(name, expected_name)
                    self.assertIn(str(expected_price), price)
                    self.assertEqual(product_id, str(expected_id))
        else:
            self.fail("No products found")

