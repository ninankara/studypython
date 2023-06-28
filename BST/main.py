from bst import solve

def main():
    
    nodes = [int(v) for v in input().split()]
    
    print(*solve(nodes))

if __name__ == "__main__":
    main()
