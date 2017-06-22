# Map
Will show a map with a red tipped pin at the coordinates given.
The map will be centered at the coordinates given.

```yaml
service: notify.iOSApp
data:
  message: Something happened at home!
  data:
    push:
      category: map
    action_data:
      latitude: 40.785091
      longitude: -73.968285
```

# Camera Stream

The notification thumbnail will be a still image from the camera.
The notification content is a real time stream of a camera.

You can use the attachment parameters `content-type` and `hide-thumbnail` with camera.

You can view an example [here](https://www.youtube.com/watch?v=LmYwpxPKW0g).

```yaml
service: notify.iOSApp
data:
  message: Motion detected in the Living Room
  data:
    push:
      category: camera
    entity_id: camera.demo_camera
```

# Attachment

The thumbnail of the notification will be the media at the URL.
The notification content is the media at the URL.

Attachment can be used with custom push notification categories/actions.

```yaml
service: notify.iOSApp
data:
  message: Something happened at home!
  data:
    attachment:
      url: https://67.media.tumblr.com/ab04c028a5244377a0ab96e73915e584/tumblr_nfn3ztLjxk1tq4of6o1_400.gif
      content-type: gif
      hide-thumbnail: false
```

## Supported media types

If the attachment does not appear please ensure it is in one of the following formats:

### Audio

Maximum file size: 5 MB

Formats:
* AIFF
* WAV
* MP3
* MPEG4 Audio

### Image

Maximum file size: 10 MB

Formats:
* JPEG
* GIF
* PNG

### Video

Maximum file size: 50 MB

Formats:
* MPEG
* MPEG2
* MPEG4
* AVI

## Configuration
You can pass the following keys to change the behavior of the attachment:

### `url`
The URL of content to use as the attachment. This URL _must_ be accessible from the Internet, or the receiving device must be on the same network as the hosted content.

### `content-type`
By default, the extension of the URL will be checked to determine the filetype. If there is no extension/it can't be determined you can manually provide a file extension.

### `hide-thumbnail`
If set to `true` the thumbnail will not show on the notification. The content will only be viewable by expanding.