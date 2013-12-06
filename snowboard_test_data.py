test_products = [
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
    {
        'name': 'mens snowboard 3',
        'product_type': 'snowboards',
        'sizes': [142, 152, 160],
        'gender': 'mens',
        'price': 103.00
        ,
        'brand': {
            'name': 'gnu'
        },
        'board_features': [            
            { 'name': 'Directional', 'sysname': 'directional' },
        ],
    },
    {
        'name': 'mens snowboard 4',
        'product_type': 'snowboards',
        'sizes': [160],
        'gender': 'mens',
        'price': float(104.00),
        'brand': {
            'name': 'bataleon'
        }
    }, 
    {
        'name': 'mens snowboard 5',
        'product_type': 'snowboards',
        'sizes': [160],
        'gender': 'mens',
        'price': 105.99,
        'brand': {
            'name': 'bataleon'
        }
    },    
    {
        'name': 'womens snowboard 1',
        'product_type': 'snowboards',
        'sizes': [152, 157, 159, 160],
        'gender': 'womens',
        'price': 100.00,
        'brand': {
            'name': 'libtech'
        }
    },
    {
        'name': 'womens snowboard 2',
        'product_type': 'snowboards',
        'sizes': [142, 152],
        'gender': 'womens',
        'price': 102.00,
        'brand': {
            'name': 'ride'
        }
    },
    {
        'name': 'empty snowboard 5',
        'product_type': 'snowboards'        
    },
    {
        'name': 'binding 1',
        'product_type': 'binding',
        'sizes': [142, 157, 160], # just to check snowboard queries
        'gender': 'mens',
        'price': 10.00
    },
    {
        'name': 'binding 2',
        'product_type': 'binding',
        'sizes': ['small', 'medium', 'large'],
        'flex': 6,
        'gender': 'mens',
        'price': 20.00,
        'brand': {
            'name': 'ride'
        }
    }
]   
