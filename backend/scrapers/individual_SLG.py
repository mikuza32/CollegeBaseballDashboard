import pandas as pd
from .scraper import scraper


class individual_slugging_percentage(scraper):
    def parse_slg_statistics(self):
        soup = self.get_soup()

        table = soup.find("table", class_="block-stats__stats-table")
        if not table:
            raise Exception("Could not retrieve table for Slugging Percentage")
        
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
        if "SLG PCT" in df.columns:
            df["SLG PCT"] = pd.to_numeric(df["SLG PCT"], errors="coerce")
        for col in ["G", "AB", "TB"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        return df

if __name__ == "__main__":
        url = "https://www.ncaa.com/stats/baseball/d1/current/individual/321"
        html = individual_slugging_percentage(url)
        df = scraper.parse_slg_statistics()
        df = individual_slugging_percentage.clean_data(df)

        expected_columns = ["Name", "G", "AB", "TB"]
        if all(col in df.columns for col in expected_columns):
            batting_stats = df[expected_columns]
            print(batting_stats.head())
        else:
            print("Could not find or print the various columns", df.columns)