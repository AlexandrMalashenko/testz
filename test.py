import timeit

code_to_test = """
import requests


for i in range(1, 702):
    r = requests.post('http://localhost:8080/revert', json={"text":"kte"})
"""

elapsed_time = timeit.timeit(code_to_test, number=10)/10/2
print(elapsed_time)
