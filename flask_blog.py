from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '027f5ce927ba58e1709c9942adb5f5a9'

posts = [
    {
        'author': 'KOD',
        'title': 'Blog Post 1',
        'content': 'First post Content',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Ohene',
        'title': 'Blog Post 2',
        'content': 'Second post Content',
        'date_posted': 'April 20, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
