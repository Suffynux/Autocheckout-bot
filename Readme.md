# Amazon Selenium Automation

This repository contains Python scripts that use Selenium to automate interactions with the Amazon website. The scripts perform the following actions:

## 1. Search and Select Item

`amazon_search_and_select.py`:

- Opens the Chrome browser.
- Navigates to Amazon's homepage.
- Waits for the search box to be present.
- Enters a search query, in this case, "playstataion portal."
- Clicks the search button.
- Selects the first item from the search results, assumed to be the playstation portal.

## 2. Amazon Sign-In Automation

`amazon_sign_in_automation.py`:

- Opens the Chrome browser.
- Navigates to Amazon's homepage.
- Clicks the "Sign in" link.
- Finds and interacts with the email/phone number input field, prompting the user to enter their email.
- Clicks the "Continue" button.
- Finds and interacts with the password input field, prompting the user to enter their password.
- Clicks the "Sign-In" button.

## Prerequisites

Before running the scripts, make sure you have the following installed:

- Python
- Selenium library
- ChromeDriver (compatible with your Chrome browser version)

