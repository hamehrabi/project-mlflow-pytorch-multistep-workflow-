from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "REPO_NAME"
AUTHOR_USER_NAME = "Hamed Mehrabi"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['mlflow',
                        'tqdm',
                        'pandas',
                        'numpy',
                        'PyYAML']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="Template for python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/hamehrabi/project-mlflow-pytorch-multistep-workflow",
    author_email="mehrabi.hamed@outlook.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)
