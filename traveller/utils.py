"""Simple travelling salesman problem between cities."""
import math
from math import cos
from math import sin
from math import asin
from math import sqrt
from math import radians
from collections import namedtuple

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

# Declaring namedtuple()
Location = namedtuple('Point', ['longitude','latitude'])

class RouteFinder:
    def __init__(self,distance_matrix,coordinate_list=None,num_vehicles=None,depot=None):
        self.coordinate_list = coordinate_list
        self.data = {
            'distance_matrix': distance_matrix,
            'num_vehicles': num_vehicles if num_vehicles else 1,
            'depot': depot if depot else 0
        }
        self.response ={}


    def print_solution(self,manager, routing, solution):
        #self.response['Objective'] = '{} miles'.format(solution.ObjectiveValue())
        index = routing.Start(0)
        plan_output = 'Route for vehicle: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(self.coordinate_list[manager.IndexToNode(index)])
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        plan_output += ' {}'.format(self.coordinate_list[manager.IndexToNode(index)])
        self.response['plan_output'] = plan_output
        #self.response['Route distance']= '{} miles'.format(route_distance)


    def find_route(self):
        """Entry point of the program."""
        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(len(self.data['distance_matrix']),
                                               self.data['num_vehicles'], self.data['depot'])

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)


        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return self.data['distance_matrix'][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        # Print solution on console.
        if solution:
            self.print_solution(manager, routing, solution)

        return self.response


class DistanceMatrix:
    def __init__(self,coordinate_sequence):
        self.source = coordinate_sequence
        self.destination = coordinate_sequence
        self.distance_matrix = []

    def haversine(self,pointA, pointB):
        if (type(pointA) != tuple) or (type(pointB) != tuple):
            raise TypeError("Only tuples are supported as arguments")
        lat1 = pointA[1]
        lon1 = pointA[0]
        lat2 = pointB[1]
        lon2 = pointB[0]
        # convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [float(lat1), float(lon1), float(lat2), float(lon2)])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
        # returns result in kilometer
        return c * r

    def sqrt_distance(self,pointA, pointB):
        lat1 = pointA[1]
        lon1 = pointA[0]
        lat2 = pointB[1]
        lon2 = pointB[0]
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        return math.sqrt(dlon ** 2 + dlat ** 2)

    def create_distance_matrix(self):
        for pointA in self.source:
            row = []
            for pointB in self.destination:
                row.append(self.sqrt_distance(pointA,pointB))
            self.distance_matrix.append(row)
        return self.distance_matrix




