from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    username='9c8f0264-bdb8-485e-9bfc-2c9803eca33e',
    password='qjHv0LL5hqZo')
    
    
text2 = input("Enter your Description of your Diagram: \n")




response = natural_language_understanding.analyze(text= text2,
    features=Features(entities=EntitiesOptions(model='f4f6d1b0-80ff-4ca8-b659-9245754e10e8')))


#def writeToJSONFile(path, fileName, data):
#	filePathNameWext = './' + path + '/' +fileName + '.json' 
#	with open(filePathNameWext, 'w') as fp: 
#		json.dump(data, fp)

#path = './'
#fileName = 'example3'
#data = json.dumps(response)

#writeToJSONFile(path, fileName, data)
print(response)
#print(json.dumps(response.results, indent=2))
