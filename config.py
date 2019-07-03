import os
import re
import socket
import subprocess

from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule , Match, ScratchPad, DropDown
from libqtile.command import lazy, Client
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer


try :
	from typing import List  # noqa: F401
except ImportError:
	pass

mod = "mod4"
home = os.path.expanduser('~')

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("termite")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),

    Key([mod , "shift"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
	Key([mod], "d", lazy.spawn("rofi -show drun")),
]
'''
groups = [Group(i) for i in "asdfuiop"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])
'''

# for those keen on auto-start
group_spawns = [None, None, None, None, None, None, None, None]
# auto-sort programs
group_matches = [[Match(wm_class=["Atom" ,"atom",],),], [Match(wm_class=["Firefox" ,"firefox",],),], [Match(wm_class=["Thunar" ,"thunar",],),], None, None, None, None, None]
# if labels != keys
group_labels = ['1', '2', '3', '4', '5', '6', '7', '8']
group_names = ['ampersand', 'eacute', 'quotedbl', 'apostrophe', 'parenleft', 'minus', 'egrave', 'exclam'] #list("asdfuiop")

groups = [
    Group(name=group_name, label=group_label,
          spawn=group_spawn, matches=group_match)
    for group_name, group_label, group_spawn, group_match in zip(
        group_names, group_labels, group_spawns, group_matches
    )
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            # mod1 + shift + letter of group = switch to & move focused window
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ]
    )



groups.append(
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "/usr/bin/termite", opacity=0.88, height=0.35, width=0.80, ),

        # define another terminal exclusively for qshell at different position
        DropDown("qshell", "/usr/bin/termite -e qshell",
                 x=0.05, y=0.4, width=0.9, height=0.6, opacity=0.9,
                 on_focus_lost_hide=True)
    ]), )

keys.extend([
    # Scratchpad
    # toggle visibiliy of above defined DropDown named "term"
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([], 'F11', lazy.group['scratchpad'].dropdown_toggle('qshell')),
])




layouts = [
    layout.MonadTall(margin=8, border_width=4, border_focus="orange", border_normal="#4c5666"),
    #layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox( highlight_method = "text",),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            24, background="#242636",
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])



auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
