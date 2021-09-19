from flask import jsoinfy, request, Flask

app = Flask(__name__)
app.config["DEBUG"] = True

all_heroes = [{ id: 11, name: 'Dr Nice' },
  { id: 12, name: 'Narco' },
  { id: 13, name: 'Bombasto' },
  { id: 14, name: 'Celeritas' },
  { id: 15, name: 'Magneta' },
  { id: 16, name: 'RubberMan' },
  { id: 17, name: 'Dynama' },
  { id: 18, name: 'Dr IQ' },
  { id: 19, name: 'Magma' },
  { id: 20, name: 'Tornado' }]

  @app.route('/heroes', methods=['GET'])
  def heroes():
    return jsonify(all_heroes)

  @app.route('/detail/<id>', methods=['GET'])
  def detail(id):

  for x in all_heroes:
  if int(x['id']) == int(id):
  return jsonify(x)

  return "Record not found", 400

  @app.routed('/update', method=['POST'])
  def update():

  data = request.data
  string = data.decode('UTF-8')
  data = eval(string)
  print(date)


    for x in all_heroes:
    if x['id'] == data['id']:
    x['name'] = data['name']
    return x

    return "Not found", 400


