
#=========================== import librarires ===========================
import requests
import MySQLdb
from bs4 import BeautifulSoup

#=========================== SQL Connection ===========================
HOST = "localhost"
USERNAME = "scraping_user"
PASSWORD = "1234"
DATABASE = "scraping_arbisoft"

#=========================== URL to Scrap ===========================
url_to_scrap = 'https://news.ycombinator.com/jobs'

#=========================== Get HTML and Parse ===========================
plain_html_text = requests.get(url_to_scrap)
soup = BeautifulSoup(plain_html_text.text, "html.parser")

#print(soup.prettify())

basic_data_table = soup.find("table", {"class": "itemlist"});
basic_data_cells = basic_data_table.findAll('td')


#=========================== Saving into Database ===========================

db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
cursor = db.cursor()
sql = "INSERT INTO test(test_name) VALUES ('{}')".format("hello")
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()