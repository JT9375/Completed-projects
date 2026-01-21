"""
Developed by - James R Terris
"""
import logging
import time
import pandas
from clrs.quicksort import quicksort

class Line:
    """
    class consisting of a name and lists for the stations and connections on a railway line.
    """
    def __init__(self, name, list_of_stations, station_connections):
        self.name = name
        self.list_of_stations = list_of_stations
        self.station_connections = station_connections

    def open_station(self, station_name): #set station to open
        for station in self.list_of_stations:
            if self.list_of_stations[station][0] == station_name:
                self.list_of_stations[station][1] = True

    def close_station(self, station_name): #set station to closed
        for station in self.list_of_stations:
            if self.list_of_stations[station][0] == station_name:
                self.list_of_stations[station][1] = False

    def add_station(self, station):
        self.list_of_stations.append([station, True])# Add station, Presume its open

    def add_connection(self, v1, v2, weight = None):#add tuple of two connecting vertex with weight
        self.station_connections = self.station_connections + [(v1, v2, weight)] #add tuple to end of list

def create_line(dataset, line_name):
    """
    Generate the list of stations and connections to be assigned to a class
    Each station name will be stripped to remove possible whitespace
    :param dataset: London Underground data.xlsx
    :param line_name: Range of your particular lines data within the spreadsheet
    :return: list of stations on the line, connections between stations on the line
    """
    list_of_stations = []
    list_of_connections = []
    logging.debug("creating lists...")
    for x in range(line_name[0]-1, line_name[1]):
        data = list(dataset.iloc[x])#use .iloc to return a singular row of the dataframe, transform the data into a list
        if str(data[2]) == "nan": #no data available
            list_of_stations.append([data[1].strip(), True]) #deffine vertex
        else:
            list_of_connections = list_of_connections + [(data[1].strip(), data[2].strip(), int(data[3]))] #define edge
            logging.debug("lists created")
    return list_of_stations, list_of_connections

def create_complete_network():
    """
    create a list of all stations and the most efficient connection for each vertex
    """
    complete_network = [Bakerloo.list_of_stations + Central.list_of_stations + Circle.list_of_stations +
                        District.list_of_stations + Hammersmith_and_city.list_of_stations + Jubilee.list_of_stations +
                        Metropolitan.list_of_stations + Northern.list_of_stations + Piccadilly.list_of_stations +
                        Victoria.list_of_stations + Waterloo_and_city.list_of_stations,
                        Bakerloo.station_connections + Central.station_connections + Circle.station_connections +
                        District.station_connections + Hammersmith_and_city.station_connections +
                        Jubilee.station_connections + Metropolitan.station_connections + Northern.station_connections +
                        Piccadilly.station_connections + Victoria.station_connections +
                        Waterloo_and_city.station_connections]

    filtered_list_of_stations = []
    for station in complete_network[0]:
        if station not in filtered_list_of_stations:  # remove duplicate stations from the list of stations
            filtered_list_of_stations.append(station)

    filtered_station_connections_no_weight = []
    filtered_station_connections = []
    for connection in complete_network[1]:
        if (connection[0], connection[1]) not in filtered_station_connections_no_weight:
            # For any station with a connection running between both edges as the source and destination,
            # prevent the flip from being added to the list
            filtered_station_connections_no_weight.append((connection[1], connection[0]))
            filtered_station_connections.append(connection)

    quicksort(filtered_station_connections) # sort connections so duplicates are adjacent
    previous = ("", "", 0)
    for c in filtered_station_connections[:]:
        if c[0] == previous[0] and c[1] == previous[1]:  # Find the lower weight edge of duplicate tuples
            if c[2] >= previous[2]:
                filtered_station_connections.remove(c)  # remove the duplicate of a higher edge
        previous = c

    return filtered_list_of_stations, filtered_station_connections


#Small sample set for testing
sample_line = Line("sample", [["A", True], ["B", True], ["C", True], ["D", True], ["E", True]],
                   [("A", "C", 5), ("A", "B", 3), ("A", "D", 12), ("B", "E", 9), ("B", "D", 4), ("C", "D", 6), ("D", "E", 7)])

"""
Assign the file name to a variable
Turn the spreadsheet into a dataframe using: pandas library
"""
data = 'London Underground data.xlsx'
dataset = pandas.read_excel(data)

"""
Each tuple references the rows consisting of data for that particular line 
when passed as a parameter for create_line, they can be used to define the range of a for loop
"""
bakerloo = 0, 49 #tested
central = 50, 147 #tested
circle = 148, 217 # tested
district = 218, 336 #tested
hammersmith_and_city = 337, 393 #tested
jubilee = 394, 446 #tested
met = 447, 516 #tested
northern = 517, 617 #tested
piccadilly = 618, 723 #tested
victoria = 724, 754 #tested
waterloo_and_city = 755, 757 #tested

#Create a class for each of the Underground lines
s, c = create_line(dataset, bakerloo)
Bakerloo = Line("Bakerloo", s, c, )

s, c = create_line(dataset, central)
Central = Line("Central", s, c, )

s, c = create_line(dataset, circle)
Circle = Line("Circle", s, c, )

s, c = create_line(dataset, district)
District = Line("District", s, c, )

s, c = create_line(dataset, hammersmith_and_city)
Hammersmith_and_city = Line("Hammersmith and City", s, c, )

s, c = create_line(dataset, jubilee)
Jubilee = Line("Jubilee", s, c)

s, c = create_line(dataset, met)
Metropolitan = Line("Metropolitan", s, c)
#
s, c = create_line(dataset, northern)
Northern = Line("Northern", s, c)

s, c = create_line(dataset, piccadilly)
Piccadilly = Line("Piccadilly", s, c)

s, c = create_line(dataset, victoria)
Victoria = Line("Victoria", s, c)

s, c = create_line(dataset, waterloo_and_city)
Waterloo_and_city = Line("Waterloo and City", s, c)

s, c = create_complete_network()
Complete_Network = Line("Complete network", s, c)


"""
Run code
"""
if __name__ == "__main__":
    start = time.time()
    # print(Complete_Network.list_of_stations)
    # print(filtered_station_connections_no_weight)
    # print(Complete_Network.station_connections)
    print()
    end = time.time()
    print("runtime:", end - start)


"""
References:
Geeks for Geeks - 'How to import an Excel file into Python' - https://www.geeksforgeeks.org/python/how-to-import-an-excel-file-into-python-using-pandas/
                - 'Manipulating dataframes' - https://www.geeksforgeeks.org/python/manipulating-dataframes-with-pandas-python/
                - 'Convert column to list' - https://www.geeksforgeeks.org/pandas/how-to-convert-pandas-column-to-list/
"""