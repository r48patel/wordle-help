from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    contains = StringField('contains',
                           render_kw={"placeholder": "Enter letters to include",
                                      "novalidate": "novalidate",
                                     })
    excludes = StringField('excludes',
                           render_kw={"placeholder": "Enter letters to exclude",
                                      "novalidate": "novalidate",
                                     })
    known_position = StringField('known_position',
                                 render_kw={"placeholder": "Enter known position of Letters (format: LETTER-POSITION) (Space Seperated)",
                                            "novalidate": "novalidate",
                                           })
    wrong_position = StringField('wrong_position',
                                 render_kw={"placeholder": "Enter known letter wrong positions (format: LETTER-POSITION) (Space Seperated)",
                                            "novalidate": "novalidate",
                                           })
    submit = SubmitField('Submit', render_kw={"onclick": "loading();"})