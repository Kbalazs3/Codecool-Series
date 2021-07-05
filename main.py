from flask import Flask, render_template, url_for, request, jsonify, session
from data import queries
import bcrypt

app = Flask('codecool_series')


app.secret_key = 'cucumber'


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route("/shows/most-rated/<pagenum>")
def most_rated_shows(pagenum):
    top_rated_shows = queries.get_top_15_shows()
    return render_template("most_rated_shows.html", top15=top_rated_shows, pgnum=pagenum)


@app.route("/reg-data", methods=['GET', 'POST'])
def get_reg_data():
    reg_email_and_password = request.get_json(force=True)
    email = reg_email_and_password['regEmail']
    password = reg_email_and_password['regPassword']
    hashed_password = hash_passwords(password)
    used_emails = queries.get_used_emails()
    for re in used_emails:
        if re['email'] == email :
            return jsonify('used')
    queries.write_new_users(email, hashed_password)
    print()
    print('OKay')


def hash_passwords(password):
    hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password.encode('utf-8'), hashed_bytes_password)


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register_page.html')


@app.route("/login-data", methods=['GET', 'POST'])
def get_log_in_data():
    login_email_and_password = request.get_json(force=True)
    log_email = login_email_and_password['logInEmail']
    log_password = login_email_and_password['logInPassword']
    registered_users_email_and_password = queries.get_all_users_email_and_password()
    for i in registered_users_email_and_password:
        if log_email == i['email']:
            if verify_password(log_password, i['password']):
                session['email'] = log_email
                generated_username = log_email.split('@')[0]
                return jsonify('Welcome Dear ' + generated_username + '\n You have logged in!')


@app.route("/logged-in-status")
def logged_in_checker():
    if session:
        return jsonify(session['email'])
    elif not session:
        return jsonify('not_logged_in')


@app.route("/login")
def login_page():
    return render_template("login_page.html")


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    print(session)
    session.pop('email')
    print()
    print(session)
    if not session:
        return jsonify('Logout')


@app.route("/tv-show/<id>")
def show(id):
    seasons = queries.get_seasons(id)
    one_show = queries.genre_for_one_show(id)
    actor = queries.get_actor_by_show(id)
    return render_template("show.html", show=one_show, seasons=seasons, actor=actor)


@app.route('/api/actors')
def api_actors():
    return jsonify(queries.get_all_actors())


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template("search.html")


@app.route("/search/actors", methods=['POST'])
def search_actors():
    actor_name = request.get_json(force=True)
    print(actor_name)
    search_result = queries.search_actors(actor_name)
    return jsonify(queries.search_actors(actor_name))


@app.route("/send-favourite", methods=['POST'])
def favourite_show():
    favourite = request.get_json(force=True)
    print(favourite)
    queries.insert_favourite(favourite['favouriteId'], session['email'])

    return jsonify('Favourite')


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
