list_a =[{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
key= lambda x: int(x['model'])
result= sorted(list_a,key = key, reverse=True)
print(result)