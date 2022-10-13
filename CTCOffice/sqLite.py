import sqlite3

# Run this script to create tables within ctcOffice database and initialize some data

connection = sqlite3.connect("ctcOffice.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS track_blocks (
  Block_Number int NOT NULL,
  Line varchar(45) NOT NULL,
  Section varchar(45) DEFAULT NULL,
  Maintenance tinyint DEFAULT NULL,
  Infrastructure varchar(45) DEFAULT NULL,
  Failure_State varchar(45) DEFAULT NULL,
  Switch_Position tinyint DEFAULT NULL,
  Occupancy tinyint DEFAULT NULL,
  Crossing tinyint DEFAULT NULL,
  PRIMARY KEY (Block_Number,Line));""")

cursor.execute("""CREATE TABLE IF NOT EXISTS throughput (
                Line varchar(45) NOT NULL,
                throughput decimal(5,2) DEFAULT NULL,
                PRIMARY KEY (Line));""")

# cursor.execute("INSERT INTO throughput VALUES ('Red', 0);")
# cursor.execute("INSERT INTO throughput VALUES ('Green', 0);")
cursor.execute("INSERT INTO throughput VALUES ('Blue', 0);")

connection.commit()


