# Probed collections

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Latest](https://github.com/pyrustic/probed/tags) . [Documentation](https://github.com/pyrustic/probed/tree/master/docs/modules#readme)


# Overview
Sometimes you need to know when the content of a data collection has changed.

`Probed` is a library that exposes three classes: `ProbedDict`, `ProbedList` and `ProbedSet`.

These classes are containers like the built-in Python containers (dict, list, set) which they subclass but with not a twist but two twists:

- be notified when the content of your data collection changes (if you wish to be notified);
- being able to put a probe into data collection to do more than just be notified.

Let's write a script to see `Probed` in action:

```python
# script.py
from probed import ProbedList


def on_change(context):
    msg = "\nThe {} operation changed the {} collection\n{}"
    print(msg.format(context.operation, context.container, context.collection))


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

Now, let's discover what the `probe` feature does and how to use it:

```python
# script.py
from probed import ProbedSet


def probe(context):
    # this probe will lower strings added to the collection
    # also, the object None isn't allowed in the collection
    if context.operation == "add":
        if context.item is None:
            context = None
        else:
            context.item = context.item.lower()
    return context


pset = ProbedSet(probe=probe)
# add items
pset.add("RED")
pset.add(None)
pset.add("Green")
# print
print(pset)  # {'red', 'green'}

```

In the last script, the `probe` was used to control the items added to the data collection.

All operations that change the contents of the built-in containers are covered by `probed`.

> **Read the [modules documentation](https://github.com/pyrustic/probed/tree/master/docs/modules#readme) !**

# Related project
The **Shared** data exchange and persistence library uses `Probed` to implement the `autosave` feature !

> **Discover [Shared](https://github.com/pyrustic/shared) !**



# Installation
**Probed** is **cross platform** and versions under **1.0.0** will be considered **Beta** at best. It is built on [Ubuntu](https://ubuntu.com/download/desktop) with [Python 3.8](https://www.python.org/downloads/) and should work on **Python 3.5** or **newer**.

## For the first time

```bash
$ pip install probed
```

## Upgrade
```bash
$ pip install probed --upgrade --upgrade-strategy eager

```

<br>
<br>
<br>

[Back to top](#readme)

