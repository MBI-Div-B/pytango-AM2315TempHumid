from setuptools import setup, find_packages

setup(
    name="tangods_am2315temphumid",
    version="0.0.1",
    description="Tango Device Server for the AM2315 temperature and humidity sensor",
    author="Daniel Schick",
    author_email="dschick@mbi-berlin.de",
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["AM2315TempHumid = tangods_am2315temphumid:main"]
    },
    license="MIT",
    packages=["tangods_am2315temphumid", "tangods_am2315temphumid.driver"],
    install_requires=[
        "pytango",
        "adafruit-gpio",
    ],
    url="https://github.com/MBI-Div-b/pytango-AM2315TempHumid",
    keywords=["tango device", "tango", "pytango", "am2315"],
)
