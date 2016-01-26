import pymysql

MY_SQL_PASSWD = "password1"
conn = pymysql.connect(host="127.0.0.1", user='root', passwd=MY_SQL_PASSWD, db='mysql') 


cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * from pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close() 