import requests

# requests.get(
#     'curl -v -X POST -d "{\"card_no\": 25121111}" https://demo.thingsboard.io/api/v1/iK0zWkznWEoYqBnmAtQf/telemetry '
#     '--header "Content-Type:application/json"')
data = "{{\"card_no\": {}}}".format('test_post2')
requests.post(url='https://demo.thingsboard.io/api/v1/iK0zWkznWEoYqBnmAtQf/telemetry',data=data)