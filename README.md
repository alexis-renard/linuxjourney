# Linux Journey

[Linux Journey](https://linuxjourney.com) is a site dedicated to making learning Linux fun and easy.

## Usage

The text content of Linux Journey has been made free to modify and distribute. For full license terms see: [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). This license does not include the images, site design and source code which is subject to All Rights Reserved.

## It's a fork !

As the courses content are under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/), this fork aims to parse the repository lessons in order to produce an XML schema that will be integrated into another learning plateform.

## Parser requirements

* Creating the HTML from the markdown : [python-markdown2](https://github.com/trentm/python-markdown2)
* Parsing the HTML : [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#### Install the requirements
```pip install -r parser/requirements.txt```
