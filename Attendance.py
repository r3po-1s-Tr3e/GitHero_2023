import pygame
import random
import math
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Terminal Emulator")

# Set up fonts
font = pygame.font.SysFont("Consolas", 20)
input_font = pygame.font.SysFont("Consolas", 30)

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

# Set up variables
password = ""
students = [("John", 1234,"123.4.5.6"), ("Emily", 5678,"123.4.5.6"), ("Mike", 9012,"123.4.5.6"), ("Sara", 3456,"123.4.5.6"), ("David", 7890,"123.4.5.6"),
            ("Anna", 2345,"123.4.5.6"), ("Tom", 6789,"123.4.5.6"), ("Julia", 123,"123.4.5.6"), ("Peter", 4567,"123.4.5.6"), ("Mary", 8901,"123.4.5.6"),
            ("Jake", 5432,"123.4.5.6"), ("Olivia", 9876,"123.4.5.6"), ("Nick", 3210,"123.4.5.6"), ("Eva", 7654,"123.4.5.6"), ("Sam", 1098,"123.4.5.6")]
student_texts = [font.render(f"{i+1}. {name}/{id}: {ip}", True, white) for i, (name, id,ip) in enumerate(students)]
is_logged_in = False
radius_1 = 100
radius_2 = 100
distance = 400
angle_x = 20
angle_y = 20


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
hue = 0

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 800
FPS = 60

pixel_width = 20
pixel_height = 20

x_pixel = 0
y_pixel = 0






# Set up cursor timer
cursor_timer = 0

# Set up cursor visible flag
cursor_visible = True
list_typed = False
count=0
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isprintable() and not is_logged_in:
                password += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                password = password[:-1]
            elif event.key == pygame.K_RETURN:
                if password == "pass@123":
                    is_logged_in = True
                else:
                    is_logged_in= False
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Fill the screen with black
    screen.fill((0, 0 ,0))

    # Draw the terminal window
    pygame.draw.rect(screen, white, (50, 50, screen_width - 100, screen_height - 100), 2)

    # Draw the password prompt
    password_text = font.render("Password:", True, white)
    screen.blit(password_text, (70, 70))
    pygame.draw.rect(screen, gray, (200, 70, 500, 40), 2)

    # Calculate sin and cos values for rotation
    sin_x = math.sin(angle_x)
    cos_x = math.cos(angle_x)
    sin_y = math.sin(angle_y)
    cos_y = math.cos(angle_y)

    # Draw the donut
    for theta in range(0, 360, 10):
        for phi in range(0, 360, 10):
            # Calculate sin and cos values for the current theta and phi
            sin_theta = math.sin(theta * math.pi / 180)
            cos_theta = math.cos(theta * math.pi / 180)
            sin_phi = math.sin(phi * math.pi / 180)
            cos_phi = math.cos(phi * math.pi / 180)

            # Calculate the x, y, and z coordinates of the point on the donut
            x = distance + (radius_1 + radius_2 * cos_theta) * cos_phi
            y = (radius_1 + radius_2 * cos_theta) * sin_phi
            z = -radius_2 * sin_theta

            # Apply rotation to the coordinates
            x_rot = x * cos_y - z * sin_y
            z_rot = z * cos_y + x * sin_y
            y_rot = y * cos_x - z_rot * sin_x
            z_rot = z_rot * cos_x + y * sin_x

            # Project the 3D point onto the 2D screen
            scale = distance / (distance - z_rot)
            x_proj = int(screen_width / 2 + x_rot * scale)
            y_proj = int(screen_height / 2 - y_rot * scale)

            # Draw the point on the screen
            pygame.draw.circle(screen, (0,0,255), (x_proj, y_proj), 2)

    # Update the rotation angles
    angle_x += 0.01
    angle_y += 0.01


    # Update cursor visibility
    if pygame.time.get_ticks() - cursor_timer > 500:
        cursor_visible = not cursor_visible
        cursor_timer = pygame.time.get_ticks()

    # Draw password input text
    if not is_logged_in:
        input_text = input_font.render(password + ("|" if cursor_visible else ""), True, white)
    else:
        input_text = input_font.render("Logged In Successfully", True, white)
    screen.blit(input_text, (205, 75))

    # Draw the student list if logged in
    
    if is_logged_in and not list_typed:
        student_list = font.render("Student List:", True, white)
        screen.blit(student_list, (70, 120))
        for i, student_text in enumerate(student_texts):
            screen.blit(student_text, (70, 150 + i * 25))
            count+=1
            pygame.time.wait(200)
            pygame.display.update()
            if(count==15):
                list_typed=True
    
    if(list_typed==True):
        pygame.time.wait(10000)
        running=False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
