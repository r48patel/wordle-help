#!/usr/bin/env python3.7
from flask import Flask, render_template, flash
from forms import SearchForm
import os
from flask_wtf import CSRFProtect
from wordle import get_possible_word_list

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['WTF_CSRF_ENABLED'] = False
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    is_validated = form.validate_on_submit()

    if not is_validated:
        for error in form.errors:
            flash(f'Error: {form.errors[error][0]}', 'error')
        return render_template("welcome.html", title="wordle-help", form=form)
    data = get_possible_word_list(form.contains.data, form.excludes.data, form.known_position.data, form.wrong_position.data)
    return render_template("index.html", title="Possible Words", word_list=data)


@app.context_processor
def utility_functions():
    def print_in_console(message):
        print("LOG: " + str(message))

    return dict(console_log=print_in_console)


if __name__ == '__main__':
    app.run(debug=True)
