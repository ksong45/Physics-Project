import pygame,sys,pymunk
import math

def create_ball(space):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = (50,0)
    shape = pymunk.Circle(body,20)
    shape.elasticity = 1
    shape.friction = 0.6
    space.add(body,shape)
    return shape

def draw_ball(ball):
    pos_x = int(ball.body.position.x)
    pos_y = int(ball.body.position.y)
    pygame.draw.circle(screen, (0,0,0), (pos_x,pos_y), 20)

def static_floor(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (0,800)
    shape = pymunk.Poly.create_box(body,(2000,400))
    shape.elasticity = 1
    shape.friction = 0.6
    space.add(body,shape)
    return shape

def draw_floor(floor):
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,600,800,200))

def static_ledge(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (0,300)
    shape = pymunk.Poly.create_box(body,(200,20))
    space.add(body,shape)
    return shape

def draw_ledge(ledge):
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 290, 100, 20))

pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,300)
space.damping = 0.6
ball = create_ball(space)
floor = static_floor(space)
ledge = static_ledge(space)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.body.apply_impulse_at_local_point((200, 0), (10,0))
    
    screen.fill((217,217,217))
    draw_ball(ball)
    draw_floor(floor)
    draw_ledge(ledge)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
