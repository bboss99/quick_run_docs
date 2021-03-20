..  _tut_turntable_camera:

Turntable Camera
======================

..  tabs::

    .. tab:: Step 1

        Following code is copied from info_panel, slightly updated, few variables are added to make it work.
        It's well commented so you can read through it.

        .. literalinclude:: ../codes/Turntable/step_01_02.py
            :language: python
            :linenos:


        This script for simple turntable doesn't require any UI. It's not a very frequent script, it is run at the end of a process of modeling
        texturing, maybe once for each model or scene.

        changing ``frame_start`` and ``frame_end`` at line 54 and 55, manually before running script, is not very
        inconvenient, or running the script and then editing keyframe in timeline is also smooth process and so is
        changing size/radius of circle curve or changing empty/camera target position in viewport.

        **But, if we insist on creating UI**, we can create IntFields for ``frame_start`` and ``frame_end`` in the
        step 2.


    .. tab:: Step 2

        Just for demonstration, in this step we create two ``IntField``  for ``frame_start`` and ``frame_end``

        .. literalinclude:: ../codes/Turntable/step_02.py
            :language: python
            :linenos:

.. tip::

    Making camera a child of an object and rotating the object, creates a basic turntable
    but isn't very customizable.

    Whenever there are more ways of doing certain thing. Choose one, which is more
    customizable. In the above approach, there are many ways to customize the process.
    We can change camera position, change curve shapes, change keyframes interpolation,
    move camera target (empty object) far/near and animate it if needed.
