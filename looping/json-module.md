# JSON Module

JSON = JavaScript Object Notation. It's a series of key-value pairs. The key-value pairs may be nested.



json.dumps\(\) creates a JSON string from the data passed in. It looks like a Python dictionary with quotes around it

`>>> import json`

`>>> data = {'foo':1, 'bar':'qwerty'}`

`>>>json.dumps(data)`

`'{"foo": 1, "bar": "qwerty"}'`

`>>> data`

`{'foo': 1, 'bar': 'qwerty'}`

`>>>`



json.loads\(\) takes a JSON String and makes it onto a dictionary

`>>>jsonstr=json.dumps(data)`

`>>> type(json.loads(jsonstr))`

`<type 'dict'>`

