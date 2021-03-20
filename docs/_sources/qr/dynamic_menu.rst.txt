.. _dynamic_menu_title:


Dynamic Menu
===============

This part makes it very versatile.

You can write a python file in which you write a ``get_sub_md`` function that returns several python lists which
are used to creates the submenu.



Examples
----------

..  code-block:: python
    :caption: "_d_dynamicMenu.py"

    def foo(caller):
        print('foo called', caller.param)

    # def foo():
    #     print('foo called')

    def get_sub_md():
        # texts, onClicks, toolTipTexts,toolTipImages, get_submenu_data_fns, params
        return ['a', 'b', 'c'], [foo, foo, foo], ['ttt', 'ttt2', 'tt3'], ['']*3, [None]*3, ['param_x', 'param_y', 'param_z']



Save the above file as ``_d_dynamicMenu.py`` in any folder.

The name of file must begin with ``_d_``, otherwise this file will be treated as regular file which has a ``ui_elements``
function instead of ``get_sub_md`` function.


..  hint::
    Remember d as data in  ``_d_``. since this function returns data, data to create submenu.


Return values of ``get_sub_md`` function. There are 6 lists. All should have same length equal to ``number_of_entries``
    1. texts list
    2. functions list
    3. tool tip text list, must return ``['']*number_of_entries`` if no tooltip is needed.
    4. tool tip image list, must return ``['']*number_of_entries`` if no tooltip image is needed.
    5. should be ``[None]*number_of_entries``
    6. params lists, list of length must be ``number_of_entries``, list element can be any python object.


Example 2
----------

Implementing primitive example  :ref:`create_mesh_obj.py<mulitiple_ui_elements_example>` from multiple ui_elements page.

You can get same results but by writing one ``get_sub_md`` function as shown below.

You can save the following text as ``_d_create_mesh.py`` in any folder.

..  literalinclude:: ../codes/_d_create_mesh.py
    :language: python


Above code doesn't need much explanation. ``primitives`` is a list of strings, which is
returns as texts, toolTipTexts and params.

Function ``create_primitive`` uses :ref:`caller syntax<caller_title>`.

Code below show above functionality but uses lambda function just to demonstrate that it can be done.


..  literalinclude:: ../codes/_d_create_mesh2.py
    :language: python


.. note::
    check out :ref:`Text Editor Scripts<text_editor_scripts>` for more practical examples
    of dynamic menu.
