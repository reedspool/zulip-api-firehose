## Get an API key

[Follow these instructions](https://zulip.com/api/api-keys) to get a `zuliprc` file in this directory.

Copy `zuliprc.py.template` into a new file called `zuliprc.py`. Then fill out the values from your zuliprc file in the `zuliprc.py`

## Make a backup of your current subscriptions

``` sh
$ python3 get-all-my-subscriptions.py > my-subscriptions-backup.json
```

Note: Reverting based on this backup is left as an exercise to the reader. 

