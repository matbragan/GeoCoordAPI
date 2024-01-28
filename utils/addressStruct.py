def addressStruct(dictAddress: dict) -> str:
    
    allowBody = [
        'Number',
        'Street',
        'Neighborhood',
        'District',
        'PostalCode',
        'City',
        'State',
        'Country'
    ]

    listAddress = []
    
    for key, value in dictAddress.items():
        if key in allowBody:
            if value:
                listAddress.append(str(value))

    fullAddress = ', '.join(listAddress)
    
    return fullAddress


def coordStruct(dictCoord: dict) -> str:

    allowBody = [
        'Latitude',
        'Longitude'
    ]

    listCoord = []

    for key, value in dictCoord.items():
        if key in allowBody:
            if value:
                listCoord.append(str(value))

    fullCoord = ', '.join(listCoord)
    
    return fullCoord
