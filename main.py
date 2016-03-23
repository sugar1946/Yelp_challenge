import json

business_addr = 'yelp_academic_dataset_business.json'
review_addr = 'yelp_academic_dataset_review.json'
business_list = [];

with open(business_addr) as input_file:
    for line in input_file:
        line_content = json.loads(line)
        if 'Restaurants' in line_content['categories']:
            business_list.append(line_content['business_id'])
input_file.close()

output_file = open('restaurant_review.json','w')
with open(review_addr) as input_file:
    for line in input_file:
        line_content = json.loads(line)
        vote = line_content['votes']['funny']+line_content['votes']['useful']+line_content['votes']['cool']
        if vote > 0 and line_content['business_id'] in business_list:
            output_content = json.dumps(line_content)
            output_file.write(output_content + '\n')
input_file.close()

output_file = open('restaurant_review_only.json','w')
with open('restaurant_review.json') as input_file:
    for line in input_file:
        line_content = json.loads(line)
        output_content = json.dumps(line_content['text'])
        output_file.write(output_content + '\n')
input_file.close()
output_file.close()
