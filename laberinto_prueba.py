import curses
import time
from colorama import Style, init


init()


def mostrar_laberinto(stdscr, laberinto, posicion, posicion_enemigo):
    stdscr.clear()
    for i, fila in enumerate(laberinto):
        for j, casillero in enumerate(fila):
            if [i, j] == posicion:
                stdscr.addstr(i, j * 2, '☻', curses.color_pair(1)) #player (green)
            elif [i, j] == posicion_enemigo:
                stdscr.addstr(i, j * 2, '✶', curses.color_pair(2))  #enemy (red)
            else:
                stdscr.addstr(i, j * 2, casillero)
    stdscr.refresh()

def main(stdscr):
    #init setting
    curses.curs_set(0)  #Oculta el cursor (entrada de texto)
    stdscr.nodelay(1)   #runs without input // se ejecuta aunque no se presione una tecla

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Inicializar verde
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Inicializar rojo

    laberinto = [
        ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
        ["#","_","_","_","#","#","_","_","_","#","#","#","_","_","_","_","#","#","#","#"],
        ["#","_","#","_","#","#","_","#","_","#","#","#","_","#","#","#","#","#","#","#"],
        ["#","_","_","_","#","#","_","#","_","#","#","#","_","#","#","#","#","#","#","#"],
        ["#","_","_","_","#","#","_","#","_","_","_","_","_","#","#","#","#","#","#","#"],
        ["#","_","_","_","#","#","_","#","_","#","#","#","_","#","#","#","#","#","#","#"],
        ["#","_","_","_","#","#","_","#","_","#","#","#","_","#","#","#","#","#","#","#"],
        ["#","_","_","_","#","_","_","#","_","#","#","#","_","#","#","#","#","#","#","#"],
        ["#","_","_","_","_","_","_","_","_","_","_","_","_","#","#","#","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
    ]

    posicion = [1, 1] #player init position
    posicion_enemigo = [1, 6] #enemy init position
    bajar = True  #enemy
    ultima_actualizacion = time.time()

    while True:
        # Keyboard ('w'-'a'-'s'-'d')
        key = stdscr.getch() #user input
        if key == ord('w') and laberinto[posicion[0] - 1][posicion[1]] != '#':
            posicion[0] -= 1
        elif key == ord('s') and laberinto[posicion[0] + 1][posicion[1]] != '#':
            posicion[0] += 1
        elif key == ord('a') and laberinto[posicion[0]][posicion[1] - 1] != '#':
            posicion[1] -= 1
        elif key == ord('d') and laberinto[posicion[0]][posicion[1] + 1] != '#':
            posicion[1] += 1
        elif key == ord('q'):
            break

        # Updates enemy position every 0.6 seconds // Actualiza la posición del enemigo cada 0.6 segundos
        tiempo_actual = time.time()
        if tiempo_actual - ultima_actualizacion >= 0.6:
            if bajar:
                posicion_enemigo[0] += 1
                if posicion_enemigo[0] == 8:
                    bajar = False
            else:
                posicion_enemigo[0] -= 1
                if posicion_enemigo[0] == 1:
                    bajar = True
            ultima_actualizacion = tiempo_actual

        #Check if there is contact with the enemy // Verificar si hay contacto con el enemigo
        if posicion == posicion_enemigo:
            stdscr.addstr(len(laberinto), 0, "¡Has sido atrapado! Game Over", curses.color_pair(2))
            stdscr.refresh()
            time.sleep(2)  # Wait two seconds / espera dos segundos
            break

        #Show updated maze // Mostrar el laberinto actualizado
        mostrar_laberinto(stdscr, laberinto, posicion, posicion_enemigo)
        time.sleep(0.1)  #Adjust timing for fluency // Ajustar el tiempo para la fluidez

if __name__ == "__main__":
    curses.wrapper(main)
