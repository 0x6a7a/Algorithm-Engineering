import math
import time

def _dist(points, a, b):
    dx = points[a][0] - points[b][0]
    dy = points[a][1] - points[b][1]
    return math.sqrt(dx * dx + dy * dy)


def first_improvement_two_opt(
    points: list[tuple[float, float]],
    initial_tour: list[int],
    timeout: float = 10.0,
) -> list[int]:
    """
    First-improvement 2-opt (classical): find first improving move, apply, restart.

    Args:
        points: List of (x, y) coordinate tuples.
        initial_tour: Starting tour as a permutation of point indices.
        timeout: Maximum runtime in seconds. If exceeded, return the best tour
            found so far. Check ``time.perf_counter()`` against a precomputed
            deadline after each restart (coarse-grained is fine).

    Returns:
        Tour as a list of point indices.
    """
    # TODO: Implement Variant 1 (first-improvement with restart).
    # Respect ``timeout``: compute ``deadline = time.perf_counter() + timeout``
    # and break out of the outer loop once the deadline is reached.
    improved = True
    n = len(points)
    start = time.perf_counter()
    #print("##########################################################################")
    #print(initial_tour)
    
    while improved:

        if time.perf_counter() - start >= 10.0:
            break
        
        improved = False
        for i in range(0, n-2):
            for j in range(i+2, n-1):
                if i==0 and j == n-1:
                    continue
                delta = _dist(points, initial_tour[i], initial_tour[j]) + _dist(points, initial_tour[i+1], initial_tour[j+1]) - _dist(points, initial_tour[i], initial_tour[i+1]) - _dist(points, initial_tour[j], initial_tour[j+1])
                if delta < 0:
                    #reverse list
                    initial_tour[i+1:j+1] = initial_tour[i+1:j+1][::-1]
                    improved = True
                    break 
            else:
                continue
            break
    #print("##########################################################################")
    #print(initial_tour)
    return initial_tour
