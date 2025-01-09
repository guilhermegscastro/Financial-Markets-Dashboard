# Financial News (Web Scraping)


 Monte Carlo Simulation: <br/>
<img src="https://imgur.com/mtHIB5i.png" height="60%" width="130%" alt="Valuation_VaR_MonteCarlo"/>


Project Description

The News Aggregator Dashboard is a web-based application designed to gather and display news articles from multiple sources in an organized, user-friendly interface. By leveraging web scraping techniques, this project collects articles on themes such as technology and economy from a variety of international news outlets. The data is presented in a structured and visually appealing manner using Python's Dash framework.

This project showcases skills in data collection, web development, and data visualization, making it an ideal demonstration of technical and analytical capabilities in building robust tools for real-time information aggregation.

Features

Automated News Collection:

The application scrapes news articles from prominent sources like CNN, CNBC, Financial Times, and more.

Themes include economy, technology, artificial intelligence, and deep-dive analysis.

Centralized Dashboard:

News articles are displayed in a well-structured dashboard using Dash and Dash Bootstrap Components.

The layout includes distinct sections for U.S.-based and international news, ensuring comprehensive coverage.

Efficient Scraping Implementation:

Utilizes Selenium WebDriver with Beautiful Soup for dynamic and static content extraction.

Stores aggregated news data in a CSV file (news.csv) for easy accessibility and further analysis.

Responsive and User-Friendly Design:

Built using Dash Bootstrap Components, the dashboard is optimized for different screen sizes and provides a seamless user experience.

Technologies Used

Python:

Core language for scripting and development.

Libraries: Selenium, Beautiful Soup, Pandas, Dash, Dash Bootstrap Components.

Web Scraping Tools:

Selenium WebDriver for handling dynamic web pages.

Beautiful Soup for HTML parsing.

Data Storage:

Aggregated data stored in news.csv for modularity and reusability.

Web Framework:

Dash for creating interactive web applications.

Project Structure

├── dashboard.py
│   Defines the dashboard layout and integrates the scraped data for visualization.
├── data_news.py
│   Contains functions for scraping news articles from various sources.
├── news.csv
│   A CSV file generated from scraped data, containing headlines, subheadings, links, and themes.

How It Works

Data Collection:

The data_news.py script contains specialized functions to scrape articles from:

CNN

CNBC

Financial Times

China Daily

Valor Internacional

Fortune

Each function handles a specific source and theme.

Data Integration:

The scraping_news() function consolidates the collected data into a single DataFrame.

The data is saved in news.csv for dashboard consumption.

Dashboard Visualization:

The dashboard.py script builds the interactive dashboard.

News themes are presented in tabs (e.g., U.S. news, world news) for easy navigation.

Key Highlights for Recruiters

End-to-End Development: Demonstrates ability to design, develop, and deploy a functional application.

Web Scraping Expertise: Extracts structured data from diverse sources efficiently.

Data Visualization Skills: Creates an intuitive user interface with Dash for real-time insights.

Modular Design: Ensures maintainability and scalability with clear separation of concerns.

How to Run

Install Dependencies:

Clone the repository and install required Python libraries:

pip install -r requirements.txt

Run the Scraping Script:

Execute data_news.py to collect the latest articles:

python data_news.py

Launch the Dashboard:

Start the dashboard server with dashboard.py:

python dashboard.py

View the Application:

Open a web browser and navigate to http://localhost:8051.
