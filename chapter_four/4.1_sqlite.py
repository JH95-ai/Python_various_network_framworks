#connerct Msql
import MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='handsomehua',charset='utf8')
cur=conn.cursor()
print(conn)
print(cur)


cur.close()
conn.close()