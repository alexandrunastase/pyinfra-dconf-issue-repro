from pyinfra.operations import server


server.shell(
    name='dconf write test',
    commands='''dconf write /org/gnome/desktop/wm/keybindings/close "['<Primary>q']"''',
    sudo=True,
)

# Same result when escaping the quotes
# server.shell(
#     name='dconf write test',
#     commands='dconf write /org/gnome/desktop/wm/keybindings/close "[\'<Primary>q\']"',
#     sudo=True,
# )