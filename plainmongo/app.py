from flask import Flask
from flask_restful import Api
from config import app,mongo
from flask import request
from flask import jsonify
from flask_restful import Resource
from bson.json_util import dumps
import json
from bson import json_util
from bson import ObjectId
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

api = Api(app)

class createRoles(Resource):
    def get(self):
        obj = (mongo.db.roles.find())
        data=json.loads(json_util.dumps(obj))
        return ({"data":data,"sucess":True,"message":"roles feteched sucessfully "})

    def post(self):
        data = request.get_json()
        obj=mongo.db.roles.insert_one(data)
        obj2=json.loads(json_util.dumps(data))
        return({"data":obj2,"sucess":True,"message":"roles sucessfully inserted in mongodb"})

class updateRoles(Resource):

    def get(self,id):
        obj = (mongo.db.roles.find({"_id":ObjectId(id)}))
        data=json.loads(json_util.dumps(obj))
        return ({"data":data,"sucess":True,"message":"roles feteched sucessfully "})

    def put(self,id):
        obj = request.get_json()
        print(obj)
        data=mongo.db.roles.update_one({"_id":ObjectId(id)}, {"$set":obj})
        obj2=json.loads(json_util.dumps(obj))
        return({"data":obj2,"sucess":True,"message":"roles sucessfully updated in mongodb"})

    def delete(self,id):
         db_response = mongo.db.roles.delete_one({"_id":ObjectId(id)})
         return "sucessfully deleted id in mongodb"

class signup(Resource):

    def post(self):
        data = request.get_json()
        email=data["email"]
        password=data["password"]
        hash_password = generate_password_hash(password)
        dict={"email":email,"password":hash_password}
        obj=mongo.db.users.insert_one(dict)
        obj2=json.loads(json_util.dumps(dict))
        return({"data":obj2,"sucess":True,"message":"users sucessfully inserted in mongodb"})

class signin(Resource):
    def post(self):
        data = request.get_json()
        email=data["email"]
        password=data["password"]
        print(email)
        email_obj=mongo.db.users.find_one_or_404({"email":email})
        hashpassword=email_obj["password"]
        print(hashpassword)
        if email_obj is not None:
             if check_password_hash(hashpassword,password):
                   return {"success":True,
                        'data':data,
                        'message': 'logined successfully'
                        }
             else:
                return({"success":False,"message": "Invalid Password"})
        else:
             return({"success":False,"message": "Invalid UserName"})

class users(Resource):

    def get(self):
        obj = (mongo.db.users.find())
        data=json.loads(json_util.dumps(obj))
        return ({"data":data,"sucess":True,"message":"roles feteched sucessfully "})


    def post(self):
        data = request.get_json()
        obj = (mongo.db.roles.find_one_or_404({"name":"bhanu"}))
        data["roles_id"]=obj
        print(data)
        obj=mongo.db.users.insert_one(data)

class getuserid(Resource):

    def get(self,id):
        obj = (mongo.db.users.find({"_id":ObjectId(id)}))
        data=json.loads(json_util.dumps(obj))
        return ({"data":data,"sucess":True,"message":"roles feteched sucessfully "})
        #obj2=json.loads(json_util.dumps())

api.add_resource(createRoles, '/addrole')
api.add_resource(updateRoles, '/updaterole/<string:id>')
api.add_resource(getuserid, '/getuserid/<string:id>')
api.add_resource(signup, '/signup')
api.add_resource(signin, '/signin')
api.add_resource(users, '/users')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
