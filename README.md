# Temperature Data Logger and Plotter

This project aims to create a temperature data logger and plotter accessible through a web interface. The data source for this project is the Nucleo microcontroller with an MCP9808 temperature sensor connected to it. The temperature data is accessed by sending a single character over the USB virtual comm port to the Nucleo, which responds with the current temperature in ASCII format.

## Requirements

To run this project, you'll need:

- Nucleo microcontroller
- MCP9808 temperature sensor
- Software development environment for the Nucleo microcontroller
- SQLite3
- Programming language: Python
- Web server software: lighttpd
- Graphic library for data visualization
- Internet access

## Usage

1. Connect the Nucleo microcontroller with the MCP9808 temperature sensor.
2. Upload the firmware to the Nucleo.
3. Modify the getTemp.py file to match your database filepath.
4. Make a crontab job to run the getTemp.py file at your desired rate. 
5. Install and configure the web server software.
6. Access the web interface to view temperature data and graphs.
