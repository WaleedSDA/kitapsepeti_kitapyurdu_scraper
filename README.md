# Kitapsepeti and Kitapyurdu Scraper

This project scrapes data from two server-side rendered websites, KitapSepeti and KitapYurdu. The scraper utilizes
Scrapy and Beautiful Soup libraries to navigate the sites, extract raw data, format it, and save it to a database.

All date/times in this repository are in UTC timezone for consistency.

## Choosing the Right Library

The right library for a web scraping project depends heavily on the nature of the target website. For these websites,
using 'requests' library isn't feasible since the sites are server-side rendered (I mean we do not get the data as json
to parse it easily). Selenium Wire isn't needed either
because we don't need to monitor the network.

Selenium is useful when a website needs UI interaction, but it's not required in our case. Plus, Selenium tends to be
resource-heavy since it runs a browser (we still can make it run in headless mood).

Thus, this project uses lxml/beautiful soup for one site and selenium for the other. Both are great tools for the job
and
allows me to demonstrate the versatility of my code architecture.

## Template Design Pattern

The scraping process for most websites follows a similar pattern but differs in implementation: set up the scraper, open
the website, navigate to the desired category, fetch raw data, and format it. The last steps are always the same: saving
the data to a database or updating an existing product's price.

Using the Template Design pattern enables flexibility in our choice of scraping library. We're not forced to use one
tool when another might be better suited for a particular website.

there is mapping for categories, i believe that your company will have a united naming for categories that is different
than the websites, so there is mapping from "Smart Maple" naming to Kitapsepeti and Kitapyurdu naming.

accepted category names for Kitapsepeti are:
Kids
General
Literature
Exams
Turkish_Literature
sci-fi
Anime

accepted category names for Kitapyurdu are:
Kids
General
Literature
Exams
English
non-literary

mistakes you do in the parameter of the category will rais a no category found exception.

