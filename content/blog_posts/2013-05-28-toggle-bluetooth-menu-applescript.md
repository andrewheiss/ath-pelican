Title: Toggle the Bluetooth menu item with AppleScript
Excerpt: The OS X Bluetooth menu item re-enables itself everytime a device battery gets low. This simple application turns it back off. 
Category: blog
Tags: osx, automation, AppleScript
Slug: toggle-bluetooth-menu-applescript


I like to keep my menubar as uncluttered as possible, so I keep as many items hidden as possible—especially system programs like Time Machine, the displays menu, or the volume menu. 

![Clean menu bar](http://files.andrewheiss.com/images/toggle_bluetooth/menubar.png)

I also keep the Bluetooth menu turned off. However, when the battery runs low on either my keyboard or mouse, the Bluetooth menu item comes back, and it doesn't turn back off after the batteries get replaced. The only way to turn it off is to go to the Bluetooth panel in System Preferences and disable the menu item manually. It's a tiny chore, but a chore nonetheless. One that can be automated\![^fn1][^fn2]

Save [this](https://gist.github.com/andrewheiss/5667322) to an AppleScript application (or an Automator application) and run to (kludgingly) toggle the Bluetooth menu item.

```applescript
tell application "System Preferences"
  activate
  set the current pane to pane "Bluetooth"
  delay 1
end tell

tell application "System Events"
  tell process "System Preferences"
    set toggleBluetooth to the checkbox "Show Bluetooth in menu bar" of the window "Bluetooth"
    click toggleBluetooth
  end tell
end tell

tell application "System Preferences"
  quit
end tell
```


[^fn1]: See [this fantastic graph](http://files.andrewheiss.com/images/toggle_bluetooth/geeks-vs-nongeeks-repetitive-tasks.png) originally posted by [Bruno Oliviera](https://plus.google.com/+BrunoOliveira/posts/MGxauXypb1Y).

[^fn2]: And by spending 15 minutes figuring out the hidden Applescript API for System Preferences to automate a task that takes up 30 seconds every month, [I totally saved time in the long run](http://xkcd.com/1205/).



