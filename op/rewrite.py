import pymysql
from flask import Flask,request,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app,supports_credentials=True,resources=r'/*')

@app.route('/finder',methods=['POST'])
def finder():
    db = pymysql.connect(host="localhost", user="root", password="2004523", db="kkko")
    cursor = db.cursor()
    if request.method == "POST":
        cursor.execute("select id,object,describ,contect from finder")
        data=cursor.fetchall()
        temp={}
        result=[]
        if(data!=None):
            for i in data:
                temp["id"]=i[0]
                temp["object"]=i[1]
                temp["describ"]=i[2]
                temp["contect"]=i[3]
                result.append(temp.copy())
            print(f"已递交给前端：{result}")
            return jsonify(result)
        else:
            print("无对应结果")
            return jsonify([])

@app.route('/giver',methods=['POST'])
def giver():
    db = pymysql.connect(host="localhost", user="root", password="2004523", db="kkko")
    cursor = db.cursor()
    if request.method == "POST":
        cursor.execute("select id,object,address,contect,upload_image from giver")
        data=cursor.fetchall()
        temp={}
        result=[]
        if(data!=None):
            for i in data:
                temp["id"]=i[0]
                temp["object"]=i[1]
                temp["address"]=i[2]
                temp["upload_image"]=i[4]
                temp["contect"]=i[3]
                result.append(temp.copy())
            print(f"已递交给前端{result}")
            return jsonify(result)
        else:
            print("无对应结果")
            return jsonify([])

@app.route('/giver/select',methods=['POST'])
def giverfind():
    db = pymysql.connect(host="localhost", user="root", password="2004523", db="kkko")
    cursor = db.cursor()
    if request.method == "POST":
        cursor.execute("select id,object,address,contect,upload_image from giver")
        data=cursor.fetchall()
        target=request.form.get("keyword")
        temp={}
        result=[]
        if(data!=None):
            for i in data:
                if i[1]==target:
                    temp["id"]=i[0]
                    temp["object"]=i[1]
                    temp["address"]=i[2]
                    temp["upload_image"]=i[4]
                    temp["contact"]=i[3]
                    result.append(temp.copy())
                if(result!=[]):
                    print(f"已递交给前端{result}")
                    return jsonify(result)
                else:
                    temp["id"]='NULL'
                    temp["object"]=target
                    temp["address"]='NULL'
                    temp["upload_image"]='NULL'
                    temp["contect"]='NULL'
                    result.append(temp.copy())
                    print(f"数据库中未检索到{target}")
                    return jsonify(result)
        else:
            print("无对应结果")
            return jsonify([])

@app.route('/finder/select',methods=['POST'])
def finderfind():
    db = pymysql.connect(host="localhost", user="root", password="2004523", db="kkko")
    cursor = db.cursor()
    if request.method == "POST":
        cursor.execute("select id,object,describ,contect from finder")
        target=request.form.get("keyword")
        data=cursor.fetchall()
        temp={}
        result=[]
        if(data!=None):
            for i in data:
                if i[1]==target:
                    temp["id"]=i[0]
                    temp["object"]=i[1]
                    temp["describ"]=i[2]
                    temp["contect"]=i[3]
                    result.append(temp.copy())
            if(result!=[]):
                print(f"已递交给前端：{result}")
                return jsonify(result)
            else:
                temp["id"]='NUKK'
                temp["object"]=target
                temp["describ"]='NULL'
                temp["contect"]='NULL'
                result.append(temp.copy())
                print(f"数据库中未检索到{target}")
                return jsonify(result)
        else:
            print("无对应结果")
            return jsonify([])

db=pymysql.connect(host="localhost",user="root",password="2004523",db="kkko")

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
    db.close()
    print("Good Bye !")