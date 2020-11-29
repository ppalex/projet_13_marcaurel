from apiManager.models.mapquest_api import MapquestApi


def get_address_coordinates(street, number, city, region):
    mapquest = MapquestApi()

    mapquest.send_request(street, number, city, region)

    return mapquest.get_latitude(), mapquest.get_longitude()
