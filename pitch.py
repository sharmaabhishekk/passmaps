import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import math

def Pitch(ax, height = 120,  width=80, line_color = "black", pitch_color = "white", mode = "full", pitch_linewidth = 1):

    def int_angles(radius, h, k, line_x):
        """
        Calculate the intersection angles of the arc above the D-boxes
        
        Parameters: 
            radius (float): Radius of the arc
            h(float): x coordinate of the centre of the arc
            k(float): y coordiante of the centre of the arc
            line_x(float): x coordinate of the D-box or the line to be intersected by the arc
      
        Returns: 
            theta1(float): First intersection angle
            theta2(float): Second intersection angle
        """
        y1 = math.sqrt(radius**2 - (line_x - h)**2) + k
        y2 = math.sqrt(radius**2 - (line_x - h)**2)*-1 + k
        y = (y1-y2)/2
        theta1 = math.degrees(math.asin(y/radius))
        theta2 = 360-theta1

        return theta1, theta2

    
    #Pitch Outline
    ax.plot([0,0],[0,width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([0,height],[width,width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([height,height],[width,0], color=line_color, linewidth = pitch_linewidth)
    ax.plot([height,0],[0,0], color=line_color, linewidth = pitch_linewidth)

    
    ##Halfway-line
    ax.plot([height/2, height/2],[0,width], color=line_color, linewidth = pitch_linewidth)

    #Left Penalty Area
    ax.plot([0,.15*height],[.225*width, .225*width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([.15*height, .15*height],[.225*width,0.775*width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([.15*height,0],[.775*width, .775*width], color=line_color, linewidth = pitch_linewidth)

    #Right Penalty Area
    ax.plot([.85*height,height],[.15*height, .15*height], color=line_color, linewidth = pitch_linewidth)
    ax.plot([.85*height,.85*height],[.15*height, .775*width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([.85*height,height],[.775*width, .775*width], color=line_color, linewidth = pitch_linewidth)
    
    #6-yard box left
    ax.plot([0,.05*height],[.375*width, .375*width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([.05*height, .05*height],[.375*width,width - .375*width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([0,.05*height],[.625*width, .625*width ], color=line_color, linewidth = pitch_linewidth)    

    #6-yard box right
    ax.plot([.95*height,height],[.375*width, .375*width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([.95*height,114],[.375*width, .625*width], color=line_color, linewidth = pitch_linewidth)
    ax.plot([.95*height,height],[.625*width, .625*width], color=line_color, linewidth = pitch_linewidth)

      
        #Prepare Circles
    centreCircle = plt.Circle((height/2, width/2),.076*height,color=line_color,fill=False, zorder=5)
    centreSpot = plt.Circle((height/2, width/2),0.8,color=line_color)
    leftPenSpot = plt.Circle((.1*height,40),0.8,color=line_color)
    rightPenSpot = plt.Circle((.9*height,40),0.8,color=line_color)

                
        #Prepare Arcs
    theta1, theta2 = int_angles(radius = height/12,
                                h = .1*height,
                                k= width/2,
                                line_x = .15*height)

    
    leftArc = Arc((.1*height,40),
                              height=0.15*height,
                              width=0.15*height,
                              angle=0,
                              theta1=theta2,
                              theta2=theta1,
                              color=line_color,
                              zorder=5)
    
    theta1, theta2 = int_angles(radius = height/12,
                                h = .9*height,
                                k= width/2,
                                line_x = .85*height)
    
    rightArc = Arc((.9*height,40),
                               height=0.15*height,
                               width=0.15*height,
                               angle=180,
                               theta1=theta2,
                               theta2=theta1,
                               color=line_color,
                               zorder=5)

        ##Add corner arcs
    left_bottom = Arc((0,0),
                  height=.05*height,
                  width=0.05*height,
                  angle=270,
                  theta1=90,
                  theta2=180,
                  color=line_color,
                  zorder=5)

    left_top = Arc((0,width),
                  height=.05*height,
                  width=0.05*height,
                  angle=0,
                  theta1=270,
                  theta2=0,
                  color=line_color,
                   zorder=5)

    right_bottom = Arc((height, 0),
                  height=.05*height,
                  width=0.05*height,
                  angle=0,
                  theta1=90,
                  theta2=180,
                  color=line_color,
                   zorder=5    )
    
    right_top = Arc((height, width),
                  height=.05*height,
                  width=0.05*height,
                  angle=90,
                  theta1=90,
                  theta2=180,
                  color=line_color,
                   zorder=5 )    

    
        #Goals
    ax.plot([0,0],[.45*width, .55*width],color=line_color, linewidth = pitch_linewidth*4)
    ax.plot([height, height],[.45*width, .55*width],color=line_color, linewidth = pitch_linewidth*4)

        #Add patches
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    if mode == "full":
        ax.add_patch(left_bottom)
        ax.add_patch(left_top)
        ax.add_patch(right_bottom)
        ax.add_patch(right_top)

    ax.set_aspect("equal")
    ax.axis("off")

    return ax

