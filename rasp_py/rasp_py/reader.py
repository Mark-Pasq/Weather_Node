import time
import MySQLdb
import serial
DATABASE_ADDRESS = "localhost"
DATABASE_USER = "project"
DATABASE_PASSWD = "project"
DATABASE_DB = "project"
def get_connection():
	global DATABASE_ADDRESS, DATABASE_USER, DATABASE_PASSWD, DATABASE_DB
	return MySQLdb.connect(host = DATABASE_ADDRESS, user = DATABASE_USER, passwd = DATABASE_PASSWD, db = DATABASE_DB)
def write_result(content):
	conn = get_connection()
	cursor = conn.cursor()
	base_statement = "INSERT INTO `serial_data` VALUES (NULL, %s, %s);"
	cursor.execute(base_statement, [content, int(time.time())])
	cursor.close()
	conn.commit()
	conn.close()
def get_serial_console():
	return serial.Serial('/dev/ttyUSB0', 9600, timeout=4)
def main():
	while True:
		try:
			console = get_serial_console()
			content = ""
			while console.inWaiting:
				text = console.readline()
				if "[data]" in text:
					content = ""
				content += text
				print text
				if "[/data]" in text:
					print "reached the last part of data, packing into the db..."
					write_result(content)
					content = ""
				time.sleep(0.01)
		except:
			pass
		time.sleep(0.01)
main()

