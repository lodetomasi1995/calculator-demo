from setuptools import setup, find_packages

setup(
    name="calculator-demo",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pytest>=7.4.3',
        'flake8>=6.1.0',
    ],
    author="Lorenzo De Tomasi",
    author_email="lorenzo.detomasi@takeda.com",
    description="A simple calculator with DevOps practices",
    keywords="calculator,devops,demo",
    url="https://github.com/lodetomasi1995/calculator-demo",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
)