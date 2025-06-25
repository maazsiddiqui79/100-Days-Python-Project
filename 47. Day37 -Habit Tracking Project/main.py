import requests
import datetime
#------------------------Creating a new user and api------------------------

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "Siddiqui-Maazzzzz-79"
USERNAME = "maazsiddiqui"

users_params = {
    "token": TOKEN, 
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint , json=users_params)
# print(response.text)

# ------------------------Creating a graph------------------------

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_params = {
    "id" : "graph01",
    "name" : "Daily Coding",
    "unit" : "Hours",
    "type" : "float",
    "color" : "ajisai"
}


headers_params ={
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers_params)
# print(response)
# print(response.text)

# ------------------------Adding Pixel------------------------
singlepixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph01"

date = str(datetime.datetime.now().strftime("%Y%m%d"))
print(date)

pixel_prams = {
    "date" : "20250418",
    "quantity" : "57"
}

response = requests.post(url=singlepixel_endpoint, json=pixel_prams, headers=headers_params)
print(response)
print(response.text)
print(singlepixel_endpoint)
# ------------------------Updating Pixel------------------------
# PUT /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph01/20250610"
update_pixel_prams = {
    # "date" : "20250610",
    "quantity" : "22"
}

# response = requests.put(url=update_endpoint, json=update_pixel_prams, headers=headers_params)
# print(response)
# print(response.text)


# ------------------------Deleting Pixel------------------------
# DELETE /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
del_date = "20250617"
delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph01/{del_date}"

# response = requests.delete(url=delete_pixel, headers=headers_params)
# print(response)
# print(response.text)


