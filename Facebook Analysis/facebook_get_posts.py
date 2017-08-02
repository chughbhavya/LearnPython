#Program to extract posts data by calling Facebook API and storing it in PKL file.
import pickle
import facebook
import requests
import json
import os

token = 'EAACEdEose0cBAKaVlb76K84cKDzBaFW77hiZAh33WKv9M4jJlXU6GJ0mCWFM33uXc13TfLnFQZAZBmE4GHlJrs8wiwN3MCGL8OuQDUYhUBZCSwZA0IFeHrmZAIFZB54NCzkKo36ZB2QCZAeWXzwWAqVyyddR220aiRNRFOiQe8ZAP4bb2nHYvFEllTZAHq2TYVxqS4ZDEAACEdEose0cBAKaVlb76K84cKDzBaFW77hiZAh33WKv9M4jJlXU6GJ0mCWFM33uXc13TfLnFQZAZBmE4GHlJrs8wiwN3MCGL8OuQDUYhUBZCSwZA0IFeHrmZAIFZB54NCzkKo36ZB2QCZAeWXzwWAqVyyddR220aiRNRFOiQe8ZAP4bb2nHYvFEllTZAHq2TYVxqS4ZD'

data = []
# CAlling the Graph API of facebook module and extracting all my posts
if __name__ == '__main__':
    graph = facebook.GraphAPI(token)
    posts = graph.get_object('me/posts')

# while there are next pages collecting the data in an empty list
    while True:
        try:
            posts = requests.get(posts['paging']['next']).json()
            data.extend(posts['data'])
            # print data
        except KeyError:
            break
# Loading data in PKL file
pickle.dump(data,open('test.pkl', 'wb'))
loaded_data = pickle.load(file=open('test.pkl'))
