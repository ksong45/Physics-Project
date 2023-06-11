import pygame,sys,pymunk
import math

def create_ball(space):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = (71.12,0)
    shape = pymunk.Circle(body,12)
    shape.elasticity = 0.87
    space.add(body,shape)
    return shape

def draw_ball(ball):
    pos_x = int(ball.body.position.x)
    pos_y = int(ball.body.position.y)
    pygame.draw.circle(screen, (0,0,0), (pos_x,pos_y), 12)

def static_floor(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (400,800)
    shape = pymunk.Poly.create_box(body,(800,200))
    shape.elasticity = 0.87
    space.add(body,shape)
    return shape

def draw_floor(floor):
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,700,800,100))

def static_ledge(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (0,405.2)
    shape = pymunk.Poly.create_box(body,(243.84,20))
    space.add(body,shape)
    return shape

def draw_ledge(ledge):
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 395.2, 121.92, 20))

pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,500)
space.damping = 0.85
ball = create_ball(space)
floor = static_floor(space)
ledge = static_ledge(space)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.body.apply_impulse_at_local_point((180, 0), (10,0))
    
    screen.fill((217,217,217))
    draw_ball(ball)
    draw_floor(floor)
    draw_ledge(ledge)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
