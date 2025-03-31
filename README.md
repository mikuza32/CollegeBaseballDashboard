# Welcome to my College Baseball Dashboard

## Summary

The College Baseball Dashboard application was developed to track four different individual statistics: Earned Run Average, Walk Hits per Innings Pitched, Batting Average, and Slugging Percentage. The application tracks the top 150 players in NCAA Division 1 with
the best results in those statistical categories.

---

## Key Questions and Features

- **How is the college baseball data retrieved so that it can be manipulated and displayed?**
  *This application utilizes the Python webscraping library called BeautifulSoup and a data analysis library called pandas. We use BeautifulSoup to carefully scrape the data needed from the ncaa.com website ethically, then using pandas to manipulate and
  format the data retrieved so that the data needed can be stored appropriately from the service layer.*

- **How is the data stored?**
  *This application uses a Firebase SDK as it is an efficient platform for this type of project, especially since we are only using the free tier services.*

- **RESTful API Development and Design**
  *We created endpoints using FastAPI that are retrieved from the applications frontend. The APIs use the backends service layer to fulfill the scraping, manipulating, and placing of the data retrieved into the FireStore DB.*

- **Interactive Dashboard**
  *For the frontend dashboards we used Next.js as the frontend framework, along with Chart.js library to consume the Firestore data and display them accordingly into bar charts and scatter plots. This allows the user to analyze the data accordingly to generate conclusions.

- **Caching on application**
  *This application uses in-memory caching to save resources for reads/writes on the free tier Firebase app. This reduces the amount of reads and writes a user uses when using the College Baseball Dashboard application*
