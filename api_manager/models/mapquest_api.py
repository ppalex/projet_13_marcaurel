import os
import requests
import logging


class MapquestApi:

    def __init__(self):
        self.url = "http://mapquestapi.com/geocoding/v1/address?"
        self.key = os.environ.get("MAPQUEST_API_KEY")
        self._data = []

    def send_request(self, street, number, city, region):

        query = f"key={self.key}&location={street}+{number}+{city}+{region}"

        endpoint = self.url + query

        try:
            response = requests.request(
                "GET", endpoint)
        except requests.exceptions.Timeout:
            logging.error("Timeout error", exc_info=True)
        except requests.exceptions.TooManyRedirects:
            logging.error("Bad url", exc_info=True)
        except requests.exceptions.RequestException as e:
            logging.error("Bad request", exc_info=True)
            raise SystemExit(e)

        if response.status_code == 200:
            self._data = response.json()
            return response.json()
        else:
            return None

    def get_data(self):
        """This method get the data gathered from the api request.

        Returns:
            [JSON]: Response from the request. Contains the data.
        """
        return self._data

    def get_latitude(self):
        """This method get the latitude of a place.

        Returns:
            [Int]: Represents the latitude.
        """
        latitude = None
        try:
            if self.get_data():
                latitude = self.get_data(
                )['results'][0]['locations'][0]['latLng']['lat']
        except KeyError:
            logging.error("Can't get latitude", exc_info=True)

        return latitude

    def get_longitude(self):
        """This method get the longitude of a place.

        Returns:
            [Int]: Represents the longitude.
        """
        longitude = None
        try:
            if self.get_data():
                longitude = self.get_data(
                )['results'][0]['locations'][0]['latLng']['lng']
        except KeyError:
            logging.error("Can't get longitude", exc_info=True)

        return longitude
