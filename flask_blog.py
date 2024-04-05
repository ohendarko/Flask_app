from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
