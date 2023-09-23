# HTTP notifications example

This is just an example of an HTTP notification service for the RTMIP.

HTTP service should has 2 API functions:

`GET /status` - optional function, required to pass some variables to the rtmip and contacts list

`POST /` - main function to receive notifications data from rtmip and send it where is required, path to this API method specified directly in the address in rtmip, example: `http://192.168.1.23:4567/send/notify`

# Data

Notification data received from the RTMIP:

```json
{
  "recipients": ["string","string",...],
  "subject": "some notification title",
  "text": "text desciption of what happened in the event",
  "image": "base64 encoded image data"
}
```

Status data format what service should returned on `GET /status` request:

```json
{
  "version": "v1.2.3",
  "contacts": [
    { "name": "Test", "value": "test@example.com" },
    { "name": "Test2", "value": "test2@example.com" }
  ],
  "variables": []
}
```
