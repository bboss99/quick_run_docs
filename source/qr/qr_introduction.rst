..  _title_qr_introduction:

Introduction
===============


.. _Quick Run: https://gum.co/quick_run

.. |qr| replace:: `Quick Run`_

Once, script become part of your workflow, you will have 1000s of script, some will save you 30 seconds and some that
save you 2 minutes.


"|qr|" will help you organize 1000's of files easily and can save you a lot of time. Moreover,
How it will do it, go through pages in this section to find out.


.. note::

    If you have used programs like Maya, you know how important shelf can be. If you do, you can skip this note.
    If you don't or those who haven't used Maya, should
    know that it's simply container for scripts, which can be used for storing 1 line script or a whole program.

    Now forget about Maya, Imagine you are new to any software and you want to save camera position in a large scene
    because you keep coming back
    to that position. As you are a beginner, you don't know right way of doing it in the software. What would you do?

    Imagine you are making a character smile, so you want to select control curves for lips, cheeks and eye region.
    You keep finding yourself selecting the same thing again and again. You want to store it somewhere but,
    since you are a beginner, you don't know how that particular software
    does that. What would you do?

    Now think of above two situation combined, meaning, you want to focus on character's face (change camera position) and
    select the facial control curve. What would you do?

    Following are the solution in the form of pseudocode, you can see they are only few lines of code.

    solution for situation 1:  ``camera.positon = (xPos,yPos,zPos); camera.eulerAngles = (xRot,yRot,zRot)``

    solution for situation 2: pseudocode ``select_object([cc_lips,cc_cheeks,cc_eyes])``

    solution for situation 3: solution 1 + solution 2

    Just by pressing those button, you saved 30 seconds to 1 minute!!

