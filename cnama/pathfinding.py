from collections import deque
import heapq

class Pathfinding:

    @staticmethod
    def traversal_bfs(graph, start):
        frontier = deque([start])
        reached = [start]

        while frontier:
            current_node = frontier.popleft()

            neighbours = graph.get_neighbours(current_node)

            for next_node in neighbours:
                if next_node not in reached:
                    frontier.append(next_node)
                    reached.append(next_node)

        return reached

    @staticmethod
    def path_exists_bfs(graph, start, end):
        frontier = deque([start])
        reached = [start]

        while frontier:
            current_node = frontier.popleft()

            if current_node == end:
                return True

            neighbours = graph.get_neighbours(current_node)

            for next_node in neighbours:
                if next_node not in reached:
                    frontier.append(next_node)
                    reached.append(next_node)

        return False

    @staticmethod
    def get_path_bfs(graph, start, end):
        UNVISITED = -1
        frontier = deque([start])
        came_from = [UNVISITED] * graph.count

        came_from[start] = start

        while frontier:
            current = frontier.popleft()

            if current == end:
                path = []
                node = end
                while node != start:
                    path.append(node)
                    node = came_from[node]
                path.append(start)
                path.reverse()
                return path

            for neighbor in graph.get_neighbours(current):
                if came_from[neighbor] == UNVISITED:
                    frontier.append(neighbor)
                    came_from[neighbor] = current

        return []

    @staticmethod
    def traversal_dfs(graph, start):
        frontier = [start]
        reached = []

        while frontier:
            current_node = frontier.pop()

            neighbours = graph.get_neighbours(current_node)

            for next_node in neighbours:
                if next_node not in reached:
                    frontier.append(next_node)

            reached.append(current_node)

        return reached

    @staticmethod
    def get_path_dfs(graph, start, end):
        UNVISITED = -1
        frontier = [start]
        came_from = [UNVISITED] * graph.count

        came_from[start] = start

        while frontier:
            current = frontier.pop()

            if current == end:
                path = []
                node = end
                while node != start:
                    path.append(node)
                    node = came_from[node]
                path.append(start)
                path.reverse()
                return path

            for neighbor in graph.get_neighbours(current):
                if came_from[neighbor] == UNVISITED:
                    frontier.append(neighbor)
                    came_from[neighbor] = current

        return []

    @staticmethod
    def path_exists_dfs(graph, start, end):
        frontier = [start]
        reached = [start]

        while frontier:
            current_node = frontier.pop()

            if current_node == end:
                return True

            neighbours = graph.get_neighbours(current_node)

            for next_node in neighbours:
                if next_node not in reached:
                    frontier.append(next_node)
                    reached.append(next_node)

        return False

    @staticmethod
    def get_path_dijkstra(graph, start, end):
        dists = [float('inf')] * graph.count
        previous = [-1] * graph.count
        dists[start] = 0

        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            current_dist, current = heapq.heappop(pq)

            if current == end:
                break

            for neighbor in graph.get_neighbours(current):
                new_dist = current_dist + graph[current, neighbor]

                if new_dist < dists[neighbor]:
                    dists[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))

        if dists[end] == float('inf'):
            return []

        path = []
        at = end
        while at != -1:
            path.append(at)
            at = previous[at]

        path.reverse()
        return path
