import csv
import pymysql

from classes.review import Review

# Connect to the database
connection = pymysql.connect(host='localhost',
							 user='root',
							 password='yvaQEjfPZMRVxiJMZC6FyxsM',
							 db='scotchit',
							 charset='utf8',
							 cursorclass=pymysql.cursors.DictCursor)

with open('data/archive.csv', 'rb') as csvfile:
	reviewReader = csv.DictReader(csvfile, delimiter=',')
	for row in reviewReader:
		review = Review(row)

		try:
			with connection.cursor() as cursor:
				# Create a new record
				sql = "INSERT INTO `reviews` (`date`, `name`, `author`, `url`, `rating`, `region_style`, `price`, `body`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
				cursor.execute(sql, (review.getDatetime(), review.name, review.author, review.url, review.rating, review.region_style, review.price, review.getBody()))

			# connection is not autocommit by default. So you must commit to save
			# your changes.
			connection.commit()

		finally:
			connection.close()

		exit()