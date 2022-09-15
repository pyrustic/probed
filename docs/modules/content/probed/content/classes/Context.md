Back to [All Modules](https://github.com/pyrustic/probed/blob/master/docs/modules/README.md#readme)

# Module Overview

**probed**
 
No description

> **Classes:** &nbsp; [Context](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/Context.md#class-context) &nbsp;&nbsp; [ProbedDict](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedDict.md#class-probeddict) &nbsp;&nbsp; [ProbedList](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedList.md#class-probedlist) &nbsp;&nbsp; [ProbedSet](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedSet.md#class-probedset)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Context
This class contains data that describe a change event.
Three attributes are always available:

- collection: the collection object, i.e. an instance of probed.ProbedDict,
probed.ProbedList or probed.ProbedSet

- container: a string that indicates the type of container.
The containers are 'dict', 'list' and 'set'.

- operation: a string that indicates the type of operation.
The operations are same as the names of the methods (minus underscores)
of the collections.
Example, these are the operations for probed.ProbedDict:
'pop', 'setdefault', 'clear', 'popitem', 'update', 'delitem', 'setitem'

Then there are attributes that are available or not, depending of the operation
and the type of container.
Example: when you append a value to an instance of probed.ProbedList,
the operation name is "append", the container is "list", the collection is
the actual instance of probed.ProbedList, and then you have an extra attribute
called 'value'. This attribute contains the value that will be added to
the collection.
Note: the extra attributes mimic the name of the parameters of the operation method.

Illustration:

def on_change(context):
    context.container # 'dict'
    context.collection # the actual plist object
    context.operation # 'append'
    context.value # 'hello'

plist = probed.ProbedList(on_change=on_change)
plist.append("hello") # the name of the parameter of this operation is 'value'

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|collection|getter|None||
|container|getter|None||
|operation|getter|None||



# All Methods
[\_\_init\_\_](#__init__)

## \_\_init\_\_
Init




**Signature:** (self, collection, container, operation, \*\*kwargs)

|Parameter|Description|
|---|---|
|collection|the collection object|
|container|str, the type of container ("dict", "set", "list")|
|operation|str, the type of operation. Example: "pop", "remove", "append".|





**Return Value:** None

[Back to Top](#module-overview)



