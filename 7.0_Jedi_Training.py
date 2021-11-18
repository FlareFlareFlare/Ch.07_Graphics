#Sign your name:Matthew Flyr

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLUE, BRICK_RED.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
GraphW = 500
GraphH = 400
arcade.open_window(GraphW, GraphH, "Ch. 7 Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
for i in range(0, GraphW+1, 20):
    arcade.draw_line(i, 0, i, GraphH, (0, 0, 0))
    #x lines on graph
for o in range(0, GraphH+1, 20):
    arcade.draw_line(0, o, GraphW, o, (0, 0, 0))
    #y lines on graph
arcade.draw_circle_filled(GraphW-40, GraphH-390, 3, arcade.color.RED)
#red dot
arcade.draw_circle_filled(GraphW/2, GraphH/2, 40, arcade.color.WISTERIA)
#purple circle
arcade.draw_lrtb_rectangle_filled(GraphW-480, GraphW-420, GraphH-20, GraphH-40, arcade.color.PHLOX)
#purple square
arcade.draw_arc_filled(GraphW-100, GraphH-80, 110, 120,
arcade.color.YELLOW, 30, 330)
#pac man
arcade.draw_rectangle_filled(GraphW/2-50,GraphH/2+60,40,20,arcade.color.BLUSH, -45)
#tilted rectangle
arcade.draw_ellipse_filled(GraphW-GraphW+100, GraphH-300, 120, 40, arcade.color.AMBER)
#eclispe my g
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
#lineeeee
arcade.draw_text("I love you. I know.", 20, 175, arcade.color.BRICK_RED, 19, 0, "left", "Ariel", True)
#the text
arcade.finish_render()
arcade.run()
