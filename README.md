## Probed

Sometimes you need to know when the content of a data collection has changed.

`Probed` is a library that exposes three classes: `ProbedDict`, `ProbedList` and `ProbedSet`.

These classes are containers like the built-in `Python` containers (dict, list, set) which they subclass but with not a twist but two twists:

- be notified when the content of your data collection changes (if you wish to be notified);
- being able to put a probe into data collection to do more than just be notified.

Let's write a script to see `Probed` in action:

```python
# script.py
from probed import ProbedList


def on_change(info):
    msg = "\nThe {} operation changed the {} collection\n{}"
    print(msg.format(info.operation, info.container,
                     info.collection))


plist = ProbedList(on_change=on_change)
plist.append("hi")
plist.insert(1, "friend")

```

Let's run the script:

```bash
$ python3 script.py

The append operation changed the list collection
['hi']

The insert operation changed the list collection
['hi', 'friend']
```

Now, let's discover what the `probe` does and how to use it:

```python
# script.py
from probed import ProbedSet


def probe(info):
    if info.operation == "add":
        if info.item is None:
            info = None
        else:
            info.item = info.item.lower()
    return info


pset = ProbedSet(probe=probe)
# add items
pset.add("RED")
pset.add(None)
pset.add("Green")
# print
print(pset)  # {'green', 'red'}

```

In the last script, the `probe` was used to control the items added to the data collection.

All operations that change the contents of the built-in containers are covered by "probed".

`Probed` is available on PyPI:

```bash
$ pip install probed
```

[Shared](https://github.com/pyrustic/shared) uses `Probed` !


A better documentation will come later. If you like it, bookmark the repository so you don't miss out updates.


Join the [Discord](https://discord.gg/fSZ6nxzVd6) !