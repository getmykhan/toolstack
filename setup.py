from setuptools import setup
setup(
  name = 'toolstack',
  packages = ['toolstack'], # this must be the same as the name above
  version = '0.0.19',
  description = 'A collection of Useful tools to speed-up the data analysis process',
  author = 'Mohammed Yusuf',
  author_email = 'mohammedykhan7@gmail.com',
  url = 'https://github.com/getmykhan/toolstack', # use the URL to the github repo
  keywords = ['toolkit', 'nlp', 'data cleaning', 'toolstack', 'data science', 'machine learning'], # arbitrary keywords
  install_requires=['pandas', 'numpy', 'nltk', 'googlemaps'],
)