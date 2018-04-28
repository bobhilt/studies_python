# A* Shortest Path Algorithm
# http://en.wikipedia.org/wiki/A*
# FB - 201012256
# http://code.activestate.com/recipes/577519-a-star-shortest-path-algorithm/
from heapq import heappush, heappop # for priority queue
import math
import time
import random

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
    dir_map = [] # map of dirs
    row = [0] * n
    for i in range(m): # create 2d arrays
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

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
                j = dir_map[y][x]
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
                    dir_map[ydy][xdx] = int((i + dirs / 2) % dirs)
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    # update the priority
                    open_nodes_map[ydy][xdx] = m0.priority
                    # update the parent direction
                    dir_map[ydy][xdx] = (i + dirs / 2) % dirs
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


def build_a_map(m,n):
    #m  vertical size of the map (rows)
    #n  horizontal size of the map (cols)
    m = int(m)
    n = int(n)
    the_map = []
    row = [0] * n
    for i in range(m): # create empty map
        the_map.append(list(row))

    # fillout the map with a '+' pattern
    for x in range(int(n / 8), int(n * 7 / 8)):
        the_map[m / 2][x] = 1
    for y in range(int(m/8, m * 7 / 8)):
        the_map[y][n / 2] = 1

    # randomly select start and finish locations from a list
    sf = []
    sf.append((0, 0, n - 1, m - 1))
    sf.append((0, m - 1, n - 1, 0))
    sf.append((n / 2 - 1, m / 2 - 1, n / 2 + 1, m / 2 + 1))
    sf.append((n / 2 - 1, m / 2 + 1, n / 2 + 1, m / 2 - 1))
    sf.append((n / 2 - 1, 0, n / 2 + 1, m - 1))
    sf.append((n / 2 + 1, m - 1, n / 2 - 1, 0))
    sf.append((0, m / 2 - 1, n - 1, m / 2 + 1))
    sf.append((n - 1, m / 2 + 1, 0, m / 2 - 1))
    (xStart, yStart, xFinish, yFinish) = random.choice(sf)
    return the_map
    
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

def print_map(the_map, route):
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

# MAIN
maze  = [[0, 0, 0, 0, 0, 0], 
         [1, 1, 1, 1, 1, 0], 
         [0, 0, 0, 0, 0, 0], 
         [0, 1, 1, 1, 1, 1], 
         [0, 1, 1, 1, 1, 1], 
         [0, 0, 0, 0, 0, 0]]
"""
maze = [[0, 1, 1, 0], 
        [0, 0, 0, 1], 
        [1, 1, 0, 0], 
        [1, 1, 1, 0]]
"""
m,n = len(maze), len(maze[0])
#maze = build_a_map(7,6)

yStart, xStart  = 0,0
yFinish, xFinish = m - 1,n - 1

route = map_info(maze,xStart, yStart, xFinish, yFinish , True)
#route = '100101'
 
input('Press Enter...')
