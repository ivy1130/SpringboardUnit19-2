from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """Return homepage."""

    return render_template("home.html", form = story.prompts)

@app.route('/story')
def show_story():
    """Return madlib story filled in."""

    madlib = story.generate(request.args)
    return render_template("story.html", madlib = madlib)

    # answers = dict()
    # for prompt in story.prompts:
    #     answers[prompt] = request.args[prompt]

    # return story.generate(answers)