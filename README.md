Playing around with Rethinkdb 1.11, trying to learn its query support in python. 

Tried out various queries ranging in complexity that I might encounter and to see how queries might be dynamically constructed.

Currently using sample data using embedded array documents. 

Wanted to to perform queries that filter
* by field
* by nested field
* by values within a range
* if value exists in embedded array
* any combination

eg:

* all snowboards
* all products in given size[s]
* all snowboards that have x features
* all mens snowboards in size[s] x, with board features y, that cost between a & b

using example data like this
```
{
    'name': 'mens snowboard 1',
    'product_type': 'snowboards',
    'sizes': [152, 157, 159, 160],
    'board_features': [
        { 'name': 'Twin Tip', 'sysname': 'twin-tip' },
        { 'name': 'Reverse Camber', 'sysname': 'reverse-camber' },
    ],
    'gender': 'mens',
    'price': 100.00,
    'brand': {
        'name': 'libtech'
    }
},    
{
    'name': 'mens snowboard 2',
    'product_type': 'snowboards',
    'sizes': [157, 164],
    'gender': 'mens',
    'price': 102.00,
    'brand': {
        'name': 'libtech'
    },
    'board_features': [
        { 'name': 'Powder Board', 'sysname': 'powder-board' },
        { 'name': 'Reverse Camber', 'sysname': 'reverse-camber' },
        { 'name': 'Directional', 'sysname': 'directional' },
    ],
}, 
```

to get it running:

```
virtualenv _env
. _/env/bin/activate
pip install -r requirements.txt 
python test_queries.py
```


