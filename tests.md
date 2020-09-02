# Test System Documentation

## Useful links
[](https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index)
[](https://selenium-python.readthedocs.io/locating-elements.html)
[](https://selenium-python.readthedocs.io/navigating.html)

## Adding a Test

Begin by opening the `website_tests.py` file.

In the WebsiteTest class you will begin by adding a method with a name describing the test you will execute.

```python
class WebsiteTest(unittest.TestCase):
    ...
    def your_new_test(self):
        # Do something!
        pass
    ...
```



Let's say we want to create a function checking if the title is correct.
```python
def test_title_is_correct(self):
    print("Checking if title is correct.")
    driver = self.driver
    driver.get(self.WEBSITE_URL)
    validTitle = "NTI"
    self.assertIn(validTitle, driver.title) 
```


Now the test is implemented and will be run.