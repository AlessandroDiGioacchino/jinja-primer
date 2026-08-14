
from jinja2 import Environment, FileSystemLoader

def main():
  max_score = 100
  test_name = 'Python challenge'
  students = [
    { 'name': 'Sandrine', 'score': 100 },
    { 'name': 'Gergeley', 'score': 87 },
    { 'name': 'Frieda', 'score': 92 },
    { 'name': 'Fritz', 'score': 40 },
    { 'name': 'Sirius', 'score': 75 }
  ]

  environment = Environment( loader=FileSystemLoader( 'templates/' ) )
  template = environment.get_template( 'message.txt' )

  for student in students:
    filename = f"message_{student[ 'name' ].lower()}.txt"
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )

    with open( filename, mode='w', encoding='utf-8' ) as message:
        message.write( content )
        print( f'… wrote {filename}' )

  results_filename = 'students_results.html'
  results_template = environment.get_template( 'results.html' )

  content = {
    'students': students,
    'max_score': max_score,
    'test_name': test_name
  }

  #   Note that the keys of the `students` dictionary […] match the template
  # variables in `message.txt`

  with open( results_filename, mode='w', encoding='utf-8' ) as results:
    results.write( results_template.render( content ) )
    print( f'… wrote {results_filename}')

if __name__ == '__main__':
  main()
