import unittest
from cnama.graph import AdjacencyMatrix  # Assuming graph.py contains your graph structure and pathfinding algorithms
from cnama.pathfinding import Pathfinding

# run:
# 'export PYTHONPATH=$PYTHONPATH:/home/alice/dev/pyt/class_tryout'
# before doing tests

class TestPathfinding(unittest.TestCase):

    def setUp(self):
        # Create an Adjacency Matrix for testing
        self.graph = AdjacencyMatrix(7)

        self.graph[0, 1] = 1
        self.graph[0, 2] = 3

        self.graph[1, 0] = 1
        self.graph[1, 3] = 4
        self.graph[1, 4] = 10
        self.graph[2, 3] = 3

        self.graph[3, 4] = 1
        self.graph[3, 6] = 1

    def test_bfs(self):
        traversal = Pathfinding.traversal_bfs(self.graph, 1)
        self.assertEqual(traversal, [1, 0, 3, 4, 2, 6])

        self.assertTrue(Pathfinding.path_exists_bfs(self.graph, 0, 4))
        self.assertTrue(Pathfinding.path_exists_bfs(self.graph, 1, 0))
        self.assertFalse(Pathfinding.path_exists_bfs(self.graph, 2, 5))

        starts = [1, 0, 0, 0]
        ends = [3, 4, 5, 6]
        expected_paths = [[1, 3], [0, 1, 4], [], [0, 1, 3, 6]]
        
        for i in range(len(starts)):
            path = Pathfinding.get_path_bfs(self.graph, starts[i], ends[i])
            self.assertEqual(path, expected_paths[i])

    def test_dfs(self):
        traversal = Pathfinding.traversal_dfs(self.graph, 1)
        self.assertEqual(traversal, [1, 4, 3, 6, 0, 2])

        self.assertTrue(Pathfinding.path_exists_dfs(self.graph, 0, 4))
        self.assertTrue(Pathfinding.path_exists_dfs(self.graph, 1, 0))
        self.assertFalse(Pathfinding.path_exists_dfs(self.graph, 2, 5))

        starts = [1, 0, 0, 0]
        ends = [3, 4, 5, 6]
        expected_paths = [[1, 3], [0, 2, 3, 4], [], [0, 2, 3, 6]]
        
        for i in range(len(starts)):
            path = Pathfinding.get_path_dfs(self.graph, starts[i], ends[i])
            self.assertEqual(path, expected_paths[i])

    def test_dijkstra(self):
        # Test GetPathDijkstra
        starts = [1, 0, 0, 0]
        ends = [3, 4, 5, 6]
        expected_paths = [[1, 3], [0, 1, 3, 4], [], [0, 1, 3, 6]]

        for i in range(len(starts)):
            path = Pathfinding.get_path_dijkstra(self.graph, starts[i], ends[i])
            self.assertEqual(path, expected_paths[i])

if __name__ == '__main__':
    unittest.main()
