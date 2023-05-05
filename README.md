## Description
The Travelling Salesman Problem (TSP) is a known optimization problem associated with finding the optimal route through a given city. It is NP-hard in nature and requires time resources exponentially dependent on the size of the problem.

TSP has various variations, such as finding the shortest or cheapest route. To solve the problem with a large number of cities, approximate algorithms and heuristics are used, as complete brute force becomes ineffective.

The main goal of TSP is to find the optimal route, which visits each city only once and returns to the original city. This task has wide application in various fields such as logistics, route planning and network design.

## Algorithms

### Brute Force
- Searches every permutation of cycles and returns the shortest one. Simple algorithm that guarantees the optimal solution, but has O(N!) efficiency, and is therefore not feasible to run on a 100 city dataset (at least on my puny computer), regardless of how fast your for loops were.

### Approximate
- Uses a greedy algorithm to find the shortest path.
- This algorithm is relatively fast O(N^3) and provide very good solutions.
1) Starts at an arbitrary city
2) Go to the next closest unvisited city
3) Repeat (2) until all cities have been visited, save path length
4) Start again at (1) with a diferent initial city.
5) Repeat (1-4) until all possibilities have been exausted and return the shortest path

## Swap
- This algorithm is so faster, O(M*N^2) and produces not bad solutions.
1) Start with a random route
2) Perform a swap between two edges
3) Keep new route if it is shorter
4) Repeat (2-3) for all possible swaps
5) Repeat (1-5) for M possible initial configurations

![image](https://user-images.githubusercontent.com/91421235/236538012-26c79534-67a3-4d38-9ebb-ca5b562764f0.png)

## Installation
```bash
    pip install -r requirements.txt
```

## Usage
- you can run this with or without arguments
- for help, run `python main.py --help` or `python main.py -h`
```bash
    usage: main.py [-h] [--file FILE] [--algorithm {approx,brute-force,swap}]

    The salesman problem solver

    options:
    -h, --help            show this help message and exit
    --file FILE, -f FILE  Specify the file name
    --algorithm {approx,brute-force,swap}, -a {approx,brute-force,swap}
                            Specify the algorithm to use
```
- [file with points example](points.txt) - contains two space-separated values representing the x and y coordinates of a point
