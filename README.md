# chromecast-rest-api
Simplistic rest api to cast youtube videos on chromecast using `HTTP PUT` and leveraging [catt](https://pypi.org/project/catt/). For home use only.

The api was written to support playing a youtube video on chromecast as part of a [homassistant](https://www.home-assistant.io/) automation.

## Usage from within homeassitant

Add the following to your `configuration.yaml` to create an action that you can invoke from any automation or script:
``` yaml
rest_command:
  play_my_favourite_video:
    url: "http://<host>:5000/cast"
    method: 'PUT'
    content_type: 'application/json'
    payload: '{ "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ" }'
    verify_ssl: false
```
