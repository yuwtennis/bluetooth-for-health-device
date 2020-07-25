import setuptools

PACKAGE="iotble"

with open("README.md", "r") as fh:
    long_description = fh.read()

# Find required packages inside requirements.txt
with open("requirements.txt", "r") as fh:
    requirements = fh.read()

setuptools.setup(
    name=PACKAGE,
    version="0.0.1",
    author="Yu Watanabe",
    author_email="yu.w.tennis@gmail.com",
    description="App for fetching data from ble device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuwtennis/iot-ble",
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
    python_requires='>=3.7',
    package_dir={PACKAGE:'src'},
    packages=[PACKAGE],
    package_data={PACKAGE: ['data/*']},
    install_requires=requirements
)
