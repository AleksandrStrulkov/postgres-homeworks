"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

EMPLOYEES = "north_data/employees_data.csv"
CUSTOMERS = "north_data/customers_data.csv"
ORDERS = "north_data/orders_data.csv"

connect = psycopg2.connect(host="localhost", database="north", user="postgres", password="1247")

try:
	with connect:
		with connect.cursor() as cursor:
			with open(EMPLOYEES, 'r') as csvfile:
				reader = csv.reader(csvfile)
				next(reader)
				for row in reader:
					cursor.execute(
							"INSERT INTO employees (employee_id,"
							"first_name,"
							"last_name,"
							"title,"
							"birth_date,"
							"notes)"
							"VALUES (%s, %s, %s, %s, %s, %s)", row)


finally:
	connect.close()

