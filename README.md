# Renesas IoT Sandbox and IBM Watson API Test

Test scripts to accompany an introductory article for 
use of Renesas IoT Sandbox APIs with IBM Watson APIs.

Both Renesas IoT Sandbox and IBM Watson are free to use for limited 
development testing.

Tutorial will be published at [learn.iotcommunity.io]learn.iotcommunity.io()

## File Description

- getiIot.sh pulls JSON data from Renesas IoT Sandbox Data Monitoring
- iot-watson.py parses JSON data and saves human-understandable data to file
- watson-api-no-passwords.sh sends text data to IBM Watson APIs and downloads audio file


## Learning Objections

- pull data from Renesas IoT Sandbox Data Monitoring
- parse JSON IoT data and convert to human-readable data
- push data to Watson text-to-speech API
- get sound file and play

## Additional Information

Although the Renesas IoT Sandbox Data Monitoring dashboard provides
nice gauges, it does not provide a way to get audio alerts.
This is a starter demo to show how data can be downloaded with
the Renesas IoT Sandbox Data Monitoring API and then send to
the IBM Watson API for processing.