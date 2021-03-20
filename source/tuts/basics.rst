..  _tut_basics:

Basic Scripts (No UI)
======================

Some times, you don't need a UI but just a button to run some code.


Following are some example scripts to help you get started.



:ref:`Important tips<basic_important_tips>`



..  toggle-header::
    :header: **1. Select All Animated Objects**

        ..  literalinclude:: ../codes/Animation/selectAllAnimated.py
            :language: python
            :linenos:

|

..  toggle-header::
    :header: **2. Set Animation Range to selected object/s animation range**

        ..  literalinclude:: ../codes/Animation/setAnimationRange.py
            :language: python
            :linenos:


|

..  toggle-header::
    :header: **3. Create Curve Object with no CP**

        ..  literalinclude:: ../codes/Modeling/createEmptyCurve.py
            :language: python
            :linenos:


|


..  toggle-header::
    :header: **4. Create Curve Object with single CP**

        ..  literalinclude:: ../codes/Modeling/createOneCPCurve.py
            :language: python
            :linenos:


|

..  toggle-header::
    :header: **5. Separate select mesh object faces**

    As you can see, these are unedited code from info panel pasted as it is, which just worked for me.
    I didn't even bother to edit the long line which has so many default parameter

        ..  literalinclude:: ../codes/Modeling/separateFaces.py
            :language: python
            :linenos:


|


..  toggle-header::
    :header: **6. Purge Orphan Data**

        ..  literalinclude:: ../codes/purge.py
            :language: python
            :linenos:


|


..  _basic_important_tips:

..  tip::

    Tips For beginners coders, for majority of tasks, rarely you need to write from scratch.

    1.  If you turn on ``preference->interface-> developer extra`` you get a ``copy python command`` in
    the context menu.

    2.  Copy code from info_panel, it's reflects history of commands you ran from interface.

    3.  All the addons that are installed or you can find in net. ``execute`` method is called when operator is run,
        so you can copy that code and any other function that is called by that method

    4.  Online from blender stack_exchange, blender_artist, SO etc
