from database_operations import create_tables, drop_tables
from scraping import scraper
from database_operations import export_data


def execute_fresh_start() -> None:
    """
    Executes all the scraper abilities from droping tables to creating
    to scraping data to inserting it to the database and exporting to csv.
    It is recommended for first time use
    """
    drop_tables()
    create_tables()
    keywords_list = ['personalised gifts', 'personalised gifts for moms', 'moms day gifts']
    scraper(keywords_list, 3000)
    export_data()


def execute_new_keyword_scrape() -> None:
    """
    Works with already existing tables and adds new data to it for selected keywords.
    Great for continous use and comparisons between results by the query timestamp
    """
    keywords_list = ['tshirts for moms day', 'funny mom tshirts', 'personalised tshirt for mother']
    scraper(keywords_list, 10)
    export_data()


if __name__ == "__main__":
    execute_new_keyword_scrape()
