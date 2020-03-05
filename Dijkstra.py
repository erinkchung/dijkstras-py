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
distances_heap = [] #priority queue in heap form for getting min distance nodes
heapq.heappush(distances_heap, [0, uber_origin])
parents = [[None] for i in range(num_nodes)] #where we will put parents once known

while not distances_heap==[]:
	curr = heapq.heappop(distances_heap) #pops child with min distance from uber origin
	curr_node = int(curr[1])
	curr_distance = int(curr[0])
	for neighbour in adjacency_list[curr_node]: #go through children of node
		[weigh, neigh] = neighbour
		if neighbour==uber_origin: #ignore a cycle
			continue
		elif distances[neigh] == float('inf') or weigh + curr_distance < distances[neigh]:
			#if node is not visited or distance to node on current path
			# is different from previously best found distance
			parents[neigh].append(curr_node) #track parents
			distances[neigh] = curr_distance + weigh #update distance
		else: #if it already has a better distance from uber origin
			continue
		heapq.heappush(distances_heap, [distances[neigh], neigh])
		#put children into priority queue to examine further generations

for n in range(num_nodes):
	parent = parents[n].pop() #fetch most recent / best path parent
	if parent != None: #unless disconnected from uber origin
		sys.stdout.write(str(n) + ' ' + str(distances[n]) + ' ' + str(parent) + '\n')