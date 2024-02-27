import sys

try:
    file = open('zuliprc', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Could not find zuliprc file. Did you put it in the source root?", file=sys.stderr)
    sys.exit(1)

for line in file:
    # skip the lines that don't have key value pairs
    if (line.find('=') < 0):
        continue

    key, value = line.split('=')
    value = value[:-1] # drop the trailing newline
    if (key == 'email'):
        email = value
    if (key == 'key'):
        api_key = value
    if (key == 'site'):
        baseurl = value

auth = (email, api_key)
