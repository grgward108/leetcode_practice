class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()
        def dfs(visited, node):
            if node not in visited:
                visited.add(node)
                for neighbor in rooms[node]:
                    dfs(visited, neighbor)
            
        
        dfs(visited, 0)
        if len(visited) == len(rooms):
            return True
        else:
            return False
