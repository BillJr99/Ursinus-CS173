# render via: python3 -m manim <name of File>.py <name of Scene>
# animated gif via: ffmpeg -i media/videos/<name of File>/1080p60/<name of Scene>.mp4 -r 15 media/videos/<name of File>/1080p60/<name of Scene>.gif

from manim import *

class Substrings(Scene):
    def draw_array(self, lst, moveunits=0, movedir=DOWN, xbuff=0.8, ybuff=0.5):
        # https://stackoverflow.com/questions/62409364/is-there-a-better-approach-to-visualize-an-array
        indices = Tex(*[f"[{i}]" for i in range(len(lst))])
        text = Tex(*[f"[{lst[i]}]" for i in range(len(lst))])
        
        text.arrange(RIGHT,buff=xbuff)
        
        for idx, txt in zip(indices, text):
            idx.scale(0.5)
            idx.next_to(txt,DOWN,buff=ybuff)
            
            if moveunits != 0:
                idx.shift(moveunits * movedir)
                txt.shift(moveunits * movedir)            
            
        self.play(*list(map(lambda x: Write(x,run_time=2),[text,indices])))
        
        return text, indices
        
    def construct(self):   
        strtext = Text("x = \"Hamburger\";")
        strtext.shift(1*DOWN)
        self.play(FadeIn(strtext))
        self.wait(1)
        
        str = "Hamburger"
        text, indices = self.draw_array(str, 1, UP)
        self.wait(2)
        
        # substring code
        text2 = Text("x.substring(0, 3);")
        text2.shift(3*DOWN)
        self.play(FadeIn(text2))
        
        rect = SurroundingRectangle(mobject=text[0:3], color=YELLOW, buff=0.15)
        self.play(Create(rect), runtime=2)
        for i in range(3):
            self.play(Indicate(text[i], runtime=0.1), Indicate(indices[i]), runtime=0.1) 
            
        self.play(Indicate(indices[i+1], color=RED), runtime=0.1) 

        self.wait(2)
        
        # substring code
        self.remove(rect)
        text3 = Text("x.substring(3);")
        text3.shift(3*DOWN)
        rect = SurroundingRectangle(mobject=text[3:], color=YELLOW, buff=0.15)
        self.play(ReplacementTransform(text2, text3))
        self.play(Create(rect), runtime=2)
        for i in range(3, 9):
            self.play(Indicate(text[i], runtime=0.1), Indicate(indices[i]), runtime=0.1)        
            
        self.wait(2)
        
        # clean up
        self.remove(rect)
        self.remove(text3)
        self.remove(strtext)
        
        # new string
        str = "Cheese"
        text4, indices4 = self.draw_array(str, 3, UP)
        
        # concatenation
        text5 = Text("\"Cheese\" + x.substring(3);")
        text5.shift(3*DOWN)
        self.play(Write(text5), runtime=3)   
        rect2 = SurroundingRectangle(mobject=text5[0:8], color=YELLOW, buff=0.15)
        self.play(Create(rect2), runtime=2)
        for i in range(6):
            self.play(Indicate(text4[i], runtime=0.1), Indicate(indices4[i]), runtime=0.1) 
        self.remove(rect2)
        rect3 = SurroundingRectangle(mobject=text5[9:], color=YELLOW, buff=0.15)
        self.play(Create(rect3), runtime=2)
        for i in range(3, 9):
            self.play(Indicate(text[i], runtime=0.1), Indicate(indices[i]), runtime=0.1)      
        self.remove(rect3)
        str = "Cheeseburger"
        text6, indices6 = self.draw_array(str, 1, DOWN)
  
        self.wait(2)
        
class ArrayExample1(Scene):
    def construct(self):
        m0 = Matrix([[4, 9, 2, 3, 5, 7, 8, 1, 6]])
        text1 = Text('int[] x = {4, 9, 2, 3, 5, 7, 8, 1, 6};').scale(1)
        text2 = Text('x[col]').scale(1)
        
        self.add(text1)
        self.wait(2)
        self.play(ApplyMethod(text1.shift, 3*DOWN))
        self.play(FadeIn(m0))   

        self.wait(2)
        text2.shift(2*DOWN)
        self.play(FadeIn(text2))
        
        self.wait(2) 

        oldtext = text2
        for i in range(9):                
            newtext = Text('x[' + str(i) + ']').scale(1)
            newtext.shift(2*DOWN)           
            
            self.play(ReplacementTransform(oldtext, newtext))

            self.play(Indicate(m0.get_entries()[i]))
                        
            oldtext = newtext

class MatrixExample1(Scene):
    def construct(self):
        m0 = Matrix([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
        text1 = Text('int[][] x = {{4, 9, 2}, {3, 5, 7}, {8, 1, 6}};').scale(1)
        text2 = Text('x[row][col]').scale(1)
        
        self.add(text1)
        self.wait(2)
        self.play(ApplyMethod(text1.shift, 3*DOWN))
        self.play(FadeIn(m0))
        
        self.wait(2)
        text2.shift(2*DOWN)
        self.play(FadeIn(text2))
        
        self.wait(2)
        
        oldtext = text2
        k = 0
        for i in range(3):
            for j in range(3):                                    
                newtext = Text('x[' + str(i) + '][' + str(j) + ']').scale(1)
                newtext.shift(2*DOWN)

                self.play(ReplacementTransform(oldtext, newtext))                                        
                self.play(Indicate(m0.get_entries()[k]))
                                
                oldtext = newtext
                
                k = k + 1

