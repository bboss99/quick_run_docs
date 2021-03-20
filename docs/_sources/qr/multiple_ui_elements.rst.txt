..  _mulitiple_ui_elements_title:

Multiple ui_elements functions
=================================


There are times when you have to write one or few lines of code file to create a menu button entry.

It requires creating a lot of files. They can be placed in a folder and you can copy/paste/share that folder just fine.

but there is another way. See the example below to understand.

Example
---------

Below are few one-liner scripts, to create plane, cube, circle, uv_sphere, ico_sphere and cylinder respectively.

..  code-block:: python
    :caption: "plane.py"

    import bpy
    bpy.ops.mesh.primitive_plane_add()

..  code-block:: python
    :caption: "cube.py"

    import bpy
    bpy.ops.mesh.primitive_cube_add()

..  code-block:: python
    :caption: "circle.py"

    import bpy
    bpy.ops.mesh.primitive_circle_add()

..  code-block:: python
    :caption: "uv_sphere.py"

    import bpy
    bpy.ops.mesh.primitive_uv_sphere_add()


..  code-block:: python
    :caption: "ico_sphere.py"

    import bpy
    bpy.ops.mesh.primitive_ico_sphere_add()


..  code-block:: python
    :caption: "cylinder.py"

    import bpy
    bpy.ops.mesh.primitive_cylinder_add()


|

..  _mulitiple_ui_elements_example:

..  rubric:: You can put them in one file as shown below.

..  code-block:: python
    :caption: "create_mesh_obj.py"

    import bpy
    def ui_elements_plane(op):
        bpy.ops.mesh.primitive_plane_add()

    def ui_elements_cube(op):
        bpy.ops.mesh.primitive_cube_add()

    def ui_elements_circle(op):
        bpy.ops.mesh.primitive_circle_add()

    def ui_elements_uv_sphere(op):
        bpy.ops.mesh.primitive_uv_sphere_add()

    def ui_elements_ico_sphere(op):
        bpy.ops.mesh.primitive_ico_sphere_add()

    def ui_elements_cylinder(op):
        bpy.ops.mesh.primitive_cylinder_add()

Now you will see a menu entry named ``create_mesh_obj.py``. When clicked. You would see a menu pop up.

You can see every function name is prefixed with ``ui_elements_`` . You get a menu entry for all
the functions prefixed with ``ui_elements_``. So for function ``ui_elements_plane`` you get the menu
entry plane.

..  note::
    it's ``ui_elements_`` there is a underscore, which is must. ``ui_elements_plane`` is easier to read than
    ``ui_elementsplane`` which won't work.


SubMenu file(_m_)
------------------

If you just prefix your file name with ``_m_`` then instead of pop-up, you will get a submenu, which can be handy.
in the above example file name should be ``_m_create_mesh_obj.py``.



