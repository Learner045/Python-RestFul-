from flask import Flask, jsonify, request, render_template

app2=Flask(__name__)

#from server's perspective
#GET-used to send data back to browser
#POST-used to receive data from browser

#our data
# to send it over to the internet we need JSON object as javascript can only understand text or JSON
#so we need to convert this data to JSON
stores=[

    {'name':'My Wonderful Store',
        'items':[
             {
             'name':'item1',
             'price':10
             }
        ]
     }
]

@app2.route('/')
def home():
   return render_template('index.html')

#bydefault app2.route() makes a GET req


#END POINTS will be as follows

#POST/store data:{name:}        #create a store
@app2.route('/store',methods=['POST'])
def create_store():
    request_data=request.get_json() #gets JSON data dicionary
    new_store={
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store<string:name>        #returns store eg http://127.0.0.1:5000/store/store_name
@app2.route('/store/<string:name>')
def get_store(name):
    #iterates over all stores, checks if names match and returns that store, or else err messg
    for store in stores:
        if store['name']==name:
            return jsonify(store)

    return jsonify({"message":"No store found!"})

#GET / store                    #returns list of stores
@app2.route('/store')
def get_stores():
    return jsonify({'stores':stores}) #we convert our data which is list to JSON dictionary

#POST /store<string:name>/item  #create item in store
@app2.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    #find the store and add item to its item list
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item) #directly return new item as its a dictionary

    return jsonify({"message": "No store found!"})

#GET /store<string:name>/item   #get all items of a store
@app2.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']}) #we convert this to dictionary becuz we cannot directly send list of items
    return jsonify({"message":"No store found!"})

app2.run(port=5000)

