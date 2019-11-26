from setuptools import setup, find_packages


with open("README.md", encoding="UTF-8") as f:
    readme = f.read()


setup(
    name="{{cookiecutter.project_name}}",
    version="0.1.0",
    description=".",
    long_description=readme,
    author="Sam",
    author_email="samatkins@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click==7.0"],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_name}}={{cookiecutter.project_name}}.main:main"
        ]
    },
)
