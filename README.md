# PyTango Device Server AM2315
Content: <a href="#install_driver">Installing AM2315 driver</a>, <a href="#register_TDS">Registering TangoDS</a>, <a href="#connect_db">Connecting Databases</a>, <a href="#write_TDS">Writing TangoDS</a>, <a href="#run_TDS">Running TangoDS</a>.

This repository holds a Tango Device Server for the <a href = "https://www.adafruit.com/products/1293">AM2315 temperature and humidity sensor</a> and a quick tutorial on how it was written and what will be needed to get the Server running. I am working on a Raspberry Pi 4 with PyTango 9.2.5 (without database) but this tutorial should work with any hardware supporting an i2c bus. How to hook up the AM2315 to a Rapsi or another Arduino is shown <a href="https://cdn-learn.adafruit.com/downloads/pdf/am2315-encased-i2c-temperature-humidity-sensor.pdf?timestamp=1588759334">here</a>.  

# Installing AM2315 driver
Start by installing the <a href="https://github.com/adafruit/Adafruit_Python_GPIO">Adafruit_GPIO library</a> via

`pip3 install adafruit-gpio`

You will see that the mentioned github repository is deprecated, but you can still download the library.  
Adafruit suggests to use the AM2320 driver instead but as I have tried it, I learned that the AM2315 does not work with the AM2320 driver (see <a href="https://github.com/adafruit/Adafruit_CircuitPython_AM2320/issues/17">issue</a>). Unfortunately there is no maintained python driver for the AM2315 sensor so that I uploaded the driver <code color="code-colors inline">AM2315.py</code> from <a href="https://www.switchdoc.com/">SwitchDoc Labs</a> that can be used but will not be maintained.

Either keep the driver in the same directory as the TangoDS or move it to your python site-/dist-packages.
Now you should be able to `import AM2315` in a python prompt and test the driver.
