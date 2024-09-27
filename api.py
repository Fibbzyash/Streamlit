from flask import  Flask , jsonify , request



app = Flask(__name__)


items = [
    {
        "name": "item1",
        "price": 100
    },
    {
        "name": "item2",
        "price": 200
    }
]

@app.route('/')
def homes():
    return "Welcome to the Flask API!"

#GET reterive all the data from the server

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

#get: reterive a specific item from the server
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404


#post: add a new item to the server
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"message": "Bad request"}), 400
    new_item = {
        "id": items[-1]['id'] + 1,
        "name": request.json['name'],
        "description":request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item)

#put: update an existing item on the server
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)



if __name__ == '__main__':
    app.run(debug=True , port=5001)