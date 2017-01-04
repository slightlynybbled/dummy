import time


count = 0
while True:
    count += 1
    with open('dummy.txt', 'w') as f:
        f.write('count: {}'.format(count))

    time.sleep(1.0)
