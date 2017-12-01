#import requests library for making REST calls
import requests
import json
from xml_flowrule_diman import getFlowRule
from requests.auth import HTTPBasicAuth
import time

#specify url

headers = {
    'content-type': "application/xml",
    'accept': "application/xml",
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'postman-token': "83db35c9-c8b3-bcc0-8ecf-fda842638c3c"
    }

src = 1
dst = 255
cnt=1
for i in range(0,1):
    src+=1
    dst-=1
    if src==255:
            src=1
    if dst==1:
            dst=255

    payload = getFlowRule(cnt,src,dst,(i+1))
    cnt-=1

    url = 'http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:14721744633698189312/table/0/flow/' + str((i+1))

    start_time = time.time()
    response = requests.request("PUT", url, data=payload, headers=headers)
    end_time = time.time()
    diff = end_time - start_time

    #Print Response
    print(str(i) + " " + str(response.status_code
              ) + " " + str(response.reason) + " " + str(response.text))
    print(str(round(diff*1000,1)))
