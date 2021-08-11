from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
  name = 'pearpy',
  packages = ['pearpy'],
  version = '0.1.2',
  license='MIT',
  description = 'A Python package for writing multithreaded code.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Aiden Szeto',
  author_email = 'aszeto35@gmail.com',
  url = 'https://github.com/MLH-Fellowship/pear',
  download_url = 'https://github.com/MLH-Fellowship/pear/archive/refs/tags/v0.1.2.tar.gz',
  keywords = ['multithreading', 'parallelism', 'processes'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
