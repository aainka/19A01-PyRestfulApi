
# -*- coding:utf-8 -*-

import bottle
import json
import mail_send
import file_api

mythings = {'망고종류','bb'}

@bottle.route('/')

def home_page():

    fruit = bottle.request.get_cookie("fruit")

    return bottle.template("hello_world",username="Andrew",things=mythings,like=fruit)

@bottle.post('/api/V1/mail')

def api_post():
    print("/api/V1:put ###################")
    body = bottle.request.body.read()
    print("BODY ="+body.decode("utf-8"))
    jsonObj = json.loads(body.decode("utf-8"))
    print("OBJ  ="+jsonObj[0].get("subject"))
    smtp_server='aainka@gmail.com'
    smtp_server_password='inka4723'
    print("MMMMMMMMMMMMMMMMMMMMMMMMMM")
    m_eMail =  mail_send.cEMail(smtp_server,smtp_server_password)
    
    toMail='jaeyoung.jeon@ericsson.com'
    Subject= jsonObj[0].get("subject")
    Message= jsonObj[0].get("message")
  
    m_eMail.send(toMail,Subject,Message)
    return jsonObj  

@bottle.get('/api/V1/file')

def api_file():
    dir = bottle.request.query.dir
    if dir != None and len(dir)>0:
        s = file_api.get_directory(dir)
        return s
    else :
        readfile = bottle.request.query.readfile
        return file_api.read_file(readfile)


@bottle.post('/favorite_fruits')

def favorite_fruits():

    fruit = bottle.request.forms.get('fruit')

    if(fruit == None or fruit==""):

        fruit="No Fruit Selected"

    bottle.response.set_cookie('fruit',fruit)

    return bottle.template("fruit.tpl",{'fruit':fruit})

 


bottle.run(host='0.0.0.0',port=9292)
