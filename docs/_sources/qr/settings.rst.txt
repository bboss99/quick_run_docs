..  _qr_settings_title:

Settings
==========

you can open the ``settings.json`` file by going to ``open>> settings``.

``settings.json`` file is located in quick_run install directory.


..  note::

    Addon writers might know that Addon settings are saved in a class inherited from ``bpy.types.AddonPreferences``.
    You can do that, but I think ``settings.json`` file can be more intuitive in many cases.


settings.json
---------------

..  literalinclude:: ../files/settings_qr.json
    :language: json




* root_dir:
    default value: ""

    This is directory where scripts are saved. When empty, it opens ``addon_install_directory/Scripts``

    When using :ref:`ChangeRoot<change_root_title>` menu, it changes this property, **so you don't have to
    manually change here.**

* ttt_lines:
    default value: 4

    This many number of lines shown as tool tip text


* title_width:
    default value: 200

    Menu Title's width in pixel

* title_height:
    default value: 30

    Menu Title's height in pixel


* element_width:
    default value: 200

    Menu button's width in pixel

* element_height:
    default value: 25

    Menu button's height in pixel

* element_width:
    default value: 200

    button's width in pixel


* use_context_space:
    default value: false

    There is always visible button :ref:`use_space<use_space>`. So no need to change it in file.


* extra_buttons_on_menu:
    default value: false

    This moves the :ref:`ChangeRoot<change_root_title>` and :ref:`Open<open_menu>`  to main Menu.


..  note::

    other than changing Menu's dimensions ``extra_buttons_on_menu`` and ``ttt_lines`` you can change in this
    file directly. To change ``use_context_space`` and ``root_dir`` there is a way to do it from UI.
