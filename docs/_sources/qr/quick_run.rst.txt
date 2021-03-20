.. _quick_run_title:

Quick Run
===========

This does everything that free version does. Other than that it makes it easy to save and organize scripts.

UI
----

.. image:: ../imgs/qr.png
   :alt: 'quick run'

1. Menu
    It contains:

    1. All the files and folder as buttons.

    2. ``OpenDir`` button:

        Opens the directory in that folder

    3. :ref:`Save from CB (Clipboard)<save_from_cb>` button

2. :ref:`use_space for contextual menu <use_space>`

3. Help: just a slideshow of of image. It's of no use.

4. :ref:`Open>><open_menu>`

5. :ref:`Change Root<change_root_title>`

6. Reload Settings
    Reloads settings immediately after making change, so that you won't have to restart blender.

    see :ref:`settings.json<qr_free_settings>`


.. _save_from_cb:

Save from CB (Clipboard)
--------------------------
Some times when you quickly want to save some text in a file in a particular directory and don't want to leave blender
UI, you can do so by pressing this button. First you copy the text to put it in clipboard

Just press CTRL + A,C in Text Editor to select all the text or select whatever text you need.

.. WARNING::

    First copy text then press ``Save from CB``

    Cancel and Save buttons don't work, while editing TextField, Press Enter or Escape to save or cancel.
    (This isn't desired behaviour and this issue will be solved with future updates of boss)



.. _open_menu:

Open Menu
-------------

``Open>>`` Menu is always visible. It has buttons to open important folders and files.


You get a tooltip what each button does.

Two are important for users:

    1.  ``root_dir_options.txt`` text file. It's use is covered in :ref:`Change Root<change_root_title>`
    2.  ``setting.json`` json file. see :ref:`settings <qr_free_settings>` for details


.. note::

    ``scripts directory`` and ``custom scripts directory`` are not useful. It's there because I need to
    go to these folders a lot during development. At the moment, it is hardcoded in the file. In future,
    I will make it customizable.



