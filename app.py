
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
web = "https://www.audible.com/search"
path = r"C:\Users\rahee\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(web)


audio_books = driver.find_elements(by='xpath',value='//li[contains(@class,"productListItem")]')

book_title = []
book_author =[]
book_length = []


for book in audio_books:    
    book_title.append(book.find_element(by='xpath',value='.//h3[contains(@class,"bc-heading")]').text)
    book_author.append(book.find_element(by='xpath',value='.//li[contains(@class,"authorLabel")]').text)
    book_length.append(book.find_element(by='xpath',value='.//li[contains(@class,"runtimeLabel")]').text)

books_df = pd.DataFrame({'title':book_title,'author':book_author,'length':book_length})
books_df.to_csv('books.csv',index=False)
driver.quit()