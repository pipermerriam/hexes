from hexes import (
    Application,
    Box,
    Style,
)

lipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ac justo sapien.
In hac habitasse platea dictumst. In aliquam felis eget turpis sagittis, ac
convallis quam euismod. Nam commodo enim vel vestibulum tempus. Fusce ac
interdum dolor, vel sodales neque. Vivamus consectetur euismod maximus. Interdum
et malesuada fames ac ante ipsum primis in faucibus. Lorem ipsum dolor sit amet,
consectetur adipiscing elit. Nunc odio metus, volutpat ut congue non, egestas id
ligula. Aenean egestas pellentesque felis vitae consectetur. In nec sem vitae
neque pellentesque facilisis. Mauris dignissim lorem id pretium tincidunt.
Pellentesque non erat erat. Aenean lobortis nec lorem nec vehicula. Nam eget
lacus faucibus, lacinia ipsum eget, volutpat purus.

Integer nec molestie massa. Pellentesque eu lectus nec nunc faucibus pretium ac
ut lacus. Nulla sit amet tellus quis orci bibendum pharetra. Maecenas quis
placerat mi. Suspendisse ligula tellus, iaculis at rutrum ut, elementum vitae
est. Fusce vehicula commodo tellus sed finibus. Pellentesque non bibendum quam.
Nullam consectetur vestibulum ligula, non molestie odio mattis vitae. Proin
sapien nulla, sollicitudin quis fermentum non, luctus et dolor. Donec vel velit
euismod, accumsan lacus vitae, varius justo. Duis in erat dolor. Maecenas non
sapien a lacus posuere ultrices sit amet eget quam. Sed vel tellus risus.
Suspendisse ac leo pharetra, dictum sem ac, malesuada mauris. Donec in eleifend
mauris. Vestibulum eu rhoncus nibh.
""".strip()

root = Box(
    style=Style(
        layout=Style.Layout.Horizontal,
    ),
    children=(
        Box(
            children=(
                Box(
                    text=lipsum
                ),
                Box(
                    style=Style(
                        height=3,
                    ),
                ),
            ),
        ),
        Box(
            style=Style(
                width=20,
            ),
        ),
    ),
)

with Application(root=root) as app:
    app.register('q', app.quit)
    app.run()