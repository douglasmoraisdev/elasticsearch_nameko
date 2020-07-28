import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elasticsearch_nameko",
    version="0.0.1",
    author="Douglas Morais",
    author_email="msantos.douglas@gmail.com",
    description="Elasticsearch dependency for Nameko",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglasmoraisdev/elasticsearch_nameko.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        'elasticsearch>=7.0.0,<8.0.0',
        'nameko==3.0.0-rc8',
        'git+https://github.com/douglasmoraisdev/backoff_retry#egg=backoff_retry'
    ]    
)