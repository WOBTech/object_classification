import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="object_classification"
AUTHOR_USER_NAME='WOBTech'
SRC_REPO="CNN_classification"
AUTHOR_EMAIL="jyothsna.v@wobtstory.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    url=f'https://github.com/WOBTech/object_classification.git',
    project_url={
        "Bug Tracker":f"https://github.com/WOBTech/object_classification.git/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
)