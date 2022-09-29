import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='LibraryTest',
    version='0.0.1',
    author='itwasthatguy',
    author_email='blank@blank.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/itwasthatguy/LibraryTest',
    packages=['LibraryTest'],
    install_requires=['requests'],
)