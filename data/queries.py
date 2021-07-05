from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_top_15_shows():
    return data_manager.execute_select(f'''SELECT shows.*, STRING_AGG(genres.name, ', ') AS genre
  FROM shows JOIN show_genres ON shows.id =show_genres.show_id 
    JOIN genres ON genres.id=show_genres.genre_id 
    GROUP BY shows.id 
    ORDER BY shows.rating DESC;''')


def get_show(id):
    return data_manager.execute_select(f"""SELECT * FROM shows WHERE id = '{id}'""")


def get_seasons(id):
    return data_manager.execute_select(f"""SELECT seasons.* FROM
     seasons JOIN shows ON seasons.show_id=shows.id 
     WHERE show_id='{id}' ORDER BY season_number;""")


def new_user(email, password):
    return data_manager.execute_select(f"""INSERT INTO users (email, pw) VALUES('{email}', '{password}')""")


def genre_for_one_show(show_id):
    return data_manager.execute_select(f'''SELECT shows.*, STRING_AGG(genres.name, ', ') AS genre
    FROM shows JOIN show_genres ON shows.id =show_genres.show_id 
      JOIN genres ON genres.id=show_genres.genre_id
      WHERE shows.id = '{show_id}'
      GROUP BY shows.id 
      ORDER BY shows.rating DESC;''')


def get_actor_by_show(show_id):
    return data_manager.execute_select(f"""SELECT STRING_AGG(actors.name, ', ') AS actor FROM actors
JOIN show_characters ON show_characters.actor_id = actors.id
JOIN shows ON shows.id = show_characters.show_id 
WHERE shows.id= '{show_id}' 
GROUP BY shows.id;""")


def get_all_actors():
    return data_manager.execute_select('''SELECT * FROM actors ''')


def search_actors(actor_name):
    return data_manager.execute_select("""SELECt * FROM actors
     WHERE actors.name LIKE  %s """, [actor_name + '%'])


def write_new_users(email, password):
    return data_manager.execute_dml_statement(
        "INSERT INTO users (email, password) VALUES(%(email)s, %(password)s);", {"email": email, "password": password})


def get_used_emails():
    return data_manager.execute_select("SELECT email FROM users")


def get_all_users_email_and_password():
    return data_manager.execute_select("SELECT email, password FROM users;")


def insert_favourite(show_id, email):
    return data_manager.execute_dml_statement(f"""UPDATE users SET (favourites) 
    WHERE users.email = '{email}'
     """)



def get_users_favourites(user_email):
    return data_manager.execute_select('''SELECT favourites 
    FROM users WHERE email = %(user_email)s''', {'user_email': user_email})
