from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    contains = StringField('contains',
                           render_kw={"placeholder": "contains",
                                      "novalidate": "novalidate",
                                     })
    excludes = StringField('excludes',
                           render_kw={"placeholder": "excludes",
                                      "novalidate": "novalidate",
                                     })
    known_position = StringField('known_position',
                                 render_kw={"placeholder": "known positions",
                                            "novalidate": "novalidate",
                                           })
    wrong_position = StringField('wrong_position',
                                 render_kw={"placeholder": "wrong positions",
                                            "novalidate": "novalidate",
                                           })
    submit = SubmitField('Submit')
    # submit = SubmitField('Submit', render_kw={"onclick": "loading();"})