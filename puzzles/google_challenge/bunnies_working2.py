# A* Shortest Path Algorithm
# http://en.wikipedia.org/wiki/A*
# FB - 201012256
# http://code.activestate.com/recipes/577519-a-star-shortest-path-algorithm/

from heapq import heappush, heappop  # for priority queue
import math
import time
import itertools

# Maze node types
T_SPACE = 0
T_WALL = 1
T_START = 2
T_ROUTE = 3
T_FINISH = 4
DISTANCE_MEASURE = 'Manhattan' # Euclidian, Chebyshev, Manhattan

# MAIN
dirs = 4 # number of possible directions to move on the map
if dirs == 4:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
elif dirs == 8:
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

class node:
    xPos = 0 # x position
    yPos = 0 # y position
    distance = 0 # total distance already travelled to reach the node
    priority = 0 # priority = distance + remaining distance estimate
    def __init__(self, xPos, yPos, distance, priority, DISTANCE_MEASURE = 'Manhattan'):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority
    def __lt__(self, other): # comparison method for priority queue
        return self.priority < other.priority
    def updatePriority(self, xDest, yDest):
        self.priority = self.distance + self.estimate(xDest, yDest) * 10 # A*
    # give higher priority to going straight instead of diagonally
    def nextMove(self, dirs, d): # d: direction to move
        if dirs == 8 and d % 2 != 0:
            self.distance += 14
        else:
            self.distance += 10
    # Estimation function for the remaining distance to the goal.
    def estimate(self, xDest, yDest):
        xd = xDest - self.xPos
        yd = yDest - self.yPos
        if DISTANCE_MEASURE == 'Euclidean':
            d = math.sqrt(xd * xd + yd * yd)
        elif DISTANCE_MEASURE =='Chebyshev':
            d = max(abs(xd), abs(yd))
        else:
            #Manhattan distance
            d = abs(xd) + abs(yd)

        return(d)

# A-star algorithm.
# The path returned will be a string of digits of directions, 0-3, E,S,W,N
def pathFind(the_map, n, m, dirs, dx, dy, xStart, yStart, xFinish, yFinish):
    closed_nodes_map = [] # map of closed (tried-out) nodes
    open_nodes_map = [] # map of open (not-yet-tried) nodes
    came_from = [] # map of dirs
    row = [0] * n
    for i in range(m): # create 2d arrays
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        came_from.append(list(row))

    pq = [[], []] # priority queues of open (not-yet-tried) nodes
    pqi = 0 # priority queue index
    # create the start node and push into list of open nodes
    n0 = node(xStart, yStart, 0, 0)
    n0.updatePriority(xFinish, yFinish)
    heappush(pq[pqi], n0)
    open_nodes_map[yStart][xStart] = n0.priority # mark it on the open nodes map

    # A* search
    while len(pq[pqi]) > 0:
        # get the current node w/ the highest priority
        # from the list of open nodes
        n1 = pq[pqi][0] # top node
        n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority)
        x = n0.xPos
        y = n0.yPos
        heappop(pq[pqi]) # remove the node from the open list
        open_nodes_map[y][x] = 0
        closed_nodes_map[y][x] = 1 # mark it on the closed nodes map

        # quit searching when the goal is reached
        # if n0.estimate(xFinish, yFinish) == 0:
        if x == xFinish and y == yFinish:
            # generate the path from finish to start
            # by following the dirs
            path = ''
            while not (x == xStart and y == yStart):
                j = came_from[y][x]
                c = str(int((j + dirs / 2) % dirs))
                path = c + path
                x += dx[j]
                y += dy[j]
            return path

        # generate moves (child nodes) in all possible dirs
        for i in range(dirs):
            xdx = x + dx[i]
            ydy = y + dy[i]
            #if not past left or right border, top or bottom border, closed on map
            # or noted already as closed...
            if not (xdx < 0 or xdx > n-1 or ydy < 0 or ydy > m - 1
                    or the_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                # generate a child node
                m0 = node(xdx, ydy, n0.distance, n0.priority)
                m0.nextMove(dirs, i)
                m0.updatePriority(xFinish, yFinish)
                # if it is not in the open list then add into that
                if open_nodes_map[ydy][xdx] == 0:
                    open_nodes_map[ydy][xdx] = m0.priority
                    heappush(pq[pqi], m0)
                    # mark its parent node direction
                    came_from[ydy][xdx] = int((i + dirs / 2) % dirs)
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    # update the priority
                    open_nodes_map[ydy][xdx] = m0.priority
                    # update the parent direction
                    came_from[ydy][xdx] = (i + dirs / 2) % dirs
                    # replace the node
                    # by emptying one pq to the other one
                    # except the node to be replaced will be ignored
                    # and the new node will be pushed in instead
                    while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    heappop(pq[pqi]) # remove the target node
                    # empty the larger size priority queue to the smaller one
                    if len(pq[pqi]) > len(pq[1 - pqi]):
                        pqi = 1 - pqi
                    while len(pq[pqi]) > 0:
                        heappush(pq[1-pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    pqi = 1 - pqi
                    heappush(pq[pqi], m0) # add the better node instead
    return '' # if no route found



def map_info(the_map,xStart, yStart, xFinish, yFinish, print_info = True):
    if print_info:
        print ('Map size (X,Y):', n, m)
        print ('Start: ', xStart, yStart)
        print ('Finish: ', xFinish, yFinish)
    t = time.time()
    route = pathFind(the_map, n, m, dirs, dx, dy, xStart, yStart, xFinish, yFinish)
    if print_info:
        print ('Time to generate the route (seconds): ', time.time() - t)
        print ('Route:')
        print (route, 'Length = ', len(route))
    return route

"""def print_map(the_map, route):
    # mark the route on the map
    if len(route) > 0:
        x = xStart
        y = yStart
        the_map[y][x] = T_START
        for i in range(len(route)):
            j = int(route[i])
            x += dx[j]
            y += dy[j]
            the_map[y][x] = T_ROUTE
        the_map[y][x] = T_FINISH

    # display the map with the route added
    print ('Map:')
    for y in range(m):
        for x in range(n):
            xy = the_map[y][x]
            if xy == T_SPACE:
                print ('0',end="")
            elif xy == T_WALL:
                print ('1',end="")
            elif xy == T_START:
                print ('S',end="")
            elif xy == T_ROUTE:
                print ('R',end="")
            elif xy == T_FINISH:
                print ('F',end="")
        print()
"""
#grid sizes
m = n = 0

#route_node_types
NT_UNKNOWN = 999
NT_OPEN = 0
NT_WALL = 1
NT_START = 2
NT_ROUTE = 3
NT_FINISH = 4

class route_node:
    xPos = 0 # x position
    yPos = 0 # y position
    node_type = NT_UNKNOWN
    came_from = None
    goes_to = None
    route_distance = 0 # total distance already travelled to reach the node

    def __init__(self, yPos, xPos, route_distance, node_type):
        self.xPos = xPos
        self.yPos = yPos
        self.route_distance = route_distance
        self.node_type = node_type
    def __repr__(self):
        return('route_node: y: {0} x: {1} dist: {2}'.format(self.yPos, self.xPos, self.route_distance))
    
def map_nodes(the_map, route, xStart, yStart, xFinish, yFinish):
    
    node_map = []
    row_count, col_count = len(the_map), len(the_map[0])

    def prev_node(node,dir):
        x, y = node.xPos, node.yPos
        # previous node is opposite direction on route
        #ToDo: may be fancier ways to do this, but this will get the job done.
        if dir == '0': 
            x1, y1 = x-1, y
        elif dir == '1':
            x1, y1 = x, y-1
        elif dir == '2':
            x1, y1 = x + 1, y
        elif dir == '3':
            x1, y1 = x, y+1
        else:
            print('dir, y, x:',dir, y, x)
            raise ValueError
        if (x1 < 0 or x1 > col_count or y1 < 0 or y1 > row_count):
            # invalid call!
            print('Invalid prev_nod coordinates y: {0}, x: {1}, dir: {2}'.format(y, x, dir))
            raise ValueError
        return node_map[y1][x1]
    
                
    #Build node map to show distance, route, index by row, col
    row = [0] * col_count

    #build substrate grid --todo: revisit for better structure
    for y in range(row_count):
        node_map.append(list(row))
        for x in range(col_count):
            node_map[y][x] = route_node(y,x,999,the_map[y][x])

    # apply route, starting from end
    current = node_map[yFinish][xFinish]  #Don't count final node yet
    current.node_type = NT_FINISH
    route_distance = 0
    current.route_istance = route_distance

    #map nodes along route
    for previous_direction in route[::-1]: 
        #print('current: {0}, route_distance: {1}'.format(current,route_distance))
        if (current.xPos == xStart and current.yPos == yStart):
            current.came_from = None
            current.node_type = NT_START
        else:
            current.came_from = prev_node(current, previous_direction)
            current = current.came_from # march up the route to start
            route_distance += 1
            current.route_distance = route_distance
            current.node_type = NT_ROUTE

    current.node_type= NT_START
    
    # find route nodes with single adjacent wall
    # find savings as difference between path distances. Just calculate it.
        # if opposing node has not yet been evaluated, evaluate its path distance
        # (This seems like the crux)
        
    print('node_map:_length', len(node_map))
    return node_map

def get_neighbors(node_map, node):
    neighbors = [] 
    y,x = node.yPos,node.xPos
    if x < n-1:
        neighbors.append(node_map[y][x+1])
    if y < m-1:
        neighbors.append(node_map[y+1][x])
    if x > 0:
        neighbors.append(node_map[y][x-1])
    if y > 0:
        neighbors.append(node_map[y-1][x])
    
    return neighbors

def get_score(nodes):
    #expect nodes to be constellation around central node, n = 2-4 for corner, edge, central
    score = 0
    ntypes = []
    distances = []
    for neighbor in nodes:
        if neighbor.node_type != NT_WALL and neighbor.route_distance != 999: #add a check unevaluated node
            ntypes.append(neighbor.node_type)
            distances.append(neighbor.route_distance)
    if len(ntypes) < 2:
        return 0
    #this will be a problem if distance has not been calculated yet...
    score = max([abs(x[0]-x[1]) 
                    for x in list(itertools.combinations(distances, 2))]) 
    score -= 2  # cost of span
    return score

# MAIN
"""
maze  = [[0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0]]
"""
"""
maze = [[0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]]
"""

def answer(maze):
    global n, m
    m,n = len(maze), len(maze[0])

    yStart, xStart  = 0,0
    yFinish, xFinish = m - 1,n - 1
    route = pathFind(maze, n, m, dirs, dx, dy, xStart, yStart, xFinish, yFinish)
    min_route = len(route)
    for y in range(m):
        for x in range(n):
            if maze[y][x] == 1:
                maze[y][x] = 0
                route = pathFind(maze, n, m, dirs, dx, dy, xStart, yStart, xFinish, yFinish)
                #route = map_info(maze, xStart, yStart, xFinish, yFinish , False)
                if len(route) < min_route:
                    min_route = len(route)
                    print('xy min route',y,x,min_route)
                maze[y][x] = 1 #revert
    return min_route + 1 #include start step

#node_map = map_nodes(maze, route, xStart, yStart, xFinish, yFinish)
#max_wall_removal_savings = 0
#for y in reversed(range(m)):
#    for x in reversed(range(n)):
#        print('{0},type: {1}'.format(node_map[y][x],node_map[y][x].node_type))       
        #cycle through wall nodes (node_type = 1)
#        my_node = node_map[y][x]
#        if my_node.node_type == NT_WALL:
#           neighbors = get_neighbors(node_map, my_node)
#           if len(neighbors) > 1:
#               s = get_score (neighbors)
#               print('{0} score: {1}'.format(my_node,s))
#               if s > max_wall_removal_savings:
#                   max_wall_removal_savings = s
#base_len = len(route) + 1 #include start node as a step
#post_len = base_len - max_wall_removal_savings
#print ('route length before: {0}, after: {1}'.format(base_len, post_len))

#map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] #7

"""
map  = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]] #11
"""
#map = [[0,1],[0,0]] #3
"""map = [[0,1,0,0,0],
       [0,1,0,1,0],
       [0,1,0,1,0],
       [0,1,0,1,0],
       [0,0,0,1,0]] #9
"""
map = [[0,0,0,1,0,0,0],
       [0,1,0,1,0,1,0],
       [0,0,0,1,1,0,0],
       [0,1,0,0,0,0,1],
       [0,0,0,1,0,0,0]] #11

map = [[0,0,0,0,0,0,0,1],
       [0,1,1,1,1,0,1,1],
       [0,0,0,1,0,0,1,1],
       [0,1,1,0,0,1,1,1],
       [1,1,0,0,1,1,1,1],
       [0,0,0,0,0,0,0,0]] #13

answer(map)

