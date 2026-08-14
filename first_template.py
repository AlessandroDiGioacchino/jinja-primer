
import jinja2

def main():
  environment = jinja2.Environment()
  template = environment.from_string( 'Hello, {{ name }}!' )
  template.render( name='world' )

if __name__ == '__main__':
  main()
