import pandas as pd
from .scraper import scraper


class individual_batting_average(scraper):
    def parse_statistics(self):
        soup = self.get_soup()

        table = soup.find("table", class_="block-stats__stats-table")
        if not table:
            raise Exception("Could not retrieve data for Batting Averages")
        
        thead = table.find("thead", class_="tableFloatingHeaderOriginal") or table.find("thead")

        if thead is None:
            thead = table.find("thead")
        if thead is None:
            raise Exception("No table header found")


        headers = [th.get_text(strip=True) for th in thead.find_all("th")]


        tbody = table.find("tbody")
        if not tbody:
            raise Exception("Could not find table body")
        

        rows = []
        for tr in tbody.find_all("tr"):
            cols = [td.get_text(strip=True) for td in tr.find_all("td")]
            rows.append(cols)

        df = pd.DataFrame(rows, columns=headers)
        return df

    @staticmethod
    def clean_data(df):
        if "BA" in df.columns:
            df["BA"] = pd.to_numeric(df["BA"], errors="coerce")
        for col in ["G", "AB", "H"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        return df

if __name__ == "__main__":
        url = "https://www.ncaa.com/stats/baseball/d1/current/individual/200"
        html = individual_batting_average(url)
        df = scraper.parse_statistics()
        df = individual_batting_average.clean_data(df)

        expected_columns = ["Name", "G", "AB", "H", "BA"]
        if all(col in df.columns for col in expected_columns):
            batting_stats = df[expected_columns]
            print(batting_stats.head())
        else:
            print("Could not find or print the various columns", df.columns)
        