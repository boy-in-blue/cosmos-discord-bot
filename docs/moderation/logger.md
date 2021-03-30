---
description: >-
  Logger plugin provides option to log various discord and moderation events in
  desired channel.
---

# Logger

#### Available Logger Events:

* `on_message_delete` -- Logs content and other attributes of message which was just deleted.
* `on_bulk_message_delete` -- Logs channel from which messages was deleted in bulk.
* `on_message_edit` -- Logs old and new content along with other attributes of message which was just edited.
* `on_guild_channel_pins_update` -- Logs several attributes when a message is pinned in channel.
* `on_member_join` -- Logs useful attributes of member who just joined the server.
* `on_member_remove` -- Logs attributes of member who just left the server.
* `on_confession` -- Logs information about each confessions made through secret confessions.
* `on_moderation` -- Logs several attributes of member, type of moderation, moderator and reason if it was provided when moderator or auto-moderator performs any moderation action on this member.
* `on_text_level_up` -- Logs and congratulates when a member advances to upper text level.
* `on_voice_level_up` -- Logs and congratulates when a member advances to upper voice level.
* `on_server_boost` -- Sends pretty embed message when a member boosts the server. Use [serverboost preset](../settings/administrator-settings.md#preset-serverboost) to set custom thanks message.

## ;logger

Displays list of loggers enabled in different channels.

```yaml
Aliases:
- log
- logging
- loggers

Usage:
;logger
```

### ;logger enable

Enables logger in specified channel. Logger name should always start with `on_`.

```yaml
Aliases:
- create

Usage:
;logger enable [channel] [name]
```

### ;logger disable

Disables specified logger. Logger name should always start with `on_`.

```yaml
Aliases:
- remove

Usage:
;logger disable [name]
```

