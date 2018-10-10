import pandas as pd
import numpy as np
import googlemaps

def travel_time(origin, destination, key, mode = 'driving', distance=False):
    """
    Calculates the travel time between two points

    Parameters
    ----------
    origin : string
        Starting Point
    destination : string
        Destination Point
    key : string
        Google Map API key; Important (Will return NULL if the key is incorrect)
    mode : string, default = 'driving'
        Options: ['driving', 'walking', 'bicycling','transit']
        Type of Commute
    distance : boolean, default False
        If True, will return a distance between the points
    

    Returns
    -------
    String / Tuple(If Distance if True)

    """
    gm = googlemaps.Client(key=key)
    try:
        commute = gm.distance_matrix(origin, destination, mode=mode)
        commute_time = commute['rows'][0]['elements'][0]['duration']['text']

        if distance == True:
            distance_ = commute['rows'][0]['elements'][0]['distance']['text']
            return(commute_time, distance_)

        return(commute_time)
    
    except Exception as e:
        if distance == True:
            return(np.NaN, np.NaN)
        else:
            return(np.NaN)