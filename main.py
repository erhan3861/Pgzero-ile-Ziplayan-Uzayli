import random

# Ekran boyutları
WIDTH = 800
HEIGHT = 600

# Alien'in özellikleri
alien = Actor("alien")
alien.pos = WIDTH // 2, HEIGHT // 2
velocity_x = 0 # Yatay hız
velocity_y = 0  # Dikey hız
gravity = 0.5  # Yerçekimi
bounce_strength = -20 # Zıplama gücü
shoot = True

# Çarpma kontrolü
def check_ground_collision():
    global velocity_x, velocity_y, bounce_strength

    if alien.bottom >= HEIGHT:
        alien.bottom = HEIGHT
        bounce_strength += 2
        velocity_y = bounce_strength
        velocity_x = random.uniform(-3,3)


# Oyunun çerçevesini güncelleme

def update():
    global velocity_y

    # zıplamanın bitmesi
    if bounce_strength > 0:
        return

    # Yerçekimi etkisi
    velocity_y += gravity
    alien.y += velocity_y
    alien.x += velocity_x

    if alien.y <= 0:
        alien.y = 0
        velocity_y *= -1

    # sağ -sol kenar algılama
    if alien.left < 0: alien.left = 0
    elif alien.right > WIDTH: alien.right = WIDTH

    # Yere çarpma kontrolü
    check_ground_collision()


def draw():
    screen.clear()
    screen.fill((135, 206, 250))  # Gökyüzü mavisi arka plan
    screen.draw.line((0,0), alien.pos, "yellow")
    screen.draw.line((WIDTH,0), alien.pos, "yellow")
    alien.draw()

def on_mouse_down(pos, button):
    global velocity_x, velocity_y, gravity, shoot, bounce_strength

    if alien.collidepoint(pos) and shoot:

        bounce_strength = -20

        velocity_y = bounce_strength

        if alien.x < 400:
            velocity_x = random.uniform(0,alien.x/50)
        else:
            velocity_x = random.uniform(-alien.x/50, 0)

        gravity = 0.5

        shoot = False
        clock.schedule(shoot_on, 3)


def on_mouse_move(pos):
    global velocity_x, velocity_y, gravity

    if shoot:
        velocity_x = 0
        velocity_y = 0
        gravity = 0
        alien.pos = pos

def shoot_on():
    global shoot
    shoot = True



