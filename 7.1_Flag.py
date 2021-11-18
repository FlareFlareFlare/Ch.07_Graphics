'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
import arcade
y = 260
x = y*1.9
stripe = .0769*y
v = y/26
m = y/6.5
c = y*.5385
d = y*.76
e = y*.054
g = y*.063
f = y*.054
k = y*.0616
arcade.open_window(x, y, "The Stars and Stripes", True)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range(int(v), y, int(m)):
    arcade.draw_line(0,i,x,i, (191,10,48), stripe)
#red strip
arcade.draw_lrtb_rectangle_filled(0, d, y, c, (0,40,104))
#blue rectangle
for i in range(int(c), int(y), int(f+8)):
    arcade.draw_text("*", d-k/.75, i, (260,260,260), 16)

for i in range(int(c), int(y), int(f+8)):
    arcade.draw_text("*", d-k*3.5, i, (260,260,260), 16)

for i in range(int(c), int(y), int(f+8)):
    arcade.draw_text("*", d-k*5.5, i, (260,260,260), 16)

for i in range(int(c), int(y), int(f + 8)):
    arcade.draw_text("*", d - k*7.5, i, (260, 260, 260), 16)

for i in range(int(c), int(y), int(f+8)):
    arcade.draw_text("*", d-k*9.5, i, (260,260,260), 16)

for i in range(int(c), int(y), int(f+8)):
    arcade.draw_text("*", d-k*11.5, i, (260,260,260), 16)
#stars first six stripes
for i in range(int(c+e), int(y-e*2), int(e*1.5)):
    arcade.draw_text("*", d-k*2.5, i, arcade.color.WHITE, 16)

for i in range(int(c+e), int(y-e*2), int(e*1.5)):
    arcade.draw_text("*", d-k*4.5, i, arcade.color.WHITE, 16)

for i in range(int(c+e), int(y-e*2), int(e*1.5)):
    arcade.draw_text("*", d-k*6.5, i, arcade.color.WHITE, 16)

for i in range(int(c+e), int(y-e*2), int(e*1.5)):
    arcade.draw_text("*", d-k*8.5, i, arcade.color.WHITE, 16)

for i in range(int(c+e), int(y-e*2), int(e*1.5)):
    arcade.draw_text("*", d-k*10.5, i, arcade.color.WHITE, 16)
arcade.finish_render()
arcade.run()