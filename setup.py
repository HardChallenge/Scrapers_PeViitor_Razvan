from setuptools import setup, find_packages

setup(
    name="peviitor_scraper",
    version="0.0.1",
    description="A simple scraper",
    url="",
    author="Peviitor",
    packages=find_packages(),
    install_requires=["beautifulsoup4", "lxml", "requests"],
    python_requires=">=3.10",
)
