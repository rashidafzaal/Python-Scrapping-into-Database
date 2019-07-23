#Task 1
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

basic_data_table = soup.find("table", {"class": "itemlist"});
basic_data_cells = basic_data_table.findAll('a')
my_filtered_array = []

for i in range(3,len(soup.findAll('a'))-20):
	print("\n")
	indexVal = basic_data_cells[i].text.strip()
	if indexVal.find(" ago") == -1 and indexVal.find(".com") == -1 and indexVal.find(".co") == -1 and indexVal.find(".io") == -1  and indexVal.find(".ai") == -1 and indexVal.find("-") == -1 and indexVal.find("/") == -1 and indexVal.find("–") == -1 and indexVal.find("More") == -1:
		my_filtered_array.append(str(basic_data_cells[i].text.strip()))
	else:
		print("")
#=========================== Saving into Database ===========================

print(my_filtered_array)
db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
cursor = db.cursor()
sql = "INSERT INTO arbisoft (title) VALUES (%s)"
try:
    cursor.executemany(sql, my_filtered_array)
    db.commit()
except:
    db.rollback()