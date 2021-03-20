
Naming Convention
---------------------

You can name files or folder anything. It's the name of the file/folder that is displayed in the menu/button.

File/Folder names starting with ``.`` and ``_`` are hidden.

Name starting with ``.`` is hidden and usually used by IDE and OS to save configurations, so showing those files is useless.

Since files and directory whose name starts with ``_`` are not listed. They can be treated specially.


If script requires other files eg. .blend, .flx, .json it can be placed in a folder like ``_files`` since that folder is
ignored by "Quick Run". So in programming analogy this can be used like private folders, that's very crude analogy but you
got the idea.


In Quick Run (paid) addon, I have used ``_m_`` and ``_d_`` prefixes for some files and directories, and they are treated
differently. Check :ref:`Multiple ui_elements <mulitiple_ui_elements_title>` and :ref:`Dynamic Menu<dynamic_menu_title>`