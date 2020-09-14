# Florist

## Test system documentation can be found at:
[Test System Documentation](https://gitlab.com/the-travelling-salesmen/florist/-/blob/master/tests.md)

## Programming languages


#### HTML
#### CSS /w less
#### JavaScript /w JQuery
#### Python (tests)
#### Bash (CI scripts)



## Development Environment Standard

#### Editor 
**Your favorite editor**

#### Browser 
**Firefox/Chromium**

#### OS 
**Linux: Ubuntu 20.04.1 LTS**

To run the static code validation tests locally you need to install some dependencies:
`apt update -qq && apt install -yqq jq`



## Coding Conventions

#### General code
+ K&R identation standard if nothing else is specified.
+ 4 spaces are to be used for identation.
+ LF is to be used for line breaks. 
+ Complicated sections in the code shall be commented in addition to documentation.
+ All code shall be clean, no old code shall be left in comments.
+ Any "official" coding conventions for the used language shall be followed.
#### CSS
+ kebab-case
+ Unnecessary rules shall be removed, no overwritten rules shall remain in the code.
+ When possible, avoid !important.
+ Code shall be structured in a readable way.
+ Distinct class/id-names.
+ Start working from mobile viewport and work upwards.
+ All CSS shall be written in external style sheets. 
#### HTML
+ Shall validate (Done by CI on pushed commits).
+ Self-closing HTML tags shall have a slash at the end.
+ Use indentation in open tags.
#### JavaScript
+ camelCase
+ The new standards shall be followed, for example, let/const, new arrow functions.
+ jQuery shall be used to minimize code and make it more effective.
+ When types are specified, type-safe comparison shall be used.



## Definition of Done 

#### General
+ Everything shall be presentable.
#### Documents
+ All team members shall read all documents and agree on them and any changes.
+ All documents shall be complete, and cover the whole sprint.
#### Code
+ Tests shall be written and passing.
+ Coding conventions and programming languages documents shall be followed.
+ All team members shall read the code and documentation and understand them.
+ If needed, QA shall be preformed.
+ Pat Capitalist-Robin and ask for forgiveness for the awful code.
+ Code shall be looked through in search of points to be improved (Variables, hardcoded code etc.).



## CI

### Tests
+ All tests specified in `.gitlab-ci.yml` will be run on pushed code, assuming that files related to the test have been changed.
### Pages
+ GitLab pages will be automatically deployed on successful CI tests.



## Copyright

### Images
We use images from unsplash. [Unsplash License](https://unsplash.com/license)

### Fonts
All fonts used on our website are provided by [Google Fonts](https://fonts.google.com/), whose fonts are free and open source. 

### Social media icons
The icons we are using are provided by [Font Awesome](https://fontawesome.com/icons?d=gallery). The icons at Font Awesome are free to use and open source. Since we are using Facebook's, Twitter's and Instagram's brand icons with the sole purpose of giving the visitors of Floristgården a direct link to their social medias, our usage adheres to Font Awesome's [Free License](https://fontawesome.com/license/free) which states: "**All brand icons are trademarks of their respective owners. The use of these trademarks does not indicate endorsement of the trademark holder by Font Awesome, nor vice versa. Please do not use brand logos for any purpose except to represent the company, product, or service to which they refer.**" 