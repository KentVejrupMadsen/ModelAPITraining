import requests

HEADERS = {
    'Authorization': 'Token 3b5c3ed6d6799a0909c3b1c5b2a58a929bd67af1'
}

limit = 50
offset = 0

all_tasks = []
size_of_tasks: int = 0


while True:    
    Response = requests.get(
        str(
            'http://192.168.0.189:8080/api/projects/1/tasks' + 
            '?limit=' + str(limit) + 
            '&offset=' + str(offset) 
        ),
        headers=HEADERS
    )

    tasks = Response.json()

    if not tasks:
        break

    all_tasks.extend(tasks)
    offset += limit

    size_of_tasks = len(all_tasks)
    
    if int((size_of_tasks % 1000)) == 0:
        print(size_of_tasks)
        break

print(size_of_tasks)
print(all_tasks[0])