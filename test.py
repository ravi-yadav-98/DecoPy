from DecoPy import measure_time

@measure_time
def slow_function():
    for _ in range(10000000):
        pass

if __name__ == "__main__":
    slow_function()
