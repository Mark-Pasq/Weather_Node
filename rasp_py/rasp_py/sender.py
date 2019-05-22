import time
import requests
import json
import MySQLdb
DATABASE_ADDRESS = "localhost"
DATABASE_USER = "project"
DATABASE_PASSWD = "project"
DATABASE_DB = "project"
def get_connection():
	global DATABASE_ADDRESS, DATABASE_USER, DATABASE_PASSWD, DATABASE_DB
	return MySQLdb.connect(host = DATABASE_ADDRESS, user = DATABASE_USER, passwd = DATABASE_PASSWD, db = DATABASE_DB)
def delete_by_id(id):
	id = str(int(id))
	print "deleting id = ", id
	conn = get_connection()
	cur = conn.cursor()
	cur.execute("DELETE FROM `serial_data` WHERE `id` = " + id)
	conn.commit()
	conn.close()
def main():
	print "Sender is ON!"
	print "Use http://159.203.78.94/rpilog/receiver_with_db to view the data!!"
	while True:
		try:
			database_connection = get_connection()
			cur = database_connection.cursor()
			cur.execute("SELECT `id`, `content`, `timestamp` FROM `serial_data` ORDER BY `id` LIMIT 0, 10;")
			all_results = cur.fetchall()
			cur.close()
			database_connection.close()
			result_to_send = {}
			for r in all_results:
				if r[0] is not None and r[1] is not None:
					result_to_send[r[0]] = "[" + unicode(str(r[2]), errors="replace") + "]" + unicode(str(r[1]), errors="replace")
			if len(result_to_send) == 0:
				continue
			request = requests.post("http://159.203.78.94/rpilog/receiver_with_db/receive.php", data={"data": json.dumps(result_to_send)})
			print "imhere222"
			if request.status_code == 200:
				response_json_array = json.loads(request.text)
				print "got response from the server.."
				print response_json_array
				for key in response_json_array:
					delete_by_id(key)
		except Exception as e:
			print str(e)
			pass
		time.sleep(1)
main()

