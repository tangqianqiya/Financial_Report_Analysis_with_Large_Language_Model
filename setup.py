from setuptools import setup, find_packages

setup(
    name="financial_rag",
    version="0.1.0",
    author="Tang Qianqi",
    author_email="tangqianqiya@gmail.com",
    description="Financial Report Analysis with Large Language Model",
    long_description_content_type="text/markdown",
    url="https://github.com/tangqianqiya/Financial_Report_Analysis_with_Large_Language_Model.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "financial-rag=financial_rag.main:main",
        ],
    },
)
