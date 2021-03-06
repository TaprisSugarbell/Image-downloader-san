from setuptools import setup

with open("./README.md", "r") as file:
    long_description = file.read()

setup(name="image-downloader-san",
      version="0.1.0",
      description="An image downloader",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/TaprisSugarbell/Image-downloader-san",
      author="Sayu Ogiwara",
      author_email="anonesayu@gmail.com",
      license="MIT",
      packages=["Id"],
      install_requires=["requests", "beautifulsoup4", "html-to-json"],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      zip_safe=False)



