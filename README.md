# Audible Web Scraper using Selenium (Python)

## 📌 Project Overview

This project is a simple web scraper built using Python and Selenium.  
It extracts audiobook data from Audible’s search page, including:

- Book Title  
- Author Name  
- Book Length (Runtime)

The scraped data is saved into a CSV file.

This project is created for beginners learning:
- Web Scraping
- Selenium
- XPath
- Browser Automation

---

## 🛠 Technologies Used

- Python
- Selenium
- Google Chrome
- ChromeDriver
- Pandas (used only to save data)

---

## 📂 Project Structure
```
audible-web-scraper/
│
├── scraper.py # Main scraping script
├── books.csv # Output file (generated after running script)
└── README.md # Project documentation
```


---

## ⚙️ Prerequisites

### 1️⃣ Python Installed

Check version:
```bash
python --version


pip install selenium pandas

path = r"C:\path\to\chromedriver.exe"
```

## 🚀How to Run the Project

Clone the repository:
```
git clone https://github.com/your-username/audible-web-scraper.git
```

Go to project directory:
```
cd audible-web-scraper
```

Run the script:
```
python scraper.py
```

Check books.csv for results
