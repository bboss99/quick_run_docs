.. _quickStart_title:


Quick Start
===============

.. include:: ../files/links.rst

.. note::
    This Quick Start page and tutorial is shown using free version. After this page, head over to
    :ref:`Tutorial Section<tut_basics>`


You can get started with free version |qrf|. Check :ref:`Installation page <installation_title>` for details.

.. image:: ../imgs/qr_free.png
   :alt: 'quick run'

|

..  rubric:: For example, look at following code of creating  cube from :ref:`Comparisons page <boss:comparisons>`

..  literalinclude:: ../codes/Boss/create_cube.py
    :language: python
    :linenos:
    :caption: create_cube.py


..  rubric:: How would you run above ``create_cube.py`` script? Read the following section.

|

Important Scripts
-------------------

Two Scripts are placed in the script directory.
    1. run_clipboard.py
    2. run_qr_text.py

.. image:: ../imgs/imp_buttons.png
    :alt: 'important buttons'
    :scale: 50 %

These scripts are helpful to test scripts before saving code in a file.

run_clipboard.py
+++++++++++++++++++++

This is a one-liner script that helps to run text on clipboard.

.. literalinclude:: ../codes/run_clipboard.py
    :language: python
    :linenos:
    :caption: run_clipboard.py



copy the above ``create_cube.py`` text and press ``run_clipboard.py`` button. This code runs!!!!


.. note::
    This one liner script is useful for testing code easily by coping from web-browser or external
    /internal text-editor. This way, you can run example scripts shown in documentation, including all
    the code in the :ref:`tutorial section<tut_basics>`.


..
    EDITME make video


run_qr_text.py
+++++++++++++++++

This is another small script, which cuts the step of copying the text. If your code is in ``qr_text`` named TextData
block in TEXT_EDITOR, You can launch the quick_run/free and press ``run_qr_text.py``. This way, if you want to modify
code(eg you copied from tutorial), you can do that in text editor and press ``run_qr_text.py``

.. literalinclude:: ../codes/run_qr_text.py
    :language: python


.. note::

    These scripts are very helpful since, sometimes it can be used to avoid ``wrong context - poll failed`` error, which is very
    common when copying code from info panel. You can launch quick_run/free in the correct region/space and problem may
    be avoided.

..
    EDITME make video

|

Saving your Script
------------------------

If you want to save, ``create_cube.py`` ,first copy the text, press ``Scripts Directory`` it will open the folder.
Create the file ``create_cube.py`` and paste the text in the file. Relaunch addon (press F2)


..  important::

    By default all the scripts are saved in a sub-directory within addon install directory. You must change the
    :ref:`root directory in settings<qr_free_settings>`.

    This way, if you have multiple blender installation, they all
    can use same root/script directory. Second, You can open root directory in external editor(eg VSCode). Further,
    You can save your codes in github.( and doing all that inside a subdirectory of addon doesn't feel right!!)

..
    EDITME make video

|

ui_elements
-------------

``ui_elements`` is name of function that is called by quick_run/_free. It's hardcoded. It could just as well have been ``foo``.

``ui_elements`` is also name of method that is overridden in the class to create UI. check here :ref:`convert script to addon<convert_to_addon>`.

