#!/usr/bin/python

# Outline Simple creator plugin for GIMP
# https://github.com/LatinSuD/outline-simple/

from gimpfu import *


def plugin_main(image, layer, border=10, color=(255,255,255), blurriness=0):

  pdb.gimp_image_undo_group_start(image)

  try:

    # Prepare for different types of input images
    if (pdb.gimp_image_base_type(image) == RGB):
      ltype = RGBA_IMAGE
    elif (pdb.gimp_image_base_type(image) == GRAY):
      ltype = GRAYA_IMAGE
    else:
      ltype = INDEXEDA_IMAGE
      blurriness = 0


    # given border is split into: grow_border and blur
    grow_border = border * ( 100 - blurriness ) / 100
    blur = border - grow_border;
    safe_border = border+3;
   
    # get and grow selection
    selection = pdb.gimp_selection_save(image)
    pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, layer)
    pdb.gimp_selection_grow(image, grow_border)
    
    # create and place the new layer
    new_layer = pdb.gimp_layer_new(image, layer.width + 2*safe_border, layer.height + 2*safe_border, ltype, layer.name+"_shadow", 100, NORMAL_MODE)
    pdb.gimp_layer_set_offsets(new_layer, layer.offsets[0]-safe_border, layer.offsets[1]-safe_border)
    pos = pdb.gimp_image_get_item_position(image, layer)
    pdb.gimp_image_insert_layer(image, new_layer, None, pos+1)
    
    # fill
    oldcolor = pdb.gimp_context_get_background()
    pdb.gimp_context_set_background(color)
    pdb.gimp_edit_fill(pdb.gimp_image_get_active_layer(image), BACKGROUND_FILL)
    pdb.gimp_context_set_background(oldcolor)
    
    # blur
    if (blurriness > 0):
      pdb.gimp_selection_none(image)
      pdb.plug_in_gauss_rle2(image, pdb.gimp_image_get_active_layer(image), blur, blur)

    
  # cleanup
  finally:
    try:
     pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, selection)
     pdb.gimp_image_remove_channel(image, selection)
     pdb.gimp_image_set_active_layer(image, layer)
    except:
     pass
   
    pdb.gimp_image_undo_group_end(image)



register(
        "outline_simple",
        "Outline Simple",
        "Outline Simple",
        "LatinSuD",
        "MIT License",
        "2018",
        "<Image>/Filters/Decor/Outline Simple",
        "*",
        [
	  (PF_INT, "border", "Border Size (px)", 10),
          (PF_COLOR, "color", "Border Color", (255, 255, 255)),
          (PF_SLIDER, "blurriness", "Blurriness (%)", 0, (0, 100, 1))
	],
        [],
        plugin_main)

main()
