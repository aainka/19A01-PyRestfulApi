# -*- coding:utf-8 -*-

import httplib2

host = "localhost:9292"

h= httplib2.HTTP(host)
h.putrequest("POST","/")
h.putheader("Host",host)
h.putheader("User-agent", "python-httplib")
h.endheaders()

returncode, returnmsg, headers = h.getreply()

if   returncode == 200  :
    f=h.getfile()
    print(f.read())