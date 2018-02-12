from flask import Flask, request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

items=[]

#http status codes: 200-ohk data returned successfully  404-not found 201-data created
# 202-accepted, when creation of obj is delayed and is done after latency behind the scnees
class Item(Resource):
    def get(self,name):
        item=next(filter(lambda x: x['name']==name,items),None) #filter func returns list of matching items, next gives us 1st item
        return item, 200 if item else 404

    def post(self,name):
        if next(filter(lambda x: x['name']==name, items),None):
            return {"message":"item with {} elready exists ".format(name)},400
        else:
            data=request.get_json(force=True) #if JSON payload is not proper/body does not have JSON then this gives an err..to avoid err..use force
            item={'name':name, 'price':data['price']}
            items.append(item)
            return item

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item, '/item/<string:name>') #we are receiving name directly from url into our method
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)