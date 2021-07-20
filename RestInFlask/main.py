from flask import Flask, jsonify, request, json
app = Flask(__name__)

stores = [
    {
        'name': 'store1',
        'items': [
            {
                'name': 'flowers',
                'price': '100'
            }
        ]
    },
    {
        'name': 'store2',
        'items': [
            {
                'name': 'books',
                'price': '500'
            }
        ]
    }
]

##----------------------READ-----------##
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify({'store_name':store['name'],'code':200})
    return jsonify({'message':'Store not found','code':404})



@app.route('/store/<string:name>/items', methods=['GET'])
def get_store_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify({'store_items':store['items'],'code':200})
    return jsonify({'message':'Store not found','code':404})


##------------------------CREATE----------------##
@app.route('/store', methods=['POST'])
def create_store():
    req_data = request.get_json()
    new_store={
        'name': req_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify({'store':new_store, 'code':202})

@app.route('/store/<string:name>/items', methods=['POST'])
def create_store_items(name):
    for store in stores:
        if(store['name'] == name):
            req_data = request.get_json()
            new_item = {
                'name':req_data['name'],
                'price':req_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'item':new_item, 'code':202})
    return jsonify({'message':'Store not found','code':404})


##----------------DELETE-----------##
@app.route('/store/<string:name>', methods=['DELETE'])
def delete_store(name):
    for i in range(len(stores)):
        if(stores[i]['name'] == name):
            del stores[i]
            return jsonify({'message':'Deleted','code':204})
    return jsonify({'message':'Store not found','code':404})



##--------------UPDATE-------------##
@app.route('/store/<string:name>', methods=['PUT'])
def update_store_name(name):
    req_data = request.get_json()
    for i in range(len(stores)):
        if(stores[i]['name'] == name):
            stores[i]['name'] = req_data['newName']
            return jsonify({'message':'Updated','code':200})
    return jsonify({'message':'Store not found','code':404})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
