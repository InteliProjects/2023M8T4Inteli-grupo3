from setuptools import setup, find_packages

setup(
    name="pacote_uploadS3",
    author="Patrick Victorino Miranda",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'boto3',
        'python-dotenv'
    ]
)
