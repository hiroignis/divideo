import os

print(os.getcwd())

for i in range(0, 100):
    os.mkdir(('%04d' % i))
