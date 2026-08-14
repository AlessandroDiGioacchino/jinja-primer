
from flask import Flask, render_template

app = Flask( __name__ )

@app.route( '/' )
def home():
  return render_template( 'base.html', title='Jinja and Flask' )
  #   By default, Flask expects your templates in a `templates/` directory.
  # Therefore, you don’t need to set the template directory explicitly. When
  # you provide `base.html` to `render_template()`, Flask knows where to look
  # for your template.

if __name__ == '__main__':
  app.run( debug=True )
