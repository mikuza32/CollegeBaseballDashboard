import concurrent.futures
import pandas as pd
from .scrapers.individual_BA import individual_batting_average
from .scrapers.individual_ERA import individual_earned_run_average
from .scrapers.individual_SLG import individual_slugging_percentage
from .scrapers.individual_WHIP import individual_walk_hits_innings_pitched

def scrape_pages(url_list, scraper_class, parse_method):
    data_frames = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {
            executor.submit(lambda url=url: getattr(scraper_class(url), parse_method)()): url
            for url in url_list
        }
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                df = future.result()
                data_frames.append(df)
            except Exception as exc:
                print(f"Error scraping the following url {url}: {exc}")
    if data_frames:
        return pd.concat(data_frames, ignore_index=True)
    return None

if __name__ == "__main__":
    from backend.scrapers.individual_BA import individual_batting_average
    batting_average_urls = [
        "https://www.ncaa.com/stats/baseball/d1/current/individual/200",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/200/p2",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/200/p3",
    ]
    batting_avg_df= scrape_pages(batting_average_urls, individual_batting_average, "parse_statistics")
    if batting_avg_df is not None:
        batting_avg_df = individual_batting_average.clean_data(batting_avg_df)
        print("Batting Stats: ")
        print(batting_avg_df.head())
    else:
        print("No individual batting average data has been scraped!")

    from backend.scrapers.individual_ERA import individual_earned_run_average
    era_urls = [
        "https://www.ncaa.com/stats/baseball/d1/current/individual/205",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/205/p2",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/205/p3",
    ]
    era_df = scrape_pages(era_urls, individual_earned_run_average, "parse_era_statistics")
    if era_df is not None:
        era_df = individual_earned_run_average.clean_data(era_df)
        print("ERA Stats: ")
        print(era_df.head())
    else:
        print("No ERA data scraped.")
    from backend.scrapers.individual_SLG import individual_slugging_percentage
    slugging_percentage_urls = [
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321/p2",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321/p3",
    ]
    slugging_df = scrape_pages(era_urls, individual_slugging_percentage, "parse_slg_statistics")
    if slugging_df is not None:
        slugging_df = individual_slugging_percentage.clean_data(slugging_df)
        print("SLG Stats: ")
        print(slugging_df.head())
    else:
        print("No Slugging Percentage data has been scraped")
    from backend.scrapers.individual_WHIP import individual_walk_hits_innings_pitched
    whip_urls = [
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321/p2",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321/p3",
    ]
    slugging_df = scrape_pages(era_urls, individual_walk_hits_innings_pitched, "parse_slg_statistics")
    if slugging_df is not None:
        slugging_df = individual_walk_hits_innings_pitched.clean_data(slugging_df)
        print("SLG Stats: ")
        print(slugging_df.head())
    else:
        print("No Slugging Percentage data has been scraped")