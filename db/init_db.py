import sqlite3

# Initialize a Database to use for local Dev.
# DB can be deleted and configured to MYSqlDb if setup on pc.



sqlite_file = 'todo.db'

task_table = """ CREATE TABLE IF NOT EXISTS task (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        task TEXT NOT NULL
                                    ); """
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Execute the queries to stage the data for commits
c.execute(task_table)

# commit the changes to the db and then close the connection
conn.commit()
conn.close()