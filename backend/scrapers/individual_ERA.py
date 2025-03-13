import pandas as pd
from .scraper import scraper


class individual_earned_run_average(scraper):
    def parse_era_statistics(self):
        soup = self.get_soup()

        table = soup.find("table", class_="block-stats__stats-table")
        if not table:
            raise Exception("Could not find table for ERA stats")
        
        thead = table.find("thead", class_="tableFloatingHeaderOriginal") or table.find("thead")

        if thead is None:
            thead = table.find("thead")
        if thead is None:
            raise Exception("No table header found")

        headers = [th.get_text(strip=True) for th in thead.find_all("th")]

        tbody = table.find("tbody")
        if not tbody:
            raise Exception("Could not find table body needed for ERA stats")    
        
        rows = []
        for tr in tbody.find_all("tr"):
            cols = [td.get_text(strip=True) for td in tr.find_all("td")]
            rows.append(cols)
        
        df = pd.DataFrame(rows, columns=headers)
        return df
    
    @staticmethod
    def clean_data(df):
        if "ERA" in df.columns:
            df["ERA"] = pd.to_numeric(df["ERA"], errors="coerce")
        for col in ["APP", "IP", "R", "ER"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        return df 

if __name__ == "__main__":
    url = "https://www.ncaa.com/stats/baseball/d1/current/individual/205"
    html = individual_earned_run_average(url)
    df = scraper.parse_era_statistics()
    df = individual_earned_run_average(df)

    expected_columns = ["Name", "APP", "IP", "R", "ER", "ERA"]
    if all(col in df.columns for col in expected_columns):
        era_stats = df[expected_columns]
        print(era_stats.head())
    else:
        print("Could not find various columns", df.columns)        