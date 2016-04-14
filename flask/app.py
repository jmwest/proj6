from flask import Flask, render_template, session
from controllers import ember_api
from extensions import mysql
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Secret key for cookie authentication
app.secret_key = 'rkrjjwkx1or'

# Initialize Flask file upload path
app.config['UPLOAD_FOLDER'] = 'static/images/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'bmp', 'gif'])

# Initialize MySQL database connector
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'project1'
mysql.init_app(app)

# Register the controllers

app.register_blueprint(controllers.album)
app.register_blueprint(controllers.albums)
app.register_blueprint(controllers.pic)
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.user)
app.register_blueprint(controllers.login)
app.register_blueprint(controllers.logout)
app.register_blueprint(controllers.wikipedia)
app.register_blueprint(controllers.ember_api)


# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)
