def CityTraffic(strArr):
    
    # get cities (int) and cities' neighbours (string) list
    cities = []
    neighbours = []
    
    for element in strArr:
        cities.append(int(element.split(":")[0]))
        neighbours.append(element.split(":")[1][1:-1].split(","))
    # print(cities)
    # print(neighbours)
    
    # order cities and neighbours in cities population size 
    cities, neighbours = map(list, zip(*sorted(zip(cities, neighbours))))
    
    # create dictionary of cities (string) and corresponding neighbours
    cities_str = [str(city) for city in cities]
    dic = dict(zip(cities_str, neighbours))
    
    # output list of strings: City and city's max traffic
    output = []

    # compute max traffic for each city
    for city in cities_str:
        
        max_traffic = 0

        # possible roads to get to the city
        roads_unexplored = dic[city]
        
        # visit the unexplored cities nodes adding them to the explored cities set and removing them from the unexplored set
        # check traffic for each possible road
        for road in roads_unexplored:

            # initialize set of cities_explored (with starting city and neighbor city chosen by road)
            # initialize set of cities_unexplored (neihgbours of road taken city without the initial city which is already explored)
            cities_explored = {city, road}
            cities_unexplored = set(dic[road])
            cities_unexplored.remove(city)
            
            # while loop visits each unexplored city and adds neighbours of unexplored cities set to a temporal set which will be the next unexplored cities set
            # while loop continue flag. True if there are more cities to explore
            road_continue = True
            
            while road_continue:
                # next layer of cities to explore
                visit_next = set()

                # visit each city in unexplored set. Adds visited city to explore and its neighbours to next visit layer 
                for visiting in cities_unexplored:
                    cities_explored.add(visiting)
                    for neighbor in dic[visiting]:
                        if neighbor not in cities_explored:
                            visit_next.add(neighbor)

                # remove explored cities in unexplored set                            
                for explored in cities_explored:
                    if explored in cities_unexplored:
                        cities_unexplored.remove(explored)
                
                # add next visit layer cities to unexplored set
                for next_neighbor in visit_next:
                    cities_unexplored.add(next_neighbor)
                
                # check if there are still cities to visit in unexplored set
                road_continue = any(cities_unexplored)
            
            # finished exploring all cities. Remove starting city from explored set to compute road's traffic
            cities_explored.remove(city)
            
            # compute road's traffic and check if it is greater than previous road traffics
            traffic = [int(city_str) for city_str in cities_explored]
            if sum(traffic) > max_traffic:
                max_traffic = sum(traffic)

        # append max traffic of city to output list
        output.append(city + ":" + str(max_traffic))
    
    # final output string
    output_str = ",".join(output)
    
    return output_str
    
    
# keep this function call here  
print CityTraffic(raw_input())