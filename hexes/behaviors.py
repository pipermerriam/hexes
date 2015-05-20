import asyncio


@asyncio.coroutine
def render(app):
    """
    The core rendering loop.

    Do not schedule this with ``app.on``; it is scheduled automatically when
    you start the application.
    """

    if app.root.dirty:
        app.log("Rendering")
        app.stdscr.refresh()
        app.recalculate_windows()
        for box, win, pad in app.windows:
            win.refresh()
            x, y = box.upper_left
            dx, dy = box.lower_right
            pad.refresh(0, 0, y + 1, x + 1, dy - 2, dx - 2)
        app.root.dirty = False
    # I'd love the idea of "repeat this indefinitely" to be expressed in the
    # decorator used, but that might deny the ability to key it off particular
    # logic?
    app.schedule(render)


@asyncio.coroutine
def quit(app):
    """
    Basic quitting behavior.

    Typically, you'll want to schedule this with:

    .. code-block:: python

        app.on('q', quit)

    or something similar.
    """

    app.loop.stop()
