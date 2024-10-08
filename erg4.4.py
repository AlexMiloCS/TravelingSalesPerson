
class travelingSalesperson:
    def __init__(self,data):
        self.graph = {}
        with open(data, 'r') as file:
            # Skip the header
            next(file)
            for line in file:
                sender, receiver, risk = line.strip().split(',')
                risk = int(risk)
                if sender not in self.graph:
                    self.graph[sender] = {}
                if receiver not in self.graph:
                    self.graph[receiver] = {}
                self.graph[sender][receiver] = risk  

    def calculate_distance(self,path,start_agent,last_agent):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += self.graph[path[i]][path[i + 1]]
        total_distance +=self.graph.get(start_agent).get(last_agent)
        return total_distance

    def backtrack(self,curr_path, remaining_agents, shortest_path, shortest_distance,start_agent,current_agent):
        if not remaining_agents:
            distance = self.calculate_distance(curr_path,start_agent,current_agent)
            if distance < shortest_distance[0]:
                shortest_distance[0] = distance
                shortest_path[0] = curr_path.copy()
            return  
        for agent in remaining_agents:
            new_path = curr_path + [agent]
            new_remaining = [n for n in remaining_agents if n != agent]
            self.backtrack(new_path, new_remaining, shortest_path, shortest_distance,start_agent,agent) 

    def tsp_backtracking(self,start_agent, agents):
        shortest_path = [None]
        shortest_distance = [float('inf')]
        self.backtrack([start_agent], [agent for agent in agents if agent != start_agent], shortest_path, shortest_distance,start_agent,"")

        return shortest_path, shortest_distance[0]

    def tsp(self):
        agents = list(self.graph.keys())
        for start_agent in agents:
            shortest_path, shortest_distance = self.tsp_backtracking(start_agent, agents)
            print(f"Shortest Path from {start_agent}: {shortest_path}")
            print(f"Shortest Distance Cost: {shortest_distance}\n")



file_path = 'data.txt'  
my_tsp = travelingSalesperson(file_path)
my_tsp.tsp()