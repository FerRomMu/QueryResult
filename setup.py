from setuptools import setup, find_packages

setup(
    name='queryresult',
    version='0.1',
    packages=find_packages(),  # Encuentra automáticamente todos los subpaquetes
    description='A simple data structure for Query Results of ChromaDb.',
    author='fer.rom.mu',
    author_email='fer.rom.mu.dev@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/FerRomMu/QueryResult.git',
    license='MIT'
)