.. _use_space:

use_space
===========

It's a toggle button.

This is one of the most important feature.

When on(green):
    will pop different set of menus based on context/area like ``3D_VIEWPORT``, ``GRAPH_EDITOR``, ``TEXT_EDITOR`` etc.

..  note::
    Blender's quick shortcut button (shortcut Q) works this way by default, meaning different areas have
    different entry based on context.

When off(reddish):
    will pop common set of menus for all context/area


..  rubric:: Areas

.. literalinclude:: ../files/spaces.txt


..  note::

    In Future there will be even more categories, based on modes (like edit mode, object modes etc),
    use_context is more appropriate name for this.