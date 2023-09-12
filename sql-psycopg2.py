import psycopg2


# connect to "chinook" database, can add other credentials like pwords etc here
connection = psycopg2.connect(database="chinook")


# build cursor object of the database, set/list/similar to array, 
# data we query becomes part of this object, must iterate using for loop
cursor = connection.cursor()


# Query 1 
# cursor.execute('SELECT * FROM "Artist"')

# Query 2
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 use python string placeholder and 
# define what should be in single quotes in a list [""] with double quotes after end '
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])


# Query 4, both do the same thing, both together only returns 1 result
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 51')


# Query 5
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])


# Query 6
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# Query 7
# cursor.execute('SELECT * From "Track" Where "Composer" = %s', ["Foo Fighters"])


# Query 8, doesnt return anything at all
cursor.execute('SELECT * From "Track" Where "Composer" = %s', ["test"])


# fetch the results (multiple), returns as tuple ie (51, 'Queen')
results = cursor.fetchall()


# fetch the result (single), prints each column individually ie 51 (new line) Queen
# results = cursor.fetchone()

#close the connection, once fetched end the connection
connection.close()


# print results by iterating over 
for result in results:
    print(result)
