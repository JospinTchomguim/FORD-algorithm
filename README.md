# FORD-algorithm

The problem of the shortest paths from an origin has a solution only if there is no attainable absorbing circuit. Ford's algorithm verifies that there is no circuit absorbent reachable from s. If so, it returns the shortest paths to from s. It is a greedy dynamic programming algorithm which calculates the shortest paths of increasing size. It is suitable for any graph.
Initially, the distance is initialized to 0 for the origin and to infinity for the other vertices.
It examines all the arcs and improves the value of the paths if possible. The new value for each vertex is the minimum distance of all paths of size k-1 at which we adds the edges entering the vertex. As there may be circuits, it is necessary restart.
