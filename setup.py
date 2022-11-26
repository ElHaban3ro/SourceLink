from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'SourceLink',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['SourceLink'],
    version = '1.1',
    license = 'MIT',
    description = 'Generate a file with the contribution list of your youtube video from a playlist. 📷',
    author = 'ElHaban3ro',
    author_email = 'habanferd@gmail.com',
    url = 'https://github.com/ElHaban3ro/ConvTool',
    keywords = ['python', 'playlists', 'youtube', 'content-creator'],
    classifiers = [
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
        'Programming Language :: Python :: 3.11'
    ],
    install_requires=['requests']
)