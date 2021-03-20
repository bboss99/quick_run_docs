.. _change_root_title:


ChangeRoot
==============

In Quick Run, You can have as many root folder as you want and easily switch between them.

You can go to ``open>>`` menu and press ``root_dir_options``. This should open a text file ``root_dir_options.txt``,
in default text editor of your operating system. Now, you can write one path per line in file and save. Then you can go
to ``ChangeRoot`` menu that all the paths will show up immediately. Change whichever folder you want to open.

..
    EDITME take a screenshot

You can create new category by creating a subfolders (or nest subfolders) in root_dir. This gives you
another level of categorization of scripts.

..  rubric:: When to create new root_dir?

1.  There are various cases when you want to create new Root folder. It's like starting from a clean slate.
    For eg. when you are starting a new project, you want to save files related to that folder.

2.  While rigging you will want to have files related to bones, skin weights, control curves etc. and while
    Modeling something entirely different set of menus.

3.  If you are part of three member team, then you can share each others scripts using shared folder.
    (Dropbox or Google Drive)

4.  You want to write and share and collaborate then you can git clone in this folder.


..  tip::

    In my PC, I have a made a directory ``qr_root`` and All the other root directories are under it.
    So I set root_dir to ``qr_root`` I get all the other root_dirs as it's submenu and I can always change
    to specific directory if I need.

    ..  image:: ../imgs/qr_root_dir.png


.. WARNING::
   These folders are not python packages. You can see that there is no __init__.py file.

