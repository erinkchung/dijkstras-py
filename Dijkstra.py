import sys
import heapq

info = sys.stdin.readlines()
graph_info = info[0].split()
num_nodes = int(graph_info[0])
num_edges = int(graph_info[1])
origin_node = int(graph_info[2])
edges = info[1:] #store edge array
adjacency_list = [[] for i in range(num_nodes)] #initialize adjacency list

#construct adjacency list
for e in edges:
	e = e.split() #since edges are given as string
	origin = int(e[0]) #node where directed edge starts
	destination = int(e[1]) #node where directed edge ends
	weight = int(e[2])
	adjacency_list[origin].append([weight,destination])
	#modify adjacency list sub-list corresponding to origin node adding destination node

distances = [float('inf') for i in range(num_nodes)]
explored = []
distances_heap = []
heapq.heappush(distances_heap, [0, origin_node])
explored.append(origin_node)

while(len(explored)<num_nodes and not distances_heap==[]):
	curr = heapq.heappop(distances_heap)
	curr = curr[1]
	for neighbour in adjacency_list[curr]:
		[weigh, neigh] = neighbour
		print('now explored', explored)
		print('currently examining neighbour', neigh, 'of node', curr)
		print('current distances heap', distances_heap, '\n')
		if neigh==origin_node or neigh in explored:
			continue
		else:
			if distances[neigh] == float('inf'):
				distances[neigh] = weigh
			else:
				distances[neigh] += weigh
		heapq.heappush(distances_heap, [distances[neigh], neigh])
		heapq.heapify(distances_heap)
		explored.append(neigh)

print('final distances from node', origin_node, ':', distances)
print('final distances heap', distances_heap)
print('explored by the end', explored)