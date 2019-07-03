#!/bin/sh
function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
run pamac-tray &
run volumeicon &
run nm-applet &








/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
