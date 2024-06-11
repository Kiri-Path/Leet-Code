#LEET CODE: Find the city with the smallest number of neighbours based on threshold distance

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance from a city to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Set the distances for the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Step 2: Apply Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 3: Count reachable cities within the distance threshold
        min_reachable_cities = float('inf')
        result_city = -1
        
        for i in range(n):
            reachable_cities = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachable_cities += 1
            
            # Step 4: Determine the optimal city
            if reachable_cities < min_reachable_cities:
                min_reachable_cities = reachable_cities
                result_city = i
            elif reachable_cities == min_reachable_cities and i > result_city:
                result_city = i
        
        return result_city
