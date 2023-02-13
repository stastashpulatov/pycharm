import simple_draw as sd

y = 500
while True:
    sd.clear_screen()
    point_0 = sd.get_point(300, 300)
    sd.snowflake(center=point_0, length=100)
    y -= 50
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
