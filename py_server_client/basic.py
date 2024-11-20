import requests

endpoint="http://127.0.0.1:8000/api"

get_response=requests.get(endpoint,json={"jsondata":"hello world"},params={"params":123})

print(get_response.text)#python dictionary printing 

print(get_response.json()['message'])#json printing. 


#point is that the normal http request will return the HTML response 
#while the rest api request will return the json response instead. 

#javascript object notation is similiar to the python dictionary
#json key  is null in the python dictionary while in the json the json is the none in the response. 
