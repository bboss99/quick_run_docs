..  _tut_duplicator:

Duplicator
==============

In :ref:`Array Modifier Grid Tutorial<tut_array_modifier>`, we saw how we can create object in Grid.

You can modify that script to create a duplicator. The change that you have to make is, Instead of creating new object
and adding array modifier, duplicate selected object and add modifier on duplicated object.

That script has limitation:

    1. If you want to use same mesh data. (In viewport, alt D instead of shift D)
    2. If object has animation or material that you want to handle separately based on situation.

So, we need a way to duplicate/create objects.

..  note::

    I had written this script as blender addon for an "Animation Nodes" project. If you find it's settings unintuitive
    that's because it is very project oriented.
    The blender operator version of this script is much shorter. Reason being, changing parameters(property) in operators,
    undos old operation and redos operation with new parameters. While I can delete and recreate in code too, but I have used simple
    'Object Pool' [#f1]_ mechanism.


..  note::

    This script is a bit advanced. This is over 300 lines long, but that is because I have copied some very common
    functions related to collection and object creation from a package that I keep in module folder. In my PC I could
    have imported that module. Last 100 lines or so is code related to UI creation. 'Object Pool' functionality has
    taken a lot of lines too.

    Most important function is at line 98 ``onCopiesChanged`` you can go through that and read comments.

    last line in ``ui_elements`` is ``op.onCancel.append(cleanup)`` which appends ``cleanup`` function
    to delete any remaining extra objects when operator finishes.

    This can have bugs.


..  literalinclude:: ../codes/Duplicator/duplicateGrid2.py
    :language: python
    :linenos:



..  rubric:: Footnotes:

..  [#f1]   Object Pool is a technique, frequently used in games, in which, objects are created/destroyed from a pool of objects.
            So, a few objects can be created in the beginning and whenever objects need to be created/deleted they are pulled
            from/pushed to that pool. This increases the performance as memory is not freed every time an object is deleted
            and then again allocated when object is recreated. So, it's easy on garbage collector.