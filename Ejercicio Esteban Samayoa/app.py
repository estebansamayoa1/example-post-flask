from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


app = Flask(__name__)
with open ('data.json')as json_file:
  jsonfile = json.load(json_file)


@app.route('/')
def index():
  template = env.get_template('index.html')
  return template.render(my_data = jsonfile['data'], headers = jsonfile['headers'])

@app.route('/crear', methods = ['GET', 'POST'])
def crear():
  if request.method == 'POST':
    _id = request.form['id']
    _type = request.form['type']
    _name = request.form['name']
    _image = request.form['image']
    _thumbnail = request.form['thumbnail']
    print (f'{_id} {_type} {_name} {_image} {_thumbnail}')

    jsonfile['data'].append({"Id":_id, "Type":_type, "Name":_name, "image":{"url":_image}, "thumbnail":{"url":_thumbnail}})
    return redirect(url_for('index'))
  template = env.get_template('form.html')
  return template.render()


@app.route('/info')
def info():
  return 'Nombre: Esteban Samayoa\nCarnet: 20200188\n, Edad: 19\n'


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
