# Test System Documentation

## Useful links
- [Unittest cheat sheet](https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index)
- [Selenium locating elements](https://selenium-python.readthedocs.io/locating-elements.html) (Note: We're using a pre-release of selenium that selects elements differently)
- [Navigating in selenium](https://selenium-python.readthedocs.io/navigating.html)

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



# Static code validation

## Useful links
- [W3C HTML validator](https://validator.w3.org/)
- [W3C HTML validator API](https://github.com/validator/validator/wiki/Service-%C2%BB-Input-%C2%BB-POST-body)
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
- [W3C CSS validator API](https://jigsaw.w3.org/css-validator/api.html)
Note: We used the regular form for the CSS validator because the API wasn't to our liking


## Using the validators
```bash
./html_validator.sh public # public is the root path for the website
./css_validator.sh public # public is the root path for the website
```
