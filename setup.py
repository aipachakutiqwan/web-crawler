"""
Setup application libraries
"""
import setuptools

setuptools.setup(
    name="web-crawler",
    version="1.0.0",
    packages=setuptools.find_packages(include=["src", "src.*"]),
    python_requires=">=3.10.4",
    install_requires=[
            "aiohttp==3.8.3",
            "PyYAML==6.0",
            "pydantic==1.9.0",
            "Flask==2.2.2",
            "Flask[async]",
            "certifi",
            "pytest==7.1.0",
            "fastapi==0.68.1",
            "uvicorn==0.17.6",
    ]
)
