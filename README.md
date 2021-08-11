# Ticket Checker

This is a basic script for sending an email notification when event tickets are released. 
The script uses uses [Selenium](https://selenium-python.readthedocs.io/) to run a Chrome browser in headless mode, load a web page and search for any number of strings within ghte HTML of that page.
If any of the given strings are found in the HTML, an email will be sent to the given recipients. 

### Usage

#### Requirements

To install the requirements, simply run:

```python -m pip install -r requirements.txt```

#### Setting up the GMail API

In order to use this script, you first need to generate credentials for the Google mail API. You can do this by running:

```python quickstart_mail.py``` 

This will generate a file called `token.json` which contains the credentials required to use the Google mail API. 

#### Installing ChromeDriver

The ChromeDriver can downloaded [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). You may need to match the ChromeDriver version to your version of Google Chrome. You will need to add the file to PATH.

#### Running the script
The script takes four arguments, with list arguments using a whitespace separator:
```
 -u | The URL of the web page to check
 -s | A list of strings to search for in the HTML
 -r | A list of email recipients
 -t | The time in seconds between each poll [default=60]
```
So, for example, if you wanted to check the Sisyphos website for tickets to an event on the 20th of August, you would want to run:

``` python check_tickets.py -u https://shopyphos.com/collections/tanzen -s "20. August" 20-august -r myself@email.com my_friends@email.com```

Viel Spaß!