from flask import Flask,request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from datetime import datetime ,timedelta
import crypto2
import data

key=data.key
server_ip=data.server_ip
null=data.null

db_connect = create_engine('sqlite:///ProjectDB.db')
app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "hi"


class CheckSite(Resource):
    def get(self,HostName,save):
        try:
            conn = db_connect.connect()
            query = conn.execute("select * from Websites where HostName=? ",(crypto2.des(HostName,key),))
            result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
            if not result['data']:
                if save=="true" and request.user_agent.browser =="chrome":
                    conn.execute("insert into Websites values('{0}','{1}','{2}',NULL,NULL,NULL)".format((crypto2.des(HostName,key)),(crypto2.des("False",key)),0))
                    conn.execute("insert into CoverURL values('{0}',NULL)".format((crypto2.des(HostName,key))))
                return {'Trustable':"not found"}
            else:
                return  decrypt(result['data'][0])
        except:
            return {'Trustable':"ERROR"}

class getResult(Resource):
    def get(self,HostName):
        try:
            conn = db_connect.connect()
            query = conn.execute("select * from Websites where HostName=? ",(crypto2.des(HostName,key),))
            result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
            if not result['data']:
                return {'Trustable':"not found"}
            else:
                return  decrypt(result['data'][0])
        except:
            return {'Trustable':"ERROR"}

class GetCheckList(Resource):
    def get(self):
        try:
            ipReq=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            if(ipReq==server_ip ):
                conn = db_connect.connect()
                query = conn.execute("select HostName ,xpath from Websites where xpath IS NOT NULL ")
                result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
                if not result['data']:
                    return {'data':[]}
                else:
                    return  decrypt(result)
            else:
                return {'data':"ERROR"}
        except:
            return {'data':"ERROR"}

class GetURL(Resource):
    def get(self):
        try:
            conn = db_connect.connect()
            query = conn.execute("select HostName from Websites where xpath IS NULL ")
            result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
            if not result['data']:
                return {'data':[]}
            else:
                return  decrypt(result)
        except:
            return {'data':"ERROR"}


class setXpath(Resource):
    def post(self):
        try:
            DATA=request.json
            if "dani1212"== DATA.get('pass'):
                HostName = DATA.get('HostName')
                Xpath = DATA.get('Xpath')
                FullName = DATA.get('FullName')
                conn = db_connect.connect()
                conn.execute("UPDATE CoverURL SET FullName =? WHERE HostName=?", (crypto2.des(FullName,key),crypto2.des(HostName,key),))
                conn.execute("UPDATE Websites SET xpath =? WHERE HostName=?", (crypto2.des(Xpath,key),crypto2.des(HostName,key),))
                return {'msg':"Save"}
            else:
                return {'msg':str(DATA.get('pass'))}
        except:
            return {'msg':"ERROR"}

class DelURL(Resource):
    def post(self):
        try:
            DATA=request.json
            if "dani1212"== DATA.get('pass'):
                HostName = DATA.get('HostName')
                conn = db_connect.connect()
                conn.execute("UPDATE CoverURL SET FullName = null WHERE HostName=?", (crypto2.des(HostName,key),))
                return {'msg':"delete"}
            else:
                return {'msg':"ERROR"}
        except:
            return {'msg':"ERROR"}

class GetFullURL(Resource):
    def post(self):
        try:
            today= (datetime.today()+ timedelta(days=1)).strftime('%Y-%m-%d')
            More3Day =(datetime.today()+ timedelta(days=4)).strftime('%Y-%m-%d')
            DATA=request.json
            HostName = DATA.get('HostName')
            conn = db_connect.connect()
            query = conn.execute("select FullName from CoverURL where HostName=? and  FullName IS NOT NULL ",(crypto2.des(HostName,key),))
            result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
            if not result['data']:
                return {'data':""}
            else:
                return {'data':decrypt(result['data'][0]["FullName"]).replace("^today^",today).replace("^More3Day^",More3Day).replace("^TY^",today.split("-")[0]).replace("^TM^",today.split("-")[1]).replace("^TD^",today.split("-")[2]).replace("^MY^",More3Day.split("-")[0]).replace("^MM^",More3Day.split("-")[1]).replace("^MD^",More3Day.split("-")[2])}
        except:
            return {'data':"ERROR"}

class AcceptPassword(Resource):
    def post(self):
        try:
            if request.json.get('password')=="dani1212":
                return {'msg':"accept"}
            else:
                return {'msg':"ERROR"}
        except:
            return {'msg':"ERROR"}


class DB(Resource):
    def get(self):
        try:
            conn = db_connect.connect()
            query = conn.execute("select * from Websites")
            result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
            query = conn.execute("select * from CoverURL")
            result['data2']=[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
            return  decrypt(result)
        except:
            return {'msg':"ERROR"}

class SaveResult(Resource):
    def post(self):
        try:
            ipReq=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            if(ipReq==server_ip):
                DATA=request.json
                userAgent = DATA.get('userAgent')
                ip = DATA.get('ip')
                Result = str(DATA.get('Result'))
                HostName = DATA.get('HostName')
                conn = db_connect.connect()
                query = conn.execute("select * from Websites where HostName=? ",(crypto2.des(HostName,key),))
                result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
                if not result['data']:
                    return {"Status":"not fund"}
                elif (not ip or not userAgent) and Result=='False':
                    if result['data'][0]['Count']< -15:
                        conn.execute("DELETE  from Websites where HostName=? ",(crypto2.des(HostName,key),))
                        conn.execute("insert into Websites values('{0}','{1}','{2}',NULL,NULL,NULL)".format(crypto2.des(HostName,key),crypto2.des("False",key),0))
                    else:
                        conn.execute(" UPDATE Websites SET Count=? WHERE HostName=?", (result['data'][0]['Count']-1,crypto2.des(HostName,key),))#work
                    return {"Status":"unsuppert"}
                elif Result == 'False' and decrypt(result['data'][0]['Trustable']) == 'True':
                    conn.execute(" UPDATE Websites SET Trustable =?, ip=?, UserAgent=?,Count=0 WHERE HostName=?", (crypto2.des(Result,key),crypto2.des(ip,key),crypto2.des(userAgent,key),crypto2.des(HostName,key),))#TODO no work
                elif Result == 'True' and decrypt(result['data'][0]['Trustable']) == 'False':
                    if result['data'][0]['Count']>10:
                        conn.execute(" UPDATE Websites SET Trustable =? , Count=? WHERE HostName=?", (crypto2.des(Result,key),0,crypto2.des(HostName,key),))# TODO not work need check
                    else:
                        conn.execute(" UPDATE Websites SET Count=? WHERE HostName=?", (result['data'][0]['Count']+1,crypto2.des(HostName,key),))#work
                elif Result == 'False':
                    conn.execute(" UPDATE Websites SET ip=?,UserAgent=?,Count=0  WHERE HostName=?", (crypto2.des(ip,key),crypto2.des(userAgent,key),crypto2.des(HostName,key),))#work
                elif Result == 'True':
                    if ['data'][0]['Count']>10:
                        conn.execute(" UPDATE Websites SET Trustable =? , Count=? WHERE HostName=?", (crypto2.des(Result,key),0,crypto2.des(HostName,key),))# TODO not work need check
                    else:
                        conn.execute(" UPDATE Websites SET Count=? WHERE HostName=?", (result['data'][0]['Count']+1,crypto2.des(HostName,key),))#work
                return {"Status":"saved"}
            else:
                return {"Status":"ERROR"}
        except:
            return {"Status":"ERROR"}


def decrypt(object):
    if type(object)==type(1) or object ==null or object==None:
        return object
    if type(object)== type("string"):
        return str(crypto2.des_dicrypte(object,key))
    elif type(object)== type(list()):
        for i in range(len(object)):
            object[i]=decrypt(object[i])
        return object
    else:
        for obj in object.keys():
            object[obj]=decrypt(object[obj])
        return object


api.add_resource(CheckSite,'/CheckSite/<string:HostName>/<string:save>',methods={'GET'}) # user check site

api.add_resource(getResult,'/getResult/<string:HostName>',methods={'GET'}) # user get ip and user agent

api.add_resource(GetURL,'/GetURL',methods={'GET'}) # tech support get url for find
api.add_resource(DelURL,'/DelURL',methods={'POST'}) # tech support delete url

api.add_resource(setXpath,'/setXpath',methods={'POST'}) # tech support insert xpath for hostname
api.add_resource(AcceptPassword,'/accept',methods={'POST'}) # tech support insert password

api.add_resource(GetFullURL,'/GetFullURL',methods={'POST'}) # tech support get fullurl for find

api.add_resource(GetCheckList,'/GetCheckList',methods={'GET'}) # for async code check this site for bast ip and user agent
api.add_resource(SaveResult,'/SaveResult',methods={'POST'}) # for async code save in db result per this site for bast ip and user agent


api.add_resource(DB,'/showDB',methods={'GET'})#delete later for me show all db

if __name__ == '__main__':
     app.run()