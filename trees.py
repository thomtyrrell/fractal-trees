# set up for complex numbers
import cmath

pi = cmath.pi
e  = cmath.e

# set up for turtle
import turtle


turtle.radians()
turtle.hideturtle()
turtle.tracer(n=0)

#scale controls the length of branches, should be positive and < 1
scale = 1 / 2.0

class Tree():
    
    def __init__(self,root,level,phi,branches):
        self.root = root                #a complex number
        self.level = level              #an integer, self-explanatory
        
        self.rho = 400 * scale ** level
        self.phi = phi                  #an argument, perpendicular to branch
        
        self.branches = branches        #a list of sub-Trees
    
    def grow_tree(self,n,generations):
        if self.branches == [] and generations > 0:
            sub_roots = [self.root + cmath.rect(self.rho,self.phi) * cmath.exp(1j * 2 * pi * (k / (2*n) + 1 / (4*n))) for k in range(n)]
            for new_root in sub_roots:
                self.branches.append(Tree(new_root,self.level+1,cmath.phase(new_root-self.root)-pi/2,[]).grow_tree(n,generations-1))
        return self;
    
    def draw_tree(self,mode):
        for t in self.branches:
            self.draw_branch(t.root,mode)
            t.draw_tree(mode)
            
    def draw_branch(self,next_root,mode):
        if mode == "turtle":
            turtle.penup()
            turtle.goto(self.root.real,self.root.imag)
            turtle.pendown()
            turtle.goto(next_root.real,next_root.imag)        

# example
empty_tree=Tree(0,1,0,[])
test_tree = empty_tree.grow_tree(3,7)
test_tree.draw_tree("turtle")

# draw trunk
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,-400)

# finish up
turtle.update()
turtle.done()
