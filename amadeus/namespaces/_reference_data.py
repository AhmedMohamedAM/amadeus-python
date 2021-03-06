from amadeus.client.decorator import Decorator
from amadeus.reference_data._urls import Urls
from amadeus.reference_data._location import Location
from amadeus.reference_data._locations import Locations
from amadeus.reference_data._airlines import Airlines


class ReferenceData(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.urls = Urls(client)
        self.locations = Locations(client)
        self.airlines = Airlines(client)

    def location(self, location_id):
        return Location(self.client, location_id)
