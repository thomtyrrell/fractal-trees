# set up for complex numbers
import cmath

pi = cmath.pi
e  = cmath.e

# set up for turtle
import turtle

turtle.radians()
turtle.hideturtle()
turtle.tracer(n=0)

# tree will be height of screen
height = turtle.window_height()

# draw trunk, half of screen
turtle.pensize(5)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,-height/2)

class Tree():
    
    def __init__(self,root,level,phi,branches):
        self.root = root                            #a complex number
        self.level = level                          #an integer, self-explanatory, controls length and width of branches
        
        self.length = height / 2 * 2 ** (-level)    #controls length of branch
        self.width = 5 / (level + 1)                #controls width of branch
        self.phi = phi                              #an argument, controls angle of branches between levels
        
        self.branches = branches                    #a list of sub-Trees
    
    def grow_tree(self,n,generations):
        if self.branches == [] and generations > 0:
            sub_roots = [self.root + cmath.rect(self.length,self.phi) * cmath.exp(1j * 2 * pi * (k / (2*n) + 1 / (4*n))) for k in range(n)]
            for new_root in sub_roots:
                self.branches.append(Tree(new_root,self.level+1,cmath.phase(new_root-self.root)-pi/2,[]).grow_tree(n,generations-1))
        return self;
    
    def draw_tree(self,mode):
        for t in self.branches:
            self.draw_branch(t.root,mode)
            t.draw_tree(mode)
            
    def draw_branch(self,next_root,mode):
        if mode == "turtle":
            turtle.pensize(self.width)
            turtle.penup()
            turtle.goto(self.root.real,self.root.imag)
            turtle.pendown()
            turtle.goto(next_root.real,next_root.imag)        

# example
empty_tree=Tree(0,1,0,[])
test_tree = empty_tree.grow_tree(4,6)
test_tree.draw_tree("turtle")

# finish up
turtle.update()
turtle.done()
