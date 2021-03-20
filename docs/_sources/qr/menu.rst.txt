
Menu
==============

This page details about Menu class and it's ups and downs

1.  When number of menu entries exceeds what can fit in the space/window, You can roll MMB to go up and down.

2.  Point 1, feature is nice, but it's not a good idea to put too menu entries in a menu so that one has to scroll MMB.
    Keep number of entries below 10 or 12 so it is easy to manage. Create a new folder/sub folder/root folder to manage that.

3.  It don't need mention since that's how menu's actually work. This part is internal detail. Menu always tries to find
    a way if it can fit in the space/window to avoid any scrolling from user. so it may
    appear left/write or going up/down based on where it appeared.


..  rubric:: Notes

There are things that I don't like about how Menu class works:

1.  It's greedy evaluation. If there are 100s or 1000s of menu entries it will create all the button during creation
    and draw them, instead of only those button that are only visible.

2.  The way it works is every button is clipped,not very efficient shader work. You can see that when you drag the menu.
    There is already a way to combine geometry but it's still under progress.

3.  At the moment their is no separate timer or thread, therefore tooltips and menus appear and disappear as soon as
    cursor enters or exits, it doesn't feel smooth. When and if timers are added, there can be a delay of .2 second for
    submenu to appear and 1 second for tool tip to appear.

4.  There is no caching. Every created menu/submenu is destroyed and recreated again, if cursor exits and re-enters or
    When operator is relaunched.