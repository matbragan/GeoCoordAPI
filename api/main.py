from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

from utils.struct import addressStruct, coordStruct

app = Flask(__name__)

@app.route('/', methods=['POST'])
def Coordinates():
    geolocator = Nominatim(user_agent='geocoord')
    
    data = request.get_json()
    fullAddress = addressStruct(data)

    location = geolocator.geocode(fullAddress)

    try:
        coordinates = {
            'latitude': location.latitude,
            'longitude': location.longitude
        }

        return jsonify(coordinates)

    except AttributeError as e:
        return jsonify({'error': f'Error accessing latitude and longitude: {e}'})

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'})
    

@app.route('/reverse', methods=['POST'])
def ReverseCoordinates():
    geolocator = Nominatim(user_agent='geocoord')
    
    data = request.get_json()
    fullCoord = coordStruct(data)

    location = geolocator.reverse(fullCoord)

    try:
        address = {
            'address': location.address
        }

        return jsonify(address)

    except AttributeError as e:
        return jsonify({'error': f'Error accessing address: {e}'})

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'})


if __name__ == '__main__':
    app.run(debug=True)
