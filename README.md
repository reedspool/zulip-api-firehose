## Get an API key

[Follow these instructions](https://zulip.com/api/api-keys) to get a `zuliprc` file in this directory.

Copy `zuliprc.py.template` into a new file called `zuliprc.py`. Then fill out the values from your zuliprc file in the `zuliprc.py`

## Make a backup of ALL streams in the zulip instance

The stream subscription API endpoint has the caveat that if we attempt to subscribe to a stream which does not exist, it creates it. This scares the shit out of us, because we're doing a bulk operation. So we are going to be extra safe and do some sort of verification that each stream we attempt to subscribe to actually exists first. 

On second thought, we're just goin for it. You only live once. But we'll make a backup just in case we screw something up.

``` sh
$ python3 get-all-streams.py > all-streams-backup.json
```

Note: Reverting based on this backup is left as an exercise to the reader. 

## Make a backup of your current subscriptions

``` sh
$ python3 get-all-my-subscriptions.py > my-subscriptions-backup.json
```

Note: Reverting based on this backup is left as an exercise to the reader. 

## Subscribe to all streams

NOTE: Do the backup above before you do this, if you want to go back to your current life easily.

``` sh
$ python3 subscribe-to-all-streams.py
```
