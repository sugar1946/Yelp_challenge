import json

business_addr = 'yelp_academic_dataset_business.json'
review_addr = 'yelp_academic_dataset_review.json'
business_list = [];
with open(business_addr) as input_file:
    for line in input_file:
        line_content = json.loads(line)
        if 'Restaurants' in line_content['categories']:
            business_list.append(line_content['business_id'])



'''
obj = {'a':12,'b':23}
print obj
print type(obj)
print obj['a']
encodedjson = json.dumps(obj)
print encodedjson
print type(encodedjson)
print encodedjson[2]
decodedjson = json.loads(encodedjson)
print decodedjson
print type(decodedjson)
print decodedjson['a']
'''