pwd = {'key1': 'value1', 
       'key2': 'value2'}

print(pwd) # output -> {'key1': 'value1', 'key2': 'value2'}


pwd['key1']


"""
>>> pwd = {'key1': 'value1',
...        'key2': 'value2'}
>>> pwd['key1']
'value1'
>>>
>>>
>>> pwd['key1'] = 'changedValue1' #Canel Casing
>>> pwd
{'key1': 'changedValue1', 'key2': 'value2'}
>>>
"""


# Rules of a dictionary
"""
1. Keys must be unique
2. Keys must be immutable (strings, numbers, tuples)
3. Values can be mutable (lists, dictionaries, sets)
"""
