
# Asteroids Game Project

## Overview
The **Asteroids** project is a simple game developed using Python and the Pygame library. It is inspired by the classic arcade game "Asteroids," and serves as a practice project for Object-Oriented Programming (OOP) concepts. 
This project showcases the use of inheritance, encapsulation, and polymorphism through the creation of different game objects such as asteroids, the player character, bullets, and an asteroid field manager.


## OOP Concepts Demonstrated
- **Encapsulation:** All game objects have their own properties and behaviors encapsulated within their respective classes.
- **Inheritance:** The `Asteroid` and `Player` classes inherit from the `CircleShape` base class.
- **Polymorphism:** The `draw` and `update` methods are overridden in subclasses to provide specific implementations.

## Features
- **Asteroid Splitting:** When larger asteroids are hit, they split into smaller asteroids.
- **Collision Detection:** The game detects collisions between the player, asteroids, and bullets.
- **Randomized Asteroid Spawn:** Asteroids spawn from the edges of the screen with random velocity and direction.
- **Smooth Player Controls:** The player can move and shoot to avoid or destroy asteroids.



## Project Structure
```
├── asteroid.py         # Asteroid class implementation
├── asteroidfield.py    # Manages the spawning of asteroids
├── bullets.py          # Bullet (Shot) class implementation
├── circleshape.py      # Base class for circular objects
├── constants.py        # Game constants (screen size, asteroid sizes, etc.)
├── main.py             # Main game loop and initialization
├── player.py           # Player class implementation
```

## Key Classes
### `Asteroid`
The `Asteroid` class represents individual asteroids. It inherits from the `CircleShape` class and includes methods for drawing, updating position, and splitting into smaller asteroids upon collision.

**Methods:**
- `draw(screen)`: Draws the asteroid on the screen.
- `update(dt)`: Updates the asteroid's position based on its velocity.
- `split()`: Splits the asteroid into two smaller ones if its radius is larger than the minimum allowed size.

### `AsteroidField`
The `AsteroidField` class manages the spawning of asteroids at random positions along the screen edges. It uses the Pygame sprite system to keep track of all asteroids.

**Methods:**
- `spawn(radius, position, velocity)`: Spawns a new asteroid with the given parameters.
- `update(dt)`: Handles the timer and logic for spawning new asteroids.

### `CircleShape`
The `CircleShape` class is a base class for circular game objects such as asteroids and bullets. It provides basic properties like position, velocity, and radius.

**Methods:**
- `draw(screen)`: Abstract method to be overridden by subclasses.
- `update(dt)`: Abstract method to be overridden by subclasses.
- `collision(object)`: Checks if the current object collides with another circular object.

### `Player`
The `Player` class represents the player's spaceship. It handles `movement`, `shooting`, and `collision` detection with asteroids.



## How to Run the Game
1. Make sure you have Python installed.
2. Install the Pygame library:
   ```
   pip install pygame
   ```
3. Run the game by executing the `main.py` file:
   ```
   python main.py
   ```


## Future Improvements Ideas
- Adding a scoring system.
- Add a shield power-up
- Add a speed power-up
- Add acceleration to the player movement
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Adding sound effects and background music.
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add bombs that can be dropped
- Implementing different levels with increasing difficulty.

---
Developed as a practice project to explore Object-Oriented Programming principles in Python using Pygame.
