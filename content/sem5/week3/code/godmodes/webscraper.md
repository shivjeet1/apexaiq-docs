---
layout: default
title: week 3 webscraper
---

# Release Scraper

A Selenium script that grabs version numbers, release dates, and download links from a target page. it uses firefox and dumps everything into a pandas dataframe, then saves to a csv.

## Setup

You need firefox installed on your system since it uses the standard firefox webdriver. make sure your python venv is active and the requirements are installed.

```bash
source ../../../../../jadu/bin/activate
pip install -r ../../../../../requirements.txt
```

## Run

```bash
python webscraper.py
```

```bash
python customscrape.py
```

## Output

The output is a csv file in the `../../output/` directory.

