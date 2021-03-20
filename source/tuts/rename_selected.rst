..  _tut_rename_selected_objects:

Rename Selected objects
=========================


This script is very short in the sense that there is only one line of blender code ``object.name = textfield.value``
to rename object.



..  tabs::
    ..  tab:: Step 1

        In this step we simply rename active object.

        ..  literalinclude:: ../codes/Renamer/step_01.py
            :language: python
            :linenos:

    ..  tab:: Step 2

        In this step we repeat step 1 in a loop.

        .. note::

            Logic to create textfield in a loop is same as quick_run_free addon (where buttons
            are created in a loop.)

            So when more objects are selected that can't fit in one column textfields will be created in new
            column.

        ..  literalinclude:: ../codes/Renamer/step_02.py
            :language: python


    ..  tab:: Step 3

        ..  warning::

            I can see that changing TextField should also change selected object, that will be better user experience.

            There is no callback for when you click on Textfield and enter textfield typing mode.

            Temporarily, I solved it by making another class and overriding ``_makeEditable``. but that method is supposed
            to be private. And, a user has no way of knowing that, since it's not documented.

            In future updates, there can be a callback method for ``onTextFieldChanged`` or something.

        ..  literalinclude:: ../codes/Renamer/step_03.py
            :language: python


    ..  tab:: Step 4

            In Maya (3d software), this type of script is very useful and enough to rename joint hierarchy (bones). Since blender's works
            differently, and there are ``context`` and ``modes`` some extra work is required. A generic object Renamer isn't enough here.

            To convert this script into an addon - :ref:`To make an addon.<convert_to_addon>`



