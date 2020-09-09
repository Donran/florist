# Test System Documentation

## Useful links
- [Unittest cheat sheet](https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index)
- [Selenium locating elements](https://selenium-python.readthedocs.io/locating-elements.html) (Note: We're using a pre-release of selenium that selects elements differently)
- [Navigating in selenium](https://selenium-python.readthedocs.io/navigating.html)

## Information regarding docker
We use our own docker image in our test environment. We download it from dockerhub.
You can learn how to make your own docker image over at their [documentation](https://docs.docker.com/get-started/).

Our docker image contains: python, curl, jq, php, npm and node.js.

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


Now the test is implemented and will be run on CI.

## Running tests

To run tests, there are some dependencies that needs to be installed first. If you're using Windows, you're going to have to install WSL, specifically WSL2. You can find out how to update WSL [here on the microsoft docs](https://docs.microsoft.com/en-us/windows/wsl/wsl2-kernel).
When you have WSL2 or a Linux installation, you need to install `gitlab-runner` and `docker`. The documentation for installing them can be found [here for gitlab-runner](https://docs.gitlab.com/runner/), and [here for docker](https://docs.docker.com/).


Now, if you want to run the CI tests directly, you should be able to do so now. To run a CI test locally, simply run the following command: `gitlab-runner exec docker <testname>`, for example:
```
gitlab-runner exec docker static_validation
```
# Running tests locally without CI script

To run tests by themselves, you're going to need python3, less, and jq installed. To install those just run the following commands:
```
sudo apt install python3 npm jq
sudo npm install -g less
```

After that, you can compile the less code to css with the following command from the root project directory: 
```
lessc less/main.less public/css/style.css
```

Now you need to start a webserver to host the project with. Since this project is pure html/css/js, we can just use a simple web server serving the files in the public directory. I recommend using python3's `http.server` module, which can be run with the following command from the project root directory: 
```
cd public
python3 -m http.server 8080
```

To be able to run unittests, you need the selenium firefox standalone service running as well, it can be run with the command:
```
docker run -d -p 4444:4444 --shm-size 1g selenium/standalone-firefox:latest
```
To make sure the script can connect to the firefox server you also need to add the following to your `/etc/hosts`
```
127.0.0.1 selenium_firefox
```
Documentation for selenium's firefox docker can be [found here](https://github.com/SeleniumHQ/docker-selenium).

Now that everything is running you can just run 
```
cd tests/webtest
python3 -m unittest
```
to run all the selenium tests for the website. To run static validation, simple run 
```
./tests/validate/html_validation.sh public
```
from the root directory. If you want to run a test on the css, simply compile with like mentioned earlier and run the previous command but with css instead of html.

All the CI tests will be run when code is pushed and changes were made to related files, see `.gitlab-ci.yml` for more information.

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

# Screenshot Tests

The screenshot tests are run with selenium in the python script `screenshots.py`

In the setUp function theres a list with resolutions
```python
# Different screenshot resolutions
self.resolutions = [
    [1024, 768], 
    [1280, 800], 
    [1360, 768], 
    [1366, 768], 
    [1440, 900], 
    [1600, 900], 
    [1680, 1050],
    [1920, 1080],
    [360, 740],
    [480, 853],
    [414, 896],
    [768, 1024]
]
```
These are the resolutions that the screenshots will be taken in. You can add your own resolution by adding a list to the resolutions list with this format `[<width>, <height>]`

## Running the test
To run the test you should run the `screenshots.py` script

Note: You will need firefox installed to run the script.
