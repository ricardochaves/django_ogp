import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django_ogp",
    version="0.0b6",
    description="A more dynamic way to register Open Graph protocol",
    long_description=README,
    include_package_data=True,
    author="Ricardo Baltazar Chaves",
    author_email="ricardobchaves6@gmail.com",
    license="MIT",
    url="https://github.com/ricardochaves/django_ogp",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Environment :: Web Environment",
        "Natural Language :: Portuguese (Brazilian)",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
