
import requests,json
false = False

def dk(authorization,ThreadId,name):
    url_post="https://api.jielong.co/api/Thread/EditCheckInRecord"
    headers={
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-us,en",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Content-Type":"application/json",
        "Connection":"keep-alive",
        "Host":"api.jielong.co",
        'authorization':authorization,
    }

    data={
        "Id":0,"ThreadId":ThreadId,"Number":"","Signature":name,"RecordValues":[{"FieldId":1,"Values":[],"Texts":[],"OtherValue":"","MatrixValues":[],"Files":[],"Scores":[],"HasValue":false},{"FieldId":2,"Values":[],"Texts":[],"OtherValue":"","MatrixValues":[],"Files":[],"Scores":[],"HasValue":false}],"DateTarget":"","IsNeedManualAudit":false,"MinuteTarget":-1,"IsNameNumberComfirm":false
        }

    r=requests.post(url_post,headers=headers,data=json.dumps(data))
    print(r.text)
    return r.text

def main_handler(event,context):
    return dk()

if __name__=='__main__':
    dk(authorization,ThreadId,name)   #authorization
