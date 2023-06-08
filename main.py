import pygame,sys,pymunk

def create_ball(space):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = (50,0)
    shape = pymunk.Circle(body,20)
    space.add(body,shape)
    return shape

def draw_ball(ball):
    pos_x = int(ball.body.position.x)
    pos_y = int(ball.body.position.y)
    pygame.draw.circle(screen, (0,0,0), (pos_x,pos_y), 20)

def static_ramp(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (20,500)
    shape = pymunk.Circle(body, 50)
    space.add(body,shape)
    return shape

def draw_ramp(ramp):
    pos_x = int(ramp.body.position.x)
    pos_y = int(ramp.body.position.y)
    pygame.draw.circle(screen, (0,0,0), (pos_x,pos_y), 50)

def static_floor(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (0,800)
    shape = pymunk.Poly.create_box(body,(2000,400))
    space.add(body,shape)
    return shape

def draw_floor(floor):
    pos_x = int(floor.body.position.x)
    pos_y = int(floor.body.position.y)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,600,800,200))

pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,300)
ball = create_ball(space)
ramp = static_ramp(space)
floor = static_floor(space)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((217,217,217))
    draw_ball(ball)
    draw_ramp(ramp)
    draw_floor(floor)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)