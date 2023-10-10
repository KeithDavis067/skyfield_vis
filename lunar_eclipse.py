from manim import *

class moon_shadow(Scene):
    def construct(self):

        sun = VGroup(Circle(radius = 2, color = YELLOW_B, fill_opacity = 0.7)).shift(3.5*LEFT)
        earth = Circle(radius=1, color= GREEN, fill_opacity = 0.7).shift(2.5*RIGHT)
        moon = Circle(radius=0.3, color = YELLOW_A, fill_opacity = 0.7).shift(4*RIGHT)

        #labels

        sun_text = Text('Sun', font_size=24).shift(3.5*LEFT)
        earth_text = Text('Earth', font_size=20).shift(2.5*RIGHT)
        moon_text = Text('Moon', font_size=20).shift(4*RIGHT)

        day_text = Text('Day', font_size=20).shift(2*RIGHT)
        night_text = Text('Night', font_size=20).shift(3*RIGHT)
        

        s_coor = sun.get_center()
        e_coor = earth.get_center()
        s_top = s_coor+[0,2, 0]
        s_bottom = s_coor-[0,2, 0]
        e_top = e_coor+[0,1, 0]
        e_bottom = e_coor-[0,1, 0]

        #lines connecting
        cline1 = Line(start=s_coor+[2, 0, 0], end = e_coor-[1,0, 0])
        cline2 = Line(start=e_coor+[1, 0, 0], end = moon.get_center()-[0.3,0, 0])

        #sun to earth lines
        se_line_tt = DashedLine(start=s_top, end = e_top)
        se_line_tb = DashedLine(start=s_top, end = e_bottom)
        se_line_bt = DashedLine(start=s_bottom, end = e_top)
        se_line_bb = DashedLine(start=s_bottom, end = e_bottom)

        slope_se_tt = (s_coor - e_coor)[1]/(s_coor - e_coor)[0]
        slope_se_bt = (s_bottom - e_top)[1]/(s_bottom - e_top)[0]

        #arrows
        se_arrow_tt = Arrow(start=s_top, end = e_top)
        se_arrow_tb = Arrow(start=s_top, end = e_bottom)
        se_arrow_bt = Arrow(start=s_bottom, end = e_top)
        se_arrow_bb = Arrow(start=s_bottom, end = e_bottom)



        #solid lines

        light_line_tt = Line(start = e_top, end = [e_top[0]+4, (e_top[0]+4)*slope_se_tt, 0])
        light_line_tb = Line(start = e_bottom, end = [e_bottom[0]+4, (e_bottom[0]+4)*-slope_se_bt, 0])
        light_line_bt = Line(start = e_top, end = [e_top[0]+4, (e_top[0]+4)*slope_se_bt, 0])
        light_line_bb = Line(start = e_bottom, end = [e_bottom[0]+4, (e_bottom[0]+4)*slope_se_tt, 0])
        
        day_to_night = Line(e_coor+[0, 1, 0], e_coor-[0, 1, 0])

        umbra = Polygon(e_top, e_bottom, [e_top[0]+4, (e_top[0]+4)*slope_se_tt, 0], fill_opacity = 0.3, color = RED)
        umbra_text =  Text('Umbra', font_size=24).shift([1, -3.5, 0])
        umbra_arrow = Arrow(umbra_text.get_center(), moon.get_center()+[1, 0, 0])

        preumbra = VGroup(Polygon(e_top, [e_top[0]+4, (e_top[0]+4)*slope_se_bt, 0], [e_top[0]+4, (e_top[0]+4)*slope_se_tt, 0], fill_opacity = 0.3, color = GREEN),
                          Polygon(e_bottom, [e_bottom[0]+4, (e_bottom[0]+4)*-slope_se_bt, 0], [e_top[0]+4, (e_top[0]+4)*slope_se_tt, 0], fill_opacity = 0.3, color = GREEN)
                        )
        preumbra_text =  Text('Preumbra', font_size=24).shift([1, -3.5, 0])
        preumbra_arrow = VGroup(Arrow(umbra_text.get_center(), moon.get_center()+[1, 2, 0]),
                                Arrow(umbra_text.get_center(), moon.get_center()+[1, -2, 0])
                                )
                          


        self.play(Create(VGroup(sun, earth, moon), run_time = 2))
        self.play(AnimationGroup(FadeIn(sun_text, earth_text, moon_text.shift(DOWN*0.5))))
        self.play(Create(VGroup(cline1, cline2)))

        self.play(Create(se_line_tb), Create(se_line_tt), run_time = 2)
        self.play(Create(se_line_bb), Create(se_line_bt), run_time = 2)

        self.play(Create(se_arrow_tb), Create(se_arrow_tt), run_time = 2)
        self.play(Create(se_arrow_bb), Create(se_arrow_bt), run_time = 2)

        self.play(Create(day_to_night))

        self.play(AnimationGroup(FadeOut(earth_text)))

        self.play(AnimationGroup(FadeIn(day_text, night_text)))

        self.play(Create(light_line_tt), Create(light_line_bb),Create(light_line_bt), Create(light_line_tb))

        self.play(AnimationGroup(FadeIn(umbra, umbra_text, umbra_arrow)))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(umbra, umbra_text, umbra_arrow)))
        self.play(AnimationGroup(FadeIn(preumbra, preumbra_text, preumbra_arrow)))
        self.wait(5)

