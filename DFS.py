
import random
import pygame
class cell:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.visited=False
        # true means there is wall
        self.walls= { "Top":True, "Bottom":True, "Left":True, "Right":True} 
# i am defining a class for cell , it is initialized later

def maizeGenerator(height , width):
    grid=[]

    for x in range(width):
        column=[]
        for y in range(height):
            column.append(cell(x,y))
        # appending object
        grid.append(column)    

     #columns are attached to grids
     # .  .
     # .  . 
     # .  .


    direction=[
        (0,-1, "Top", "Bottom"),
        (0,1, "Bottom", "Top"),
        (-1, 0, "Left", "Right"),
        (1,0,"Right", "Left")
    ]

     # this is for direction, we use  two label because wall can be relative to two cells


   #this  gets unvisted neighbours only
    def unvisitedNeighbour(cell):
        x=cell.x
        y=cell.y
        neighbour=[]
        for dx, dy, wall, oppositeWall in direction:
                nx=x+dx
                ny=y+dy

                if 0<=nx<width and 0<=ny<height :
                    #checking for boundary
                    if(grid[nx][ny].visited==False):
                         neighbour.append((grid[nx][ny],wall,oppositeWall))


        return neighbour


    stack=[]
    
    starting =grid[0][0]
    starting.visited=True
    stack.append(starting)
    
    
    while stack:
            current=stack[-1]
            unvisited_neighbours=unvisitedNeighbour(current) 
            if unvisited_neighbours:
                #check if we have neighbours
                next_cell,wall, oppositeWall=random.choice(unvisited_neighbours) 
                current.walls[wall]=False
                next_cell.walls[oppositeWall] =False 
                # there is no wall now
                next_cell.visited=True
                stack.append(next_cell)

            else:
                 stack.pop()    

    return grid

def DFS_MaizeSolver(grid, height, width):
      Start=grid[0][0];    # start from 0,0 
      End=grid[width-1][height-1] # end at last

      Stack=[[Start]]
      Visited={Start}    


      while Stack:    # until stack is empty
        path=Stack.pop()    # we pop a path not a grid , each time a grid is added new path is created
        current=path[-1]    # pop a frid from last path's last grid

        if(current==End):  # stopping condition
             return path

        x=current.x
        y=current.y

        direction=[
              (0,-1, "Top"),
              (0,1, "Bottom"),
              (-1, 0, "Left"),
              (1,0,"Right")
          ]

        for dx, dy, direc in direction:# check in all direction up down left right
            if current.walls[direc]==False:  #if there is no wall, or there is path 
                nx=x+dx
                ny=y+dy

                if 0<=nx<width and 0<=ny<height:    # checking boundary
               
                     neighbour=grid[nx][ny]
                     if neighbour not in Visited:
                        Visited.add(neighbour)
                        # added a neighbour to visited

                        # now we need to add path to stack
                        new_path=path.copy()  # make a list from existing list  
                        new_path.append(neighbour) # now we add that neighbour   
                        Stack.append(new_path)


      return []
      
      



"""def main():
    width, height = 5, 5
    grid = maizeGenerator(height, width)
    
    output="+"+"---+"*width + "\n"

    for y in range(height):
         row="|"
         bottom="+"
         

         for x in range(width):
              c=grid[x][y]
              if c.walls["Right"]:
                   row+="   |"
              else :
                   row+="    "  

              if c.walls["Bottom"]:
                   bottom+="---+"
              else:
                   bottom+="   +"             
         output+=row+"\n" +bottom + "\n"
    print(output)


    path_from_start_to_end=DFS_MaizeSolver(grid,  height, width)
    print("start", end="->")
    for step in path_from_start_to_end:
         print(f"{step.x},{step.y}", end="-->")
    print("end")     


if __name__ == "__main__":
    main()"""


def main():
    width, height = 25,25 # You can make it much bigger now!
    cell_size = 30
    
    # Initialize Pygame window
    pygame.init()
    screen_width = width * cell_size
    screen_height = height * cell_size
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Backtracking Maze Generator & DFS Solver")

    # Generate maze and solve it
    grid = maizeGenerator(height, width)
    path = DFS_MaizeSolver(grid, height, width)
    path_set = set(path)

    # Main Pygame loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255)) # White background

        # Draw cells and walls
        for x in range(width):
            for y in range(height):
                c = grid[x][y]
                px = x * cell_size
                py = y * cell_size

                # Highlight solution path cells in light blue
                if c in path_set:
                    pygame.draw.rect(screen, (173, 216, 230), (px, py, cell_size, cell_size))

                # Draw walls as black lines
                if c.walls["Top"]:
                    pygame.draw.line(screen, (0, 0, 0), (px, py), (px + cell_size, py), 2)
                if c.walls["Left"]:
                    pygame.draw.line(screen, (0, 0, 0), (px, py), (px, py + cell_size), 2)
                if c.walls["Right"]:
                    pygame.draw.line(screen, (0, 0, 0), (px + cell_size, py), (px + cell_size, py + cell_size), 2)
                if c.walls["Bottom"]:
                    pygame.draw.line(screen, (0, 0, 0), (px, py + cell_size), (px + cell_size, py + cell_size), 2)

        pygame.display.flip()

if __name__ == "__main__":
    main()