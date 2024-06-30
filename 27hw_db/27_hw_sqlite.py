import sqlite3

connection = sqlite3.connect('27datab_sqlite.db')

cursor = connection.cursor()

cursor.execute(
    """
    create table if not exists books (id integer, title text, author text, year integer, genre text);
    """
)
connection.commit()

# cursor.execute(
#     """
#     insert into books (id, title, author, year, genre) values (1, 'Barbie', 'Greta Gerwig', 2023, 'comedy');
#     """
# )

# cursor.execute(
#     """
#     insert into books (id, title, author, year, genre) values (2, 'Frankenstein', 'Mary Shelley', 2022, 'horror');
#     """
# )
#
# cursor.execute(
#     """
#     insert  into books (id, title, author, year, genre) values (3, 'Middlemarch', 'George Eliot ', 2018, 'history');
#     """
# )

# cursor.execute(
#     """
#     insert  into books (id, title, author, year, genre) values (4, 'Butter', 'Asako Yuzuki', 2024, 'detective');
#     """
# )
#
# cursor.execute(
#     """
#     insert  into books (id, title, author, year, genre) values (5, 'The Bat', 'Jo Nesbo', 2013, 'detective');
#     """
# )
# connection.commit()


# cursor.execute(
#     """
#     select title from books where author='Jo Nesbo';
#     """
# )
# results = cursor.fetchall()
# print(results)


# cursor.execute(
#     """
#     update books set year=2014 where id=5;
#     """
# )
# connection.commit()


cursor.execute(
    """
    delete from books where id=4;
    """
)
connection.commit()


connection.close()