# render via: python3 -m manim <name of File>.py <name of Scene>
# animated gif via: ffmpeg -i media/videos/<name of File>/1080p60/<name of Scene>.mp4 -r 15 media/videos/<name of File>/1080p60/<name of Scene>.gif

from manim import *

class SubMatrixExample1(Scene):
    def construct(self):        
        squares = []
        matrix = []
        colors = [ORANGE, GREEN, BLUE, PURPLE, PINK, TEAL, MAROON, GREY_BROWN, GREY]
        size = 10
        
        # Draw the grid
        for x in range(size):            
            matrix.append([])
            for y in range(size):
                i = x * size + y
                squares.append(Square(0.5))
                squares[i].set_fill(colors[i % len(colors)], opacity=0.5)
                matrix[x].append(squares[i])

        grid = VGroup(*squares)
        grid.arrange_in_grid(size, size, buff=0)
        
        grid.shift(1 * UP)
        #grid.shift(4 * LEFT)
        
        self.play(FadeIn(grid))
        
        self.wait(1)
        
        # Label the axes
        labels = []
        for i in range(size):
            label = Tex(str(i)).scale(0.5)
            label.next_to(squares[i], UP)
            labels.append(label)
            
        for j in range(size):
            label = Tex(str(j)).scale(0.5)
            label.next_to(squares[j * size], LEFT)
            labels.append(label)
            
        labelgroup = VGroup(*labels)
        self.play(FadeIn(labelgroup))

        self.wait(2)
        
        # Subsquares
        subsquaresize = 3
        oldtext = None
        i = 0
        j = 0
        
        overruntext = Tex("Stop the subsquare at the edge!", color=RED)
        overruntext.shift(3 * DOWN)
        isoverrunvisible = False
        
        while j < size: # swap i, j because manim coordinates are col major
            i = 0
            while i < size:
                top = i
                left = j
                bottom = min(i + subsquaresize - 1, size - 1)
                right = min(j + subsquaresize - 1, size - 1)
            
                newtext = Tex("Subsquare from " + str(top) + "," + str(left) + " to " + str(bottom) + "," + str(right))
                newtext.shift(2 * DOWN)
                
                if (bottom < size - 1 and right < size - 1) and isoverrunvisible:
                    self.remove(overruntext)
                    isoverrunvisible = False
                
                if not (oldtext is None):
                    self.play(ReplacementTransform(oldtext, newtext))
                else:
                    self.play(FadeIn(newtext))
                    
                oldtext = newtext
                
                self.wait(1)
                
                indicates = []
                for s in range(left, right + 1): # +1 because range is exclusive
                    for t in range(top, bottom + 1):
                        indicates.append(Indicate(matrix[s][t]))

                if (bottom >= size - 1 or right >= size - 1) and (not isoverrunvisible):
                    self.play(FadeIn(overruntext))
                    isoverrunvisible = True
                    
                if(len(indicates) > 0):                    
                    self.play(*indicates, runtime=2)
                    self.wait(1)
                
                i = i + subsquaresize
                
            j = j + subsquaresize
        
        self.wait(2)

class StringIndexOf(Scene):
    # https://www.geeksforgeeks.org/python-program-convert-string-list/
    def str2list(self, string):
        list1=[]
        list1[:0]=string
        return list1
    
    def draw_array(self, lst, moveunits=0, movedir=DOWN, xbuff=0.8, ybuff=0.5, nullterminator=False):
        if type(lst) is str:
            lst = self.str2list(lst)
        
        if nullterminator:
            lst.append("0")    
            
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
        strtext = Text("x = \"Hello there!\";")
        strtext.shift(1*DOWN)
        self.play(FadeIn(strtext))
        self.wait(1)
        
        str = "Hello there!"
        text, indices = self.draw_array(str, 1, UP, xbuff=0.6, nullterminator=True)
        self.wait(2)
        
        # indexOf code
        text3 = Text("int pos = x.indexOf(\"there\");")
        text3.shift(3*DOWN)
        self.play(FadeIn(text3))

        self.wait(2)
        
        rect = SurroundingRectangle(text[6:11], color=YELLOW, buff=0.15)
        rect2 = SurroundingRectangle(indices[6:11], color=YELLOW, buff=0.15)
        self.play(Create(rect), Create(rect2), runtime=2)
        
        self.play(Indicate(text[6], runtime=0.1), Indicate(indices[6]), runtime=0.1) 
        
        self.wait(1)
        
        self.remove(rect)
        self.remove(rect2)
        
        text4 = Text("6")
        text4.shift(3*DOWN)
        self.play(ReplacementTransform(text3, text4))
        
        self.wait(2)
        
        # indexOf code        
        text5 = Text("int pos = x.indexOf(\'e\');")
        text5.shift(3*DOWN)
        self.play(ReplacementTransform(text4, text5)) 

        self.wait(2)
        
        self.play(Indicate(text[1], runtime=0.1), Indicate(indices[1]), runtime=0.1) 
        
        self.wait(1)
        
        text6 = Text("1")
        text6.shift(3*DOWN)
        self.play(ReplacementTransform(text5, text6)) 

        self.wait(2)        

        # indexOf code        
        text7 = Text("int pos = x.indexOf(\'e\', 2);")
        text7.shift(3*DOWN)
        self.play(ReplacementTransform(text6, text7))   

        self.wait(2)
        
        for i in range(2, 9):
            rect3 = SurroundingRectangle(text[i], color=YELLOW, buff=0.15)
            rect4 = SurroundingRectangle(indices[i], color=YELLOW, buff=0.15)
            self.play(Create(rect3), Create(rect4), runtime=1)
            self.remove(rect3)
            self.remove(rect4)
        
        self.play(Indicate(text[8], runtime=0.1), Indicate(indices[8]), runtime=0.1) 
        
        self.wait(1)
        
        text8 = Text("8")
        text8.shift(3*DOWN)
        self.play(ReplacementTransform(text7, text8))          
        
class Substrings(Scene):
    # https://www.geeksforgeeks.org/python-program-convert-string-list/
    def str2list(self, string):
        list1=[]
        list1[:0]=string
        return list1
    
    def draw_array(self, lst, moveunits=0, movedir=DOWN, xbuff=0.8, ybuff=0.5, nullterminator=False):
        if type(lst) is str:
            lst = self.str2list(lst)
        
        if nullterminator:
            lst.append("0")    
            
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
        text, indices = self.draw_array(str, 1, UP, nullterminator=True)
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
        text4, indices4 = self.draw_array(str, 3, UP, nullterminator=True)
        
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
        text6, indices6 = self.draw_array(str, 1, DOWN, xbuff=0.6, nullterminator=True)
  
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

