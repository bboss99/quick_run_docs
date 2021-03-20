
Advanced Details
-------------------

At the heart of it there are two ways to load a file and execute it.

`first way <https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path>`_

.. code-block:: python

   import importlib
   from os.path import basename

   def getModule(filePath):
       moduleName = basename(filePath).split('.')[0]
       spec = importlib.util.spec_from_file_location(moduleName, filePath)
       mod = importlib.util.module_from_spec(spec)
       spec.loader.exec_module(mod)
       return mod

or a more common way from blender manual

.. code-block:: python

   import bpy
   filepath = bpy.path.abspath(r"D:\path\to\file.py")
   exec(compile(open(filepath).read(), filepath, 'exec'))

Former option allows loading of modules and it's function can be accessed, it searches for ``ui_elements`` functions
and calls it.
In later way, function will have to be called explicitly. so it's commented out, since it will require more typing
in each file. Though it will be slightly easier to implement.
