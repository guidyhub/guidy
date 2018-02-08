from .models import Tour, TouristTour
from django.http import HttpResponse
from django.core import serializers
import json


import logging


def main(request):

    tours = Tour.objects.values()
    print(tours[0])

    for t in tours:
        t["available_spots"] = get_free_spots(t["id"])
        if t["price"]:
            t["price"] = calculate_price(t["id"])

    # tours_json = serializers.serialize('json', tours)
    tours_json = json.dumps([item for item in tours])

    response = HttpResponse(tours_json, content_type='application/json')

    logging.info(response)

    return response


def calculate_price(tour_id, date="", max_proportion=0.2):
    """
    Calculate pricing of tour
    :param tour_id: id of the tour
    :param date: date of the tour
    :param max_proportion: Client will never pay more than price * max_proportion
    :return: float tuple of max (0) and current price (1)
    """
    price = list(Tour.objects.filter(id=tour_id).values_list("price", flat=True))[0]
    max_price = price * max_proportion
    occupied = get_occupied_spots(tour_id, date)
    if occupied > 0:
        current_price = min(max_price, price/occupied)
    else:
        current_price = max_price

    return max_price, current_price


def get_occupied_spots(tour_id, date):
    """
    Get number of occupied spots in tour
    :param tour_id: id of the tour
    :param date: date of the tour
    :return: int, number of occupied spots
    """
    if date:
        occupied = TouristTour.objects.filter(tour_id=tour_id, date=date).count()
    else:
        occupied = TouristTour.objects.filter(tour_id=tour_id).count()
    return occupied


def get_free_spots(tour_id, date=""):
    """
    Get number of free spots in tour
    :param tour_id: id of the tour
    :param date: date of the tour
    :return: int, number of free spots
    """
    occupied = get_occupied_spots(tour_id, date)
    spots = list(Tour.objects.filter(id=tour_id).values_list("spots", flat=True))[0]

    return spots - occupied
