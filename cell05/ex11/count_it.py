import sys

if len(sys.argv) > 1:
    print(f"parameters: {len(sys.argv) - 1}")
    
    for arg in sys.argv[1:]:
        print(f"{arg}: {len(arg)}")
else:
    print("none")