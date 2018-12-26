# Outline-Simple plugin for GIMP
A simple Outline effect for GIMP. It works by adding a border to the content of a layer.

# Usage
1. Create a text layer (or any other layer), and make it the active one

![Before](https://github.com/LatinSuD/outline-simple/raw/master/samples/outline1.jpg "Before")

2. Go to menu Filters → Decor → Outline Simple

![After](https://github.com/LatinSuD/outline-simple/raw/master/samples/outline2a.jpg "After") ![After](https://github.com/LatinSuD/outline-simple/raw/master/samples/outline2b.jpg "After")

# Installation
1. Download `outline-simple.py`
1. Copy it to your plugin folder ( typically `~/.gimp-2.8/plug-ins/` )
1. Restart GIMP

# Additional notes

The effect can be performed manually without this plugin, this will just make it in a more automated fashion.
The steps are: set alpha to selection, grow selection, create new transparent layer, move new layer down, fill selection, blur.

This has been tested on GIMP 2.8 on Linux

There is a similar plugin here http://pete.nu/software/gimp-outliner/
