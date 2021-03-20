..  _tut_array_modifier:

Array Modifier Grid
=============================

This is a practical common scenario where we need to create objects in a Grid, particularly in motion graphic projects.

In this Tutorial, We'll see how we can write scripts and add functionality step by step. I will try to make each addition
only around 5 lines.


..  note::

    This is first tutorial so it contains somewhat detailed instruction, later tutorials aren't as details to avoid
    repetition.


.. tabs::

    .. tab:: Step 1

        ..  literalinclude:: ../codes/ArrayModifier/step_01.py
            :language: python
            :linenos:

        There are 4 sub-steps:
            1. create cube.
            2. add array modifier
            3. change array modifier's properties.
            4. apply and reset origin(centering pivot)

        There are several things to note in above code, lets see.
            1. sub-step 4 will be same however many copies we create.
            2. sub-step 3, ``relative_offset_displace`` and ``count`` should be ``floatField`` and ``intField`` respectively.
            3. sub-step 2, more modifiers can be added for all 3 axis
            4. sub-step 1 can be an option, where we create any any mesh type. (eg. Sphere,Cylinder)



    .. tab:: Step 2

        Things to note:
            1. highlighted lines are added.
            2. one more modifier is added.
            3. added modifiers ``relative_offset_displace`` is changed so that it goes in y axis.

        .. literalinclude:: ../codes/ArrayModifier/step_02.py
            :language: python
            :linenos:
            :emphasize-lines: 9,13,14,18,19,24



    .. tab:: Step 3

        Things to note:
            1. highlighted lines are added.
            2. all three modifiers are added.
            3. added modifiers ``relative_offset_displace`` is changed so that it goes in z axis.

        .. literalinclude:: ../codes/ArrayModifier/step_03.py
            :language: python
            :linenos:
            :emphasize-lines: 10,16,24-26,32

    .. tab:: Step 4

        Now it's time to add the boss feature, adding UI.

        Check out :ref:`boss documentation<boss:boss_index>` documentation, especially :ref:`Button class <boss:button_title>`


        Things to note:
            #. at line 4, ``create_grid`` function is defined to create object and add modifiers.
            #. at line 8, reference to selected object is saved in ``sel_obj``, which is return at last.
            #. at line 33, ``apply_mods`` contains applying part, has been moved to another function
            #. at line 54, ``caller.op.quit()`` quits the operator.
            #. at line 68, ``UICreator.deleteAllUi(op)`` deletes all previously created UI.
            #. at line 70, grid is created and returned object is saved in ``sel_obj``
            #. VectorIntField and Button are created and ``sel_obj`` is passed as ``param`` value.


        .. literalinclude:: ../codes/ArrayModifier/step_04.py
            :language: python
            :linenos:
            :emphasize-lines: 67-

        ..  note::

            ``FieldValue`` class is mainly used when setting minimum and maximum limits for  field value. It's
            parameters are self-explanatory. ``value`` is default value, ``min`` is minimum value, ``max`` is
            maximum value and ``changeBy`` is mouse-roll update value. Be careful to pass three values for
            ``Vector(Int/Float)Fields``. Same class is also used for ``(Float/Int)Field`` as ``FieldValue(3,0,10,1)``


    .. tab:: Step 5

        If you want :ref:`To make an addon.<convert_to_addon>`