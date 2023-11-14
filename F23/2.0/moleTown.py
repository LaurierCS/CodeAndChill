import time 

nWaypoints = int(input())
waypoints = []
for i in range(nWaypoints):
    waypoints.append(list(map(int,input().split())))

free = int(input())
start, end = int(input()),int(input())
print(waypoints[start],waypoints[end])

def solve(waypoints,free,start,end):
    def getCost(waypoint1,waypoint2):
        x1, y1, z1 = waypoint1
        x2, y2, z2 = waypoint2

        cost = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
        return cost
    print(getCost(waypoints[start],waypoints[end]))
    freeWaypoints = waypoints[:free] 
    if free:
        closestStart = min(freeWaypoints, key = lambda x: getCost(waypoints[start],x))
        closestEnd = min(freeWaypoints, key = lambda x: getCost(waypoints[end],x ))
    else:

        closestStart = waypoints[end]
        closestEnd = waypoints[start]

    return min(getCost(waypoints[start],waypoints[end]),getCost(closestStart,waypoints[start])+getCost(closestEnd,waypoints[end]))

print(solve(waypoints,free,start,end))