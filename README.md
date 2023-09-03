TikTok Comment Liker
Overview

This project is a Python script that automates the process of liking comments on TikTok posts. It uses Selenium WebDriver for web scraping and automation, along with multi-threading to optimize the URL collection process. Additionally, the script provides cookie handling to maintain login state across sessions.
Getting Started
Prerequisites

    Python 3.x
    Firefox Browser
    GeckoDriver (Firefox WebDriver for Selenium) | https://github.com/mozilla/geckodriver/releases

Installation

    Clone this repository:

git clone https://github.com/yourusername/tiktok-comment-liker.git

Navigate into the project folder:

cd tiktok-comment-liker

Install the required packages:

    pip install -r requirements.txt

Setup

    Cookie Setup:
        Install the Cookie Editor add-on for Firefox. | https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/
        Navigate to TikTok's website and log in to your account.
        Use Cookie Editor to export all cookies and save them into a cookies.json file in the project directory.

    Collecting URLs:
        Run first.py:

    python first.py

    When prompted, choose whether to overwrite or add URLs to your existing file. Overwriting will replace the file, while adding will append new URLs to it.

Liking Comments:

    Run main.py:

        python main.py

        The script will prompt you for a one-time verification. Complete this step.

    Enjoy! The script will automatically like comments based on the URLs you've provided.

Usage

To run the script, execute the following commands in order:

    For URL collection:


python first.py

For liking comments:

    python main.py

License

This project is free for personal use. For commercial use, do not use without prior permission. For more details, see the LICENSE.md file.
