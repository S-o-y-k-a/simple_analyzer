def read_config():
    interval = 0
    s_l = 0
    with open('../config/config.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            if key == 'interval':
                interval = int(value)
            elif key == 'sequence_length':
                s_l = int(value)
    return (interval, s_l)

print(read_config())