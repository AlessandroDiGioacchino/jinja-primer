
# Jinja Primer

A beginner-friendly project for learning Jinja2 templating in Python.

This repository includes small, practical examples that demonstrate how to
render dynamic text and HTML using templates, how to work with control flow,
and how to integrate Jinja with Flask.

This project follows the concepts introduced in the Real Python tutorial:

https://realpython.com/primer-on-jinja-templating

## Overview

The examples in this repo cover:

- basic Jinja template rendering
- template variables and expressions
- conditional logic and loops
- generating multiple files from templates
- HTML report generation
- template inheritance with Flask

## Repository structure

- `first_template.py` — a minimal Jinja example using a string template
- `templates/` — shared base templates and examples
- `control-flow-jinja/` — project that renders personalized message files and a student results page
- `jinja-with-flask/` — simple Flask app using Jinja templates

## Getting started

### 1. Install dependencies

```bash
pip install jinja2 flask
```

### 2. Run the basic example

```bash
python first_template.py
```

### 3. Run the control flow example

```bash
cd control-flow-jinja
python write_message.py
```

This generates message files such as:

- `message_frieda.txt`
- `message_fritz.txt`
- `students_results.html`

### 4. Run the Flask example

```bash
cd jinja-with-flask
python app.py
```

Then open the app in your browser at:

```text
http://127.0.0.1:5000/
```

## Example learning goals

By working through this project, you will learn how to:

- render dynamic text in Jinja templates
- use `for` loops and `if` statements in templates
- pass data from Python into templates
- reuse templates with inheritance
- build simple web pages with Flask

## Notes

This repo is intentionally small and educational, making it suitable for
beginners who want to understand the fundamentals of Jinja templating without
getting lost in larger frameworks or app structures.
