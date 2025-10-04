import json
bemor={
    'Ism':"Alijon Valiyev",
    "yosh":30,
    "oila":True,
    "farzandlari":("Axmad","Bonu"),
    "alergiya":None,
    "dorilar":[
        {"nomi":"Analgin","miqdori":0.5},
        {"nomi":"Panadol","miqdori":1.2}
    ]
}
bemor_json=json.dumps(bemor,indent=4)
print(bemor_json)
print(type(bemor_json))

with open('bemor.json','w') as f:
    json.dump(bemor,f)

d={
    "address_components": [
        {
            "long_name": "Tinchlik Street",
            "short_name": "Tinchlik Street",
            "types": [
                "political",
                "sublocality",
                "sublocality_level_1"
            ]
        },
        {
            "long_name": "Khorezm",
            "short_name": "Khorezm",
            "types": [
                "locality",
                "political"
            ]
        },
        {
            "long_name": "Khorezm Region",
            "short_name": "Khorezm Region",
            "types": [
                "administrative_area_level_1",
                "political"
            ]
        },
        {
            "long_name": "Uzbekistan",
            "short_name": "UZ",
            "types": [
                "country",
                "political"
            ]
        }
    ],
    "formatted_address": "Tinchlik Street, Khorezm, Urgench",
    "geometry": {
        "bounds": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        },
        "location": {
            "lat": 41.55860870120288,
            "lng": 60.6218083747805
        },
        "location_type": "APPROXIMATE",
        "viewport": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        }
    },
    "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
    "types": [
        "political",
        "sublocality",
        "sublocality_level_1"
    ]
}

kenglik=d["geometry"]["location"]['lat']
uzunlik=d["geometry"]["location"]['lng']
print(kenglik,uzunlik)