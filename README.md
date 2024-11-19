# Maze-Game-Mechanic-in-Python
Este proyecto es una "mecánica de juego de laberinto" en el lenguaje "Python"


--Descripción--

Utilizando la biblioteca `curses` para crear un entorno interactivo en la terminal. 

El objetivo del proyecto es ofrecer una base funcional de un juego de laberinto donde
el jugador controla a un personaje que debe evitar al enemigo que se mueve por el laberinto.

--Nota--: Este proyecto es solo un prototipo de la mecánica de un juego de laberinto.

--Características--

- Interacción en la terminal: Usa las teclas `W`, `A`, `S`, `D` para mover al jugador.
- Movimiento del enemigo: El enemigo se mueve automáticamente por el laberinto a intervalos regulares.
- Estilo visual: Utiliza caracteres ASCII para representar el laberinto, el jugador y el enemigo.
- Colores: El jugador y el enemigo están diferenciados por colores (`verde` para el jugador y `rojo` para el enemigo).

--Requisitos--

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes paquetes:

- `curses` (generalmente preinstalado en sistemas Linux y macOS)
- `colorama` (para la gestión de colores en la terminal)

Puedes instalar `colorama` usando `pip`:

```bash
pip install colorama
