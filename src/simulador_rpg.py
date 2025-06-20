import random

def mostrar_titulo():
    print('Bem-vindo ao Heran RPG')

def iniciar_jogo():
    nome = str(input('Digite seu nome: '))
    hp = 100
    lvl = 1
    forca = 3
    exp = 0
    inventario = []
    status = True
    
    return nome, hp, lvl, forca, exp, inventario, status

def sortear_monstro(jogador_lvl):
    slime = ['slime', 10, 2, 10]
    goblin = ['goblin', 20, 4, 20]
    troll = ['troll', 40, 8, 40]
    orc = ['orc', 80, 16, 80]
    mumia = ['mumia', 160, 32, 160]
    quimera = ['quimera', 320, 64, 320]
    dragao = ['dragao', 1000, 100, 1000]
    
    if jogador_lvl < 5:
        monstro_sorteado = random([slime, goblin, troll])
    elif jogador_lvl >= 5 and jogador_lvl < 10:        
        monstro_sorteado = random([troll, orc, mumia, quimera])
    else:
        monstro_sorteado = random([mumia, quimera, dragao])
        
    return monstro_sorteado

def game_over():
    print('O jogo acabou.')
    print('Obrigado por jogar!')
    exit(0)
    
def atacar(atacante_nome, atacante_forca, defensor_nome, defensor_forca, defensor_hp):
    atacante_sorte = random.randint(0,6)
    defensor_sorte = random.randint(0,6)
    
    if atacante_sorte == 6:
        print(f'O {atacante_nome} acertou um ataque crítico!')
    elif atacante_sorte > 0:
        print(f'O {atacante_nome} acertou um ataque!')
    else:
        print(f'O {atacante_nome} errou o golpe!')
    
    dano = (atacante_forca * atacante_sorte) - (defensor_forca * defensor_sorte)
    if dano > 0:
        print(f'O {defensor_nome} sofreu um dano de {dano}')
        defensor_hp -= dano
    else:
        print(f'O {defensor_nome} não sofreu dano')

    if defensor_hp <= 0:
        print(f'O {defensor_nome} morreu!')
        return 0
    else:
        return defensor_hp

def calcular_level(jogador_lvl, jogador_exp, jogador_hp, jogador_forca, exp_monstro):
    jogador_exp += exp_monstro
    exp_necessaria = 3 ** jogador_lvl
    
    if jogador_exp > exp_necessaria:
        print('Level Up!')
        jogador_lvl += 1
        jogador_hp = 100
        jogador_forca *= 2
        
    return jogador_lvl, jogador_exp, jogador_hp, jogador_forca

def obter_pocao():
    chance = random.random()
    if chance <= 0.2:
        print('Você ganho uma poção!')
        return 'Poção'
    else:
        return None
    
def usar_item(jogador_inventario, jogador_hp):
    if not jogador_inventario:
        print('Seus inventario esta vazio!\n')
    else:
        print('Inventario')
        for index, item in enumerate(jogador_inventario):
            print(f'{index+1}. {item} ')
        opcao_item = int(input('Escolha o item (ou 0 para cancelar): '))
        if opcao_item == 0:
            print('\n')
        else:
            item_escolhido = jogador_inventario[opcao_item - 1]
            if item_escolhido == 'Poção':
                print('Você usou uma poção!')
                jogador_hp += 20
                if jogador_hp > 100:
                    jogador_hp = 100
                    print(f'Seu HP agora é {jogador_hp}.\n')
                    jogador_inventario.pop(opcao_item-1)
            else:
                print('Item invalido!\n')

def fugir(jogador_nome):
    sucesso = random.choice([True, False])
    if sucesso:
        print(f'{jogador_nome} fugiu com sucesso!')
        return True
    else:
        print(f'{jogador_nome} não conseguiu escapar!')
        return False


def main():
    mostrar_titulo()
    jogador_nome, jogador_hp, jogador_lvl, jogador_forca, jogador_exp, jogador_inventario, jogador_status = iniciar_jogo()
    print('\n')
    
    jogador_enfrentando_monstro = False
    while True:
        if not jogador_enfrentando_monstro:
            monstro_nome, monstro_hp, monstro_forca, monstro_exp = sortear_monstro(jogador_lvl)
            
            print(f'\nUm {monstro_nome} aleatorio aparece!')
            print(f'HP: {monstro_hp}\n')
            jogador_enfrentando_monstro = True
        else:
            print(f'Você esta enfrentando um monstro {monstro_nome}!')
            print(f'HP: {monstro_hp}\n')
            
            print(f'{jogador_nome}: {jogador_hp}/100')
            print(f'Level: {jogador_lvl}')
            print('O que voce deseja fazer?')
            print('1. Atacar')
            print('2. Usar Item')
            print('3. Fugir')
            print('4. Visualizar Status')
            print('5. Sair do jogo')
            
            opcao = int(input())
            if opcao == 1:
                print("\n")
                monstro_hp, monstro_vivo = atacar(jogador_nome, jogador_forca, monstro_nome, monstro_hp, monstro_forca)
                print("\n")
                if monstro_vivo:
                    jogador_hp, jogador_vivo = atacar(monstro_nome, monstro_forca, jogador_nome, jogador_hp, jogador_forca)
                    print("\n")
                    if not jogador_vivo:
                        game_over()
                else:
                    print(f"Você ganhou {monstro_exp} XP!")
                    jogador_lv, jogador_exp, jogador_hp, jogador_forca = calcular_level(jogador_lv, jogador_exp, jogador_hp, jogador_forca, monstro_exp)
                    pocao = obter_pocao()
                    if pocao is not None:
                        jogador_inventario.append(pocao)
                    jogador_enfrentando_monstro = False
                    continue
            elif opcao == 2:
                jogador_hp, jogador_inventario = usar_item(jogador_inventario, jogador_hp)
                continue
            elif opcao == 3:
                fugiu = fugir(jogador_nome)
                if fugiu:
                    jogador_enfrentando_monstro = False
                    continue
                else:
                    jogador_hp, jogador_vivo = atacar(monstro_nome, monstro_forca, jogador_nome, jogador_hp, jogador_forca)
                    print("\n")
                    if not jogador_vivo:
                        game_over()
            elif opcao == 4:
                print(f"\n{jogador_nome}")
                print(f"HP: {jogador_hp/100}")
                print(f"LV: {jogador_lv}")
                print(f"EXP: {jogador_exp}")
                exp_proximo_nivel = 5 ** jogador_lv
                print(f"Falta {exp_proximo_nivel - jogador_exp} XP para evoluir")
                print(f"Força: {jogador_forca}")
                print(f"Inventário: {jogador_inventario}\n")
                continue
            elif opcao == 5:
                game_over()
            else:
                print("Opção inválida!\n")
                continue


    
if __name__ == '__main__':
    main()
