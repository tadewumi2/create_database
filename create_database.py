import sqlite3

sql_statements = [
	"""CREATE TABLE IF NOT EXISTS projects (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	begin_date DATE,
	end_date DATE
);""",

"""CREATE TABLE IF NOT EXISTS tasks (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	priority INTEGER,
	project_id INTEGER NOT NULL,
	status_id INTEGER NOT NULL,
	begin_date DATE NOT NULL,
	end_date DATE NOT NULL,
	FOREIGN KEY (project_id) REFERENCES projects (id)
);"""
]

try:
	with sqlite3.connect('my.db') as conn:
		cursor = conn.cursor()
 	
		for statement in sql_statements:
 			cursor.execute(statement)

		conn.commit()

		print("Tables created successfully.")
except sqlite3.OperationalError as e:
	print("Failed to create tables:", e)

