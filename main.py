from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.post("/pipelines/parse")
async def parse_pipeline(pipeline: Dict[str, List[Dict]]):
    # Extracting nodes and edges from the payload
    nodes = pipeline.get("nodes", [])
    edges = pipeline.get("edges", [])

    # Calculating the number of nodes and edges
    num_nodes = len(nodes)
    num_edges = len(edges)

    # Checking if the graph is a DAG
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        graph[source].append(target)
        in_degree[target] += 1
        in_degree[source] += 0  # Ensuring all nodes are in the in_degree dictionary

    # Performing Kahn's Algorithm to check for cycles
    queue = deque([node["id"] for node in nodes if in_degree[node["id"]] == 0])
    visited_count = 0

    while queue:
        current = queue.popleft()
        visited_count += 1
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    is_dag = visited_count == len(nodes)

    return {"num_nodes": num_nodes, "num_edges": num_edges, "is_dag": is_dag}
