'''
PYCASSO PROJECT
---------------
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
When you are finished Pull Request your file to your instructor.
'''
import arcade
GraphX = 500
GraphY = 500
arcade.open_window(GraphX, GraphY, "Matthew Flyr", True)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_line(0,0,150,0,arcade.color.SILVER,25)
arcade.draw_line(350,0,500,0,arcade.color.SILVER,25)
arcade.draw_line(150,0,150,450,arcade.color.SILVER,35)
arcade.draw_line(150,450,350,450,arcade.color.SILVER,35)
arcade.draw_line(350,450,350,0,arcade.color.SILVER,35)
#draws base shape of elevator

arcade.draw_lrtb_rectangle_filled(160,250,432,0,arcade.color.OLD_SILVER)
arcade.draw_lrtb_rectangle_filled(250,340,432,0,arcade.color.OLD_SILVER)
#doors

arcade.draw_line(250,0,250,432,arcade.color.BLACK)
#door line

for i in range(10, GraphY-50, 50):
    arcade.draw_circle_filled(145, i, 10, arcade.color.WHITE)
for i in range(10, 450,50):
    arcade.draw_circle_filled(355, i, 10, arcade.color.WHITE)
#circles on sides

arcade.draw_arc_filled(150, 450, 35, 35, arcade.color.SILVER, 45, 345)
arcade.draw_arc_filled(350, 450, 35, 35, arcade.color.SILVER, 1, 200)
#arcs that make the corners

arcade.draw_text("The Elevator of Destiny", 160,432,arcade.color.BLACK,14,0,"left", "Times New Roman")
arcade.finish_render()
arcade.run()


