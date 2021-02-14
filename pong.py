import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *

## RESOLUÇÃO DA TELA
LARGURA_JANELA = 1280
ALTURA_JANELA = 720

# CONFIGURAÇÃO DOS OBJETOS
xDaBola = 110
yDaBola = 0
tamanhoDaBola = 20
velocidadeDaBolaEmX = 0.1
velocidadeDaBolaEmy = 0.1

YDoJogador1 = 0
YDoJogador2 = 0

def xDoJogador1():
        return -LARGURA_JANELA / 2 + larguraDosJogadores() / 2
def xDoJogador2():
        return LARGURA_JANELA / 2 - larguraDosJogadores() / 2
def larguraDosJogadores():
        return tamanhoDaBola
def alturaDosJogadores():
        return 3 * tamanhoDaBola


def atualizar():
        global xDaBola, yDaBola, velocidadeDaBolaEmX, velocidadeDaBolaEmy, YDoJogador1, YDoJogador2

        xDaBola = xDaBola + velocidadeDaBolaEmX
        yDaBola = yDaBola + velocidadeDaBolaEmy

        if (xDaBola + tamanhoDaBola / 2 > xDoJogador2() - larguraDosJogadores() / 2
        and yDaBola - tamanhoDaBola / 2 < YDoJogador2 + alturaDosJogadores() / 2
        and yDaBola + tamanhoDaBola / 2 > YDoJogador2 - alturaDosJogadores() / 2):
                velocidadeDaBolaEmX = -velocidadeDaBolaEmX

        if (xDaBola + tamanhoDaBola / 2 < xDoJogador1() + larguraDosJogadores() / 2
        and yDaBola - tamanhoDaBola / 2 < YDoJogador1 + alturaDosJogadores() / 2
        and yDaBola + tamanhoDaBola / 2 > YDoJogador1 - alturaDosJogadores() / 2):
                velocidadeDaBolaEmX = -velocidadeDaBolaEmX

        if yDaBola + tamanhoDaBola / 2 > ALTURA_JANELA / 2:
                velocidadeDaBolaEmy = -velocidadeDaBolaEmy

        if yDaBola - tamanhoDaBola / 2 < -ALTURA_JANELA / 2:
                velocidadeDaBolaEmy = -velocidadeDaBolaEmy

        if xDaBola < -LARGURA_JANELA / 2 or xDaBola > LARGURA_JANELA / 2:
            xDaBola = 0
            yDaBola = 0

        keys = pygame.key.get_pressed()
# -----------------VELOCIDADE DOS CONTROLES-------------------------
        if keys[K_w]:
                YDoJogador1 = YDoJogador1 + 0.2
        if keys[K_s]:
                YDoJogador1 = YDoJogador1 - 0.2
        if keys[K_UP]:
                YDoJogador2 = YDoJogador2 + 0.2
        if keys[K_DOWN]:
                YDoJogador2 = YDoJogador2 - 0.2
        if keys[K_ESCAPE]:
                QUIT = exit()                   # botão para sair



def desenharRetangulo(x, y, largura, altura, r, g, b):
        glColor3f(r, g, b)

        glBegin(GL_QUADS)
        glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
        glVertex2f(0.5 * largura + x, -0.5 * altura + y)
        glVertex2f(0.5 * largura + x, 0.5 * altura + y)
        glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
        glEnd()


def desenhar():
        glViewport(0, 0, LARGURA_JANELA , ALTURA_JANELA)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)

        glClear(GL_COLOR_BUFFER_BIT)

        desenharRetangulo(xDaBola, yDaBola, tamanhoDaBola, tamanhoDaBola, 1, 0.15, 0)
        desenharRetangulo(xDoJogador1(),YDoJogador1, larguraDosJogadores(), alturaDosJogadores(), 0.5, 1, 0.25)
        desenharRetangulo(xDoJogador2(), YDoJogador2, larguraDosJogadores(),alturaDosJogadores(), 0, 0, 1)

        pygame.display.flip()



pygame.init()
pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), DOUBLEBUF | OPENGL)

while True:
        atualizar()
        desenhar()
       # pygame.event.pump() # para os eventos da biblioteca funcionarem corretamente
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                pygame.event.pump()