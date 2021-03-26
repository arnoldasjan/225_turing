# Etsy Scraper
## Turing 2.2.5 Final Subproject
In this project I had to create a scraper to scrape data of some products from chosen marketplace.
I chose Etsy and with this scraper I can scrape data about product listings such as `title`, `price`, `rating`, 
`reviews count`, `item url`, and `image url` with selected keyword.

## Setup instructions
In order to use this scraper with your own database your `create_connection.py` file should look like this:
```
import psycopg2


def connect():
    """
    Connects to the database
    :return: returns the connection to the database
    """
    connection = psycopg2.connect(
        database="your_database_name",
        user="your_user_name",
        password="your_password",
        host="your_host",
        port="your_port(usually: 5432)"
    )
    connection.autocommit = True
    return connection
```

## Scraping
If you are using the program for the first time you should make sure that main program runs
`execute_fresh_start()` function first. After that you can add new keywords and its data to the existing tables.

To scrape products information insert preferred keywords to `keywords_list` variable inside
`execute_new_keyword_scrape()` function inside the `main.py` file and run the program.

So the existing function:

```
def execute_new_keyword_scrape() -> None:
    keywords_list = ['tshirts for moms day', 'funny mom tshirts', 'personalised tshirt for mother']
    scraper(keywords_list, 10)
    export_data()
```

Would scrape 10 ( you can modify this number inside call to `scraper(keywords_list, number_of_results_wanted)` )
product listings returned for each keyword in `keywords_list` and it would export all the data fetched from the databse and export it to csv file. 

## Main Technologies
`Python 3.8` - python version used.

`BeautifulSoup4` - package used for scraping.

You can find the rest of the packages used inside `requirements.txt` file.


## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


