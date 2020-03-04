import sys
import heapq

info = sys.stdin.readlines()
graph_info = info[0].split()
num_nodes = int(graph_info[0])
num_edges = int(graph_info[1])
uber_origin = int(graph_info[2])
edges = info[1:]
adjacency_list = [[] for i in range(num_nodes)]

#construct adjacency list
for e in edges:
	e = e.split()
	origin = int(e[0])
	destination = int(e[1])
	weight = int(e[2])
	adjacency_list[origin].append([weight,destination])

distances = [float('inf') for i in range(num_nodes)] #for all nodes set distance from origin to infinity
distances[uber_origin] = 0 #except origin node itself
distances_heap = []
heapq.heappush(distances_heap, [0, uber_origin]) #priority queue for getting min distance nodes
parents = [[None] for i in range(num_nodes)]

while not distances_heap==[]:
	curr = heapq.heappop(distances_heap)
	curr_node = int(curr[1])
	curr_distance = int(curr[0])
	for neighbour in adjacency_list[curr_node]:
		[weigh, neigh] = neighbour
		if neighbour==uber_origin:
			continue
		elif distances[neigh] == float('inf') or weigh + curr_distance < distances[neigh]:
			parents[neigh].append(curr_node)
			distances[neigh] = curr_distance + weigh
		else:
			continue
		heapq.heappush(distances_heap, [distances[neigh], neigh])

for n in range(num_nodes):
	parent = parents[n].pop()
	if parent != None:
		print(n, distances[n], parent)