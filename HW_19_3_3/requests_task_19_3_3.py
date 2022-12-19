import requests
import json

# POST /pet
param_dict = {"id": 0, "category": {"id": 0, "name": "cat"}, "name": "Vasya", "photoUrls": ["string"],
              "tags": [{"id": 0, "name": "cat"}], "status": "available"}
res = requests.post(f"https://petstore.swagger.io/v2/pet",
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(param_dict))
pet_id = res.json()["id"]
print(res.json())

# POST /pet/{petId}/uploadImage
res = requests.post(f"https://petstore.swagger.io/v2/pet/{pet_id}/uploadImage",
                    headers={'accept': 'application/json'},
                    files={'file': ('Picture.jpg', open('Picture.jpg', 'rb'), 'image/jpeg')})
print(res.json())

# PUT /pet
param_dict = {"id": f'{pet_id}', "category": {"id": 0, "name": "dog"}, "name": "Rex", "photoUrls": ["string"],
              "tags": [{"id": 0, "name": "dog"}], "status": "available"}
res = requests.put(f"https://petstore.swagger.io/v2/pet",
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                   data=json.dumps(param_dict))
print(res.json())

# GET /pet/findByStatus
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'},
                   headers={'accept': 'application/json'})
print(res.json())

# GET /pet/{petId}
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'petId': f'{pet_id}'},
                   headers={'accept': 'application/json'})
print(res.json())

# POST /pet/{petId}
res = requests.post(f"https://petstore.swagger.io/v2/pet/{pet_id}",
                    headers={'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
                    data={'name': 'Max', 'status': 'pending'})
print(res.json())

# POST /store/order
param_dict = {'id': '0', 'petId': f'{pet_id}', 'quantity': '1', 'shipDate': '2022-12-16T12:26:30.711Z',
              'status': 'placed', 'complete': 'true'}
res = requests.post(f"https://petstore.swagger.io/v2/store/order",
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(param_dict))
order_id = res.json()["id"]
print(res.json())

# GET /store/order/{orderId}
res = requests.get(f"https://petstore.swagger.io/v2/store/order/{order_id}", headers={'accept': 'application/json'})
print(res.json())

# GET /store/inventory
res = requests.get(f"https://petstore.swagger.io/v2/store/inventory", headers={'accept': 'application/json'})
print(res.json())

# DELETE /store/order/{orderId}
res = requests.delete(f"https://petstore.swagger.io/v2/store/order/{order_id}")
print(res.json())

# DELETE /pet/{petId}
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
print(res.json())

# POST /user
param_dict = {'id': '0', 'username': 'Koshak', 'firstName': 'Cat', 'lastName': 'Catonovskiy',
              'email': 'catcatonovskiy@test.com', 'password': '12Cat7353', 'phone': '86565655565', 'userStatus': '0'}
res = requests.post(f"https://petstore.swagger.io/v2/user",
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(param_dict))
username = 'Koshak'
print(res.json())

# POST /user/createWithArray
param_dict = {'id': '0', 'username': 'NewTesters', 'firstName': 'Test1', 'lastName': 'Testers',
              'email': 'tester1@test.com', 'password': '12tester17353', 'phone': '86284655565', 'userStatus': '0'}
res = requests.post(f"https://petstore.swagger.io/v2/user/createWithArray",
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(param_dict))
print(res.json())

# POST /user/createWithList
param_dict = {'id': '0', 'username': 'Attempt2', 'firstName': 'John', 'lastName': 'Testers',
              'email': 'john@test.com', 'password': '12john7353', 'phone': '86565658255', 'userStatus': '0'}
res = requests.post(f"https://petstore.swagger.io/v2/user/createWithList",
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(param_dict))
print(res.json())

# GET /user/{username}
res = requests.get(f"https://petstore.swagger.io/v2/user/{username}", headers={'accept': 'application/json'})
print(res.json())

# GET /user/login
res = requests.get(f"https://petstore.swagger.io/v2/user/login", params={'username': f'{username}',
                                                                         'password': '12Cat7353'},
                   headers={'accept': 'application/json'})
print(res.json())

# GET /user/logout
res = requests.get(f"https://petstore.swagger.io/v2/user/logout", headers={'accept': 'application/json'})
print(res.json())

# PUT /user/{username}
param_dict = {'id': '0', 'username': 'Koshak', 'firstName': 'Jane', 'lastName': 'Doe',
              'email': 'janedoetest@test.com', 'password': '12Jane7353', 'phone': '86565633365', 'userStatus': '0'}
res = requests.put(f"https://petstore.swagger.io/v2/user/{username}",
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                   data=json.dumps(param_dict))
print(res.json())

# DELETE /user/{username}
res = requests.delete(f"https://petstore.swagger.io/v2/user/{username}")
print(res.json())
