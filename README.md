# KitapSepeti and KitapYurdu Web Data Scraper

This web scraper is designed to extract data from two server-side rendered websites, KitapSepeti and KitapYurdu. It
employs the Selenium and Beautiful Soup libraries to navigate these sites, retrieve raw data, reformat it, and
subsequently save it in a database. Please note that all timestamps used within this repository adhere to the UTC
standard to maintain consistency.

## Library Selection Strategy

Selecting the appropriate library for a web scraping project largely depends on the nature of the targeted website.
The 'requests' library is not applicable here, as the sites are server-side rendered and do not provide easily parsable
JSON data. Since network monitoring is unnecessary for this project, Selenium Wire is also not needed.

Selenium can be useful when a website requires UI interaction, which is not a requirement for our case. Additionally,
Selenium tends to be resource-intensive due to its browser-based operation, although its resource consumption can be
mitigated by running in headless mode.

In light of these considerations, this project employs lxml/Beautiful Soup for one site and Selenium for the other. This
strategy not only fulfills the project requirements, but also demonstrates the flexibility of the code architecture.

## Embracing the Template Design Pattern

While the scraping process may vary slightly from one website to another, it generally follows a similar pattern:
initialize the scraper, access the website, navigate to the desired category, fetch raw data, and format it. The final
steps remain consistent: save the data to a database or update an existing product's price.

Applying the Template Design pattern allows for flexibility in the choice of scraping libraries, meaning we are not
constrained to using a specific tool if another may be more suitable for a particular website.

This scraper also includes category mapping to bridge the gap between Smart Maple's category names and those of
Kitapsepeti and Kitapyurdu.

### Accepted category names for Kitapsepeti:

- Kids
- General
- Literature
- Exams
- Turkish_Literature
- Sci-Fi
- Anime

### Accepted category names for Kitapyurdu:

- Kids
- General
- Literature
- Exams
- English
- Non-literary

Please be aware that any discrepancies in category parameters will trigger a "No Category Found" exception.

## Key Features

This scraper does not segregate data from the two websites into separate collections, a practice deemed unnecessary for
this project. On subsequent runs, the scraper adds the old price to an array labeled 'historical prices'. Preserving
past prices can prove beneficial for tracking competition and conducting data analysis.

To avoid potential inconsistency, data classes are preferred over dictionaries for the serialization and deserialization
process.

During scraping, various errors may occur. However, it's crucial to distinguish between errors caused by the scraper and
those resulting from product unavailability. You can find the exceptions in `core/errors.py`.

This project has been developed following the Test-Driven Development (TDD) approach.

**Note:** Given the vast quantity of books on KitapSepeti, the number of pages to scrape has been set to 5 to simplify
testing. To scrape all pages, remove line 65 in `scrapers/kitapsepeti`.

**Note:** Docker image creation was intended but i have no access for an amd64 laptop (chrome does not exist for arm64)
**Note:** i am using python3.11
**Note:** i am using chrome V.115 (no chrome driver needed)

A GitHub Action is in place to conduct testing of the code before each deployment.

## Setup

Make sure you have Google Chrome installed on your system.

Run:

```bash
bash setup.sh
```

## Starting the code:

Run:

```bash
bash start.sh
```



