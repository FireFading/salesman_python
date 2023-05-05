## Description
The Travelling Salesman Problem (TSP) is a known optimization problem associated with finding the optimal route through a given city. It is NP-hard in nature and requires time resources exponentially dependent on the size of the problem.

TSP has various variations, such as finding the shortest or cheapest route. To solve the problem with a large number of cities, approximate algorithms and heuristics are used, as complete brute force becomes ineffective.

The main goal of TSP is to find the optimal route, which visits each city only once and returns to the original city. This task has wide application in various fields such as logistics, route planning and network design.


![image](https://user-images.githubusercontent.com/91421235/236538012-26c79534-67a3-4d38-9ebb-ca5b562764f0.png)

## Installation
```bash
    pip install -r requirements.txt
```

## Usage
- you can run this with or without arguments
- for help, run `python main.py --help` or `python main.py -h`
```bash
    usage: main.py [-h] [--file FILE] [--algorithm {approx,brute-force}]

    The salesman problem solver

    options:
    -h, --help            show this help message and exit
    --file FILE, -f FILE  Specify the file name
    --algorithm {approx,brute-force}, -a {approx,brute-force}
                            Specify the algorithm to use
```
- [file with points example](points.txt) - contains two space-separated values representing the x and y coordinates of a point
