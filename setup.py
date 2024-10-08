import setuptools

with open("README.md" , 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Text-Summarization-Project"
AUTHOR_USER_NAME = "M-Adam-Khan"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "muhammadadamkhan29@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A SMALL PYTHON PAKAGE FOR NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http: //github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker" : f"http: //github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": 'src'},
    packages= setuptools.find_packages(where="src")
)