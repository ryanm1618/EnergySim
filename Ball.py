import pygame

class Ball:
    ball_count = 0;
    def __init__(self, x, y, radius, energy_level, velocity, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.energy_level = energy_level
        self.x_velocity = velocity.xvel;
        self.y_velocity = velocity.yvel;
        self.color = color
        Ball.ball_count += 1

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def check_collision(self, other_ball):
        #Calculate distance between two points sqrt((x2 - x1)^2 + (y2 - y1)^2)
        x_dif_squared = math.pow(other_ball.x - self.x)
        y_dif_squared = math.pow(other_ball.y - self.y)
        
        #Calculate the actual distance between the two points
        distance = math.sqrt(x_dif_squared + y_dif_squared)
        #Calculate the distance needed for a collision
        collision_distance = self.radius + other.radius

        if(distance <= collision_distance):
            self.x -= other.radius
            self.x_velocity *= -1
            self.y_velocity *= -1
