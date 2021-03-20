.. _quick_run_free_title:

Quick Run Free
==================

This is basic and limited version of Quick Run. You can run all scripts with it, it's limited only in the sense of Script
organization and user experience. All boss features(UI) will work in it.

UI
----
.. image:: ../imgs/qr_free.png
   :alt: 'quick run'


1. Buttons:
    button is created for every file in Script directory.

2. Addon directory:
    opens addon install directory

3. Scripts directory:
    opens directory where scripts are saved.

    .. NOTE::
       This folders is not python package. You can see that there is no __init__.py file.

4. Reload Settings:
    Reloads settings immediately after making change, so that you won't have to restart blender.

    see :ref:`settings.json<qr_free_settings>`

5. Help:
    Before writting this documentation. I wanted to make integrated tutorial kind of thing. So it's kind of useless
    now.

.. _qr_free_settings:

settings.json
---------------

Settings are saved in ``settings.json`` file. You can open that file by pressing ``Addon Directory`` button. This opens
install directory of addon. You can find ``settings.json`` file among other files and folders.

.. literalinclude:: ../files/settings_qr_free.json
    :language: json


* root_dir:
    default value: ""

    This is directory where scripts are saved. ``Scripts directory`` button opens this path.
    When empty, it open's ``addon_install_directory/Scripts``

* ttt_lines:
    default value: 4

    This many number of lines shown as tool tip text

* element_height:
    default value: 25

    button's height in pixel

* element_width:
    default value: 200

    button's width in pixel

* element_space:
    default value: 5

    distance between two button in pixels

* start_point:
    default value: [-1,-1]

    when it's set to -1, -1, first button is created at mouse location.
    if set to [20, 400], first button will be created at that location.

    rest of the buttons will be created according to ``direction`` setting.

* normal_color:
    default value: [0.1,0.1,0.1,1]

    r g b a value of button's normal color: eg (for red: [1.0,0.0,0.0,1])

* hover_color:
    default value: [0.15,0.15,0.15,1]

    r g b a value of button's hover color: eg (for red: [1.0,0.0,0.0,1])

* direction:
    default value: "down"

    every new button are created below last

* clip_buttons:
    default value: true

    When true, long text will be clipped by rectangle size.

* _show_help:
    default value: true

    it's useless :):)

* screen_margin:
    default value: [50,100]

    button's won't be created [from top, from bottom] in the space/region


.. note::

    Addon writers might know that Addon settings are saved in a class inherited from ``bpy.types.AddonPreferences``.
    If you are writting addon, you can do that, but I think settings.json file can be more intuitive in many cases.
