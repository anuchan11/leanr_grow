from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
website = driver.get("https://web.whatsapp.com/")

name = input("Enter the name: ")
message = input("Enter the message: ")

user = driver.find_element_by_xpath('//span[@title="Amma😘😍🥀"]')
#user = driver.find_element_by_xpath('//span[@title="Appanna"]')
user.click()
msg_box = driver.find_element_by_class_name('_3uMse')

for i in range(20):
    msg_box.send_keys(message)
    button = driver.find_element_by_class_name('_1U1xa')
    button.click()

import cx_Oracle

con = cx_Oracle.connect(mode=cx_Oracle.SYSDBA)
cur = con.cursor()

cur.execute("select user from dual")
rows = cur.fetchall()
#cur.fetchone()

for row in rows:
    print(row)

con.close()























