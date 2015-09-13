# api_stress_test
Stress test your APIs.

This Python 3 script creates threads and makes GET or POST API calls to any endpoint you specify. Use this only on your own APIs to stress test and see how many concurrent requests your server can support, as well as testing the rate limit of your APIs.

##### For you to do:
- Change the number of threads and how many requests each thread makes to adjust the number of total requests to make.
- Add the API URL endpoint to call


To run: ```python3 stress_test.py``` 

##### External Dependency: 
- Python3 requests
