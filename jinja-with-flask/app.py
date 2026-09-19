
from flask import Flask, render_template


app = Flask( __name__ )


@app.route( '/' )
def home():
  return render_template( 'base.html', title='Jinja and Flask' )
  #   By default, Flask expects your templates in a `templates/` directory.
  # Therefore, you don’t need to set the template directory explicitly. When
  # you provide `base.html` to `render_template()`, Flask knows where to look
  # for your template.


max_score = 100
test_name = 'Python Challenge'
students = [
  { 'name': 'Sandrine',  'score': 100 },
  { 'name': 'Gergeley', 'score': 87 },
  { 'name': 'Frieda', 'score': 92 },
  { 'name': 'Fritz', 'score': 40 },
  { 'name': 'Sirius', 'score': 75 }
]


@app.route('/results')
def results():
  context = {
    'title': 'Results',
    'students': students,
    'test_name': test_name,
    'max_score': max_score,
  }

  #   Flask's render_template() accepts only one positional argument, which is
  # the template name. Any other arguments must be keyword arguments. So you
  # have to unpack your dictionary with two asterisks (**) in front of context.
  #   With the asterisk operators, you're passing the items of context as
  # keyword arguments into render_template().
  return render_template( 'results.html', **context )


if __name__ == '__main__':
  app.run( debug=True )
