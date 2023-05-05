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
