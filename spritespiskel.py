import pygame  # Importa a biblioteca
from pygame.locals import *  # Importa tudo do módulo locals
from sys import exit  # Importa função para fechar o jogo

pygame.init()  # Inicia método pygame

largura = 640  # Define largura para tela
altura = 480  # Define altura para tela
preto = (0, 0, 0)  # Define cor preto, podendo ser usado no jogo, inclusive para tela

tela = pygame.display.set_mode((largura, altura)) #  Cria tela do jogo
pygame.display.set_caption("Sprites")  #  Nome tela

class Personagem(pygame.sprite.Sprite):  # Cria classe chamada sapo que herda atributos e métodos da classe sprite de pygame
    def __init__(self):  # Cria método construtor
        pygame.sprite.Sprite.__init__(self)  # Inicializa a classe
        self.sprites = []  # Cria lista
        self.sprites.append(pygame.image.load('homem_terno/sprite_0.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('homem_terno/sprite_1.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('homem_terno/sprite_2.png'))  # Adiciona na lista a imagem (sprite)

        self.atual = 0  # Define posição da imagem atual
        self.image = self.sprites[self.atual]  # Define a imagem, que contêm a sprite atual
        self.image = pygame.transform.scale(self.image, (32, 32))  # Tranforma a escala da imagem (em N *).

        self.rect = self.image.get_rect()  # O 'rect' pega o retangulo onde fica a imagem na tela
        self.rect.topleft = 100, 250  #  Define a posição que será exibido a imagem contida no retângulo.

    def update(self):  # Cria animação das sprites
        self.atual = self.atual + 0.35  # A variável receberá a posição + valor (ajuda controlar velocidade das sprites)
        if self.atual >= len(self.sprites):  # Se posição atual for maior que tamnho da quantidade de sprites
            self.atual = 0  # Se condição verdadeira, variável recebe 07
        self.image = self.sprites[int(self.atual)]#  Cria o indice das sprites
        self.image = pygame.transform.scale(self.image, (32 * 7, 32 * 7))  # Tranforma a escala da imagem em N * (se precisar).

todas_as_sprites = pygame.sprite.Group()  # Cria um objeto que recebe um grupo para armazenar sprites que serão instanciadas
personagem = Personagem()  # Cria um objeto a partir da classe Sapo para desenha sapo na tela
todas_as_sprites.add(personagem)  # Adiciona o sapo no grupo todas_as_sprites

imagem_fundo = pygame.image.load('cidade_fundo.gif').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()  # Define o tempo para controlar taxa de frame do jogo

while True:  #  Cria o loop principal, onde fica todas as ações do jogo
    relogio.tick(30)  # Define taxa de frame do jogo
    tela.fill(preto)  # Pinta tela toda de preto
    for event in pygame.event.get(): #  Cria loop dos eventos capturados
        if event.type == QUIT:  # Se o tipo do evento for sair
            pygame.quit()  #  Chama a função para sair do pygame
            exit()  # Executa função para fechar janela

    tela.blit(imagem_fundo, (0, 0))  # Posiciona o fundo apartir da posição 0, 0.
    todas_as_sprites.draw(tela)  # Desenha o objeto sapo na tela
    todas_as_sprites.update()  # Faz o update das sprites
    pygame.display.flip()  # Atualiza a tela
