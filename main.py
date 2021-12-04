import dimchik_mysql_connection

database_name = "hard"
sql_object = dimchik_mysql_connection.DimchikMysqlConnection()

# Create a database
sql_object.create_database(database_name)

# Use a database
sql_object.use_database(database_name)

# Create a table
table_name = 'video_cards'
query = "(id MEDIUMINT NOT NULL auto_increment," \
        "card_name varchar (30), " \
        "gpu varchar (30), " \
        "frequency varchar (30)," \
        "memory_value varchar (30)," \
        "memory_type varchar (30)," \
        "primary key (id))"
sql_object.create_table(table_name, query)

# Insert into a table video_cards
columns = "(card_name, gpu, frequency, memory_value, memory_type)"
query = "('Nvidia GeForce RTX 3090',        'GA102',        1400,   '24GB', 'GDDR6X'),\
    ('AMD Radeon RX 6800 XT',           'Navi 21',      1825 ,  '16GB', 'GDDR6' ),\
    ('Nvidia GeForce RTX 3080',         'GA102',        1440,   '10GB', 'GDDR6X'),\
    ('AMD Radeon RX 6800',              'Navi 21',      1700,   '16GB', 'GDDR6'),\
                   ('Nvidia Titan RTX',                'TU102',        1350,   '11GB', 'GDDR6'),\
                   ('Nvidia GeForce RTX 3070',         'GA104',        1500,   '8GB',  'GDDR6'),\
                   ('Nvidia Titan V',                  'GV100',        1200,   '12GB', 'HBM2'),\
                   ('Nvidia GeForce RTX 2080 Super',   'TU104',        1650,   '8GB',  'GDDR6'),\
                   ('Nvidia GeForce RTX 2080',         'TU104',        1515,   '8GB',  'GDDR6'),\
                   ('Nvidia Titan Xp',                 'GP102',        1405,   '12GB', 'GDDR5X'),\
                   ('Nvidia GeForce RTX 2070 Super',   'TU104',        1605,   '8GB',  'GDDR6'),\
                   ('AMD Radeon VII',                  'Vega 20',      1400,   '16GB', 'HBM2'),\
                   ('Nvidia GeForce GTX 1080 Ti',      'GP102',        1480,   '11GB', 'GDDR5X'),\
                   ('AMD Radeon RX 5700 XT',           'Navi 10',      1605,   '8GB',  'GDDR6'),\
                   ('Nvidia GeForce RTX 2070',         'TU106',        1410,   '8GB',  'GDDR6'),\
                   ('AMD Radeon RX 5700',              'Navi 10',      1465,   '8GB',  'GDDR6'),\
                   ('Nvidia GeForce RTX 2060 Super',   'TU106',        1470,   '8GB',  'GDDR6'),\
                   ('AMD Radeon RX Vega 64',           'Vega 10',      1274,   '8GB',  'HBM2'),\
                   ('AMD Radeon RX 5600 XT',           'Navi 10',      1375,   '6GB',  'GDDR6'),\
                   ('Nvidia GeForce GTX 1080',         'GP104',        1607,   '8GB',  'GDDR5X'),\
                   ('Nvidia GeForce RTX 2060',         'TU106',        1365,   '6GB',  'GDDR6'),\
                   ('AMD Radeon RX Vega 56',           'Vega 10',      1156,   '8GB',  'BM2'),\
                   ('Nvidia GeForce GTX 1070 Ti',      'GP104',        1607,   '8GB',  'GDDR5'),\
                   ('Nvidia GeForce GTX 1660 Ti',      'TU116',        1365,   '6GB',  'GDDR6'),\
                   ('Nvidia GeForce GTX 1660 Super',   'TU116',        1530,   '6GB',  'GDDR6'),\
                   ('Nvidia GeForce GTX 1070',         'GP104',        1506,   '8GB',  'GDDR5'),\
                   ('Nvidia GeForce GTX 980 Ti',       'GM200',        1000,   '6GB',  'GDDR5'),\
                   ('Nvidia GeForce GTX 1660',         'TU116',        1530,   '6GB',  'GDDR'),\
                   ('AMD Radeon RX 590',               'Polaris 30',   1469,   '8GB',  'GDDR5'),\
                   ('Nvidia GeForce GTX 1650 Super',   'TU116',        1530,   '4GB',  'GDDR6')"
sql_object.insert_to_table(table_name, columns, query)

# Create a table processors
table_name = 'processors'
query = "(id MEDIUMINT NOT NULL auto_increment," \
        "processor_name varchar (30), " \
        "cores varchar (30), " \
        "threads varchar (30)," \
        "cpu varchar (30), " \
        "primary key (id))"
sql_object.create_table(table_name, query)

# Insert into a table processors
columns = "(processor_name , cores, threads, cpu)"
query = "('Intel Core i9-12900K',16,24,''), \
    ('Intel Core i9-11900K',8,16,''), \
    ('Intel Core i7-12700K',12,20,''), \
    ('AMD Ryzen 9 5900X',12,24,''), \
    ('Intel Core i5-12600K',10,16,''), \
    ('AMD Ryzen 9 5950X',16,32,''), \
    ('AMD Ryzen 5 5600X',6,12,''), \
    ('AMD Ryzen 7 5800X',8,16,''), \
    ('Intel Core i7-11700K',8,16,''), \
    ('Intel Core i9-10900K',10,20,''), \
    ('Intel Core i9-10850K',10,20,''), \
    ('Intel Core i5-11600K',6,12,''), \
    ('Intel Core i5-11400',6,12,''), \
    ('Intel Core i7-10700K',8,16,''), \
    ('Intel Core i9-10980XE',18,36,''), \
    ('Intel W-3175X',28,56,''), \
    ('Ryzen 7 5700G',8,16,''), \
    ('Intel Core i9-9900KS',8,16,''), \
    ('Intel Core i7-10700/F',8,16,''), \
    ('Intel Core i5-10600K',6,12,''), \
    ('Intel Core i7-9700K',8,8,''), \
    ('Intel Core i9-9900K / F',8,16,''), \
    ('AMD Ryzen 9 3950X',16,32,''), \
    ('AMD Threadripper 3970X',32,64,''), \
    ('AMD Threadripper 3960X',24,48,''), \
    ('AMD Ryzen 5 5600G',6,12,''), \
    ('AMD Ryzen 7 3800XT',8,16,''), \
    ('AMD Threadripper 3990X',64,128,''), \
    ('AMD Ryzen 9 3900XT',12,24,''), \
    ('AMD Ryzen 9 3900X',12,24,''), \
    ('Intel Core i9-9980XE',18,36,''), \
    ('AMD Ryzen 9 3900',12,24,''), \
    ('AMD Ryzen 7 3700X',8,16,''), \
    ('AMD Ryzen 7 3800X',8,16,''), \
    ('AMD Ryzen 5 3600XT',6,12,''), \
    ('AMD Ryzen 5 3600',6,12,''), \
    ('Intel Core i9-7960X',16,32,''), \
    ('Intel Core i7-8700K',6,12,''), \
    ('AMD Ryzen 5 3600X',6,12,''), \
    ('AMD Ryzen 3 3300X',4,8,''), \
    ('Intel Core i5-9600K',6,6,''), \
    ('AMD Threadripper Pro 3995WX',64,128,''), \
    ('Intel Core i5-8600K',6,6,''), \
    ('Intel Core i7-8700',6,12,''), \
    ('Intel Core i7-8086K',6,12,''), \
    ('Intel Core i5-9400 / i5-9400F',6,6,'')"
sql_object.insert_to_table(table_name, columns, query)


# Show databases

# Show databases

sql_object.show_databases()

# Describe a table videocards
table_name = "video_cards"
sql_object.describe_table(database_name, table_name)

# Describe a table processors
table_name = "processors"
sql_object.describe_table(database_name, table_name)

# Show row/rows in table/tables
sql_object.show_table_in_database(database_name)
print(f"Trying to delete the row with id = 8 in table {table_name}")

# Delete a row/rows
condition = "id = 8"
sql_object.delete_table_row(database_name, table_name, condition)
print(f"Check for deleted row with id = 8 in table {table_name}")
sql_object.show_table_in_database(database_name, table_name="processors WHERE 6 < id AND id < 10")

# Update
set_condition = "cores = 100"
where_condition = "processor_name = 'Intel Core i9-12900K'"

sql_object.update(table_name, set_condition, where_condition)

sql_object.update(table_name, set_condition, where_condition)

print("Check for update a row ...")
sql_object.show_table_in_database(database_name, table_name=f"processors WHERE {where_condition}")

# Join
table_left_name = "video_cards"
table_right_name = "processors"
condition_left = "processors.id"
condition_right = "video_cards.id"
join_type = "join"
sql_object.join_tables(table_left_name, table_right_name, join_type, condition_left, condition_right)
join_type = "inner join"
sql_object.join_tables(table_left_name, table_right_name, join_type, condition_left, condition_right)
join_type = "left join"
sql_object.join_tables(table_left_name, table_right_name, join_type, condition_left, condition_right)
join_type = "right join"
sql_object.join_tables(table_left_name, table_right_name, join_type, condition_left, condition_right)

# Drop a table
sql_object.drop_table(database_name, table_name)
table_name = "video_cards"
print(sql_object.is_table_exist(database_name, table_name))
table_name = "processors"
print(sql_object.is_table_exist(database_name, table_name))
print(sql_object.is_table_exist(database_name, table_name))
table_name = "processors"
print(sql_object.is_table_exist(database_name, table_name))


# Check a database
print(sql_object.is_database_exist(database_name))

# Drop a database
sql_object.drop_database(database_name)

# Check a database
print(sql_object.is_database_exist(database_name))

del sql_object
