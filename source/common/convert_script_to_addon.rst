..  _convert_to_addon:

Convert Script To Addon
=========================


..  note::
    You can share/sell your addons, just tell them to :ref:`install boss package<boss:installation_title>`.

You simply inherit from :ref:`Boss_OT_base_ui <boss:boss_ot_base_ui_title>`

if you have a ``ui_elements`` function

..  code-block:: python

    def ui_elements(op):
        # do something useful here, like create some ui
        pass

You copy and paste as shown in highlighted part.

..  code-block:: python
    :linenos:
    :emphasize-lines: 9-11

    import bpy
    from boss.ui_creator import Boss_OT_base_ui

    class Your_OT_operator_name(Boss_OT_base_ui):
        """What your operator does"""
        bl_idname = "your.operator_name"
        bl_label = "Operator Label"

        def ui_elements(op):
            # do something useful here, like create some ui
            pass


    def register():
       bpy.utils.register_class(Your_OT_operator_name)

    def unregister():
       bpy.utils.unregister_class(Your_OT_operator_name)


    if __name__ == "__main__":
       register()

    # test call
    # bpy.ops.your.operator_name()


.. note::

    You don't write usual methods like invoke, execute and modal.

    There are some other methods that can be overridden, but they are not final yet.

    classmethod poll method can be written.