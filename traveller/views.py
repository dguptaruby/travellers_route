from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from traveller.utils import DistanceMatrix, RouteFinder

'''
sample input is as follows for below api
{
    "list_cord":[[75.85962616866853,22.79614270933867],[75.84514379758467,22.797291799510006],[75.88513552642058,22.75784003109508],[ 75.89375487666832,22.744328470876017]]
}
'''
class ObtainBestRoute(GenericAPIView):
    """
        Concrete view for retrieving a model instance.
        """
    def get(self, request, *args, **kwargs):
        resp = {}
        coordinate_list = request.data.get('list_cord',None)
        if coordinate_list:
            matrix = DistanceMatrix(coordinate_list)
            distance_data = matrix.create_distance_matrix()
            route = RouteFinder(distance_matrix=distance_data,coordinate_list=coordinate_list,num_vehicles=1,depot=0)
            resp = route.find_route()
        return Response (resp)



