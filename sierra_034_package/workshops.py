import requests

print('El valor de __name__ para workshops es:', __name__)

def unreleased():
    """Retorna los próximos talleres en CódigoFacilito
    >>> type(unreleased()) == type(dict()) 
    True
    """
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')

    if response.status_code == 200:
        payload = response.json()
        return payload['data']