import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


PROJECT_NAME ="ann implementation"
USER_NAME ="yaswanth2802"

setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email="cyk12@iitbbs.ac.in",
    description="its a basic implementation of ann",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)