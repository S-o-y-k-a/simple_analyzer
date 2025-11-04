
import time
import random
from simple_analyzer.analyzer import Analyzer

def read_config():
    interval = 0
    s_l = 0
    with open('config/config.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            if key == 'interval':
                interval = int(value)
            elif key == 'sequence_length':
                s_l = int(value)
    return (interval, s_l)


def main():
    print(f"Read_config: {read_config()}")

    interval, sequence_length = read_config()
    analyzer = Analyzer()

    while True:

        num = random.randint(1, 100)
        analyzer.add_number(num)

        print("\n\n\n")
        print(f"Added number {num}")

        if len(analyzer.data) > sequence_length:
            analyzer.data.pop(0)
        
        print("\n")
        print("Analyzer results:")
        print("...")
        print(f"Total even count: {analyzer.even_count()}")
        print(f"Total odd count: {analyzer.odd_count()}")
        print(f"Highest number: {analyzer.highest_number()}")
        print(f"Total increasing pairs: {analyzer.increasing_pairs()}")


        time.sleep(interval)

        current_seconds = time.localtime().tm_sec
        if len(analyzer.data) >= sequence_length and current_seconds == 0:
            print("Loop stopped.")
            break

        

if __name__ == "__main__":
    main()