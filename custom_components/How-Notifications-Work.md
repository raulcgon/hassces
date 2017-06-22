1. Pre-define notification categories which contain 1-4 actions.
1. Notify iOS app with `data.push.category` set to `ALARM` (which contains actions named `SOUND_ALARM` and `SILENCE_ALARM`).
2. Push notification delivered to device
3. `SOUND_ALARM` button on notification pressed
4. Identifier of button (`SOUND_ALARM`) sent back to HA as the `actionName` property of the event `ios.notification_action_fired`.