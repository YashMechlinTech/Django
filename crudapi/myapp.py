import requests,json

URL='http://127.0.0.1:8000/'



def get_data(id=None):
    data={}
    if(id is not    None):
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data )
    print(r.json())
 
def post_data():
    data={
        'name':'Ravi',
        'roll':104,
        'city':'Dhanbad'
    }

    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    print(r.json)



post_data()
get_data(1)