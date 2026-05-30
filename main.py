# GLOBAL SOLUTION - MONITORAMENTO DE MISSAO ESPACIAL

print("==========================================")
print(" CENTRAL DE MONITORAMENTO ESPACIAL")
print(" Energia Renovavel e Sustentabilidade")
print("==========================================")

# Dados de exemplo da missão
temperatura = 85
energia = 18
comunicacao = "offline"
painel_solar = "ativo"
modulo_vida = "ativo"
modulo_pesquisa = "ativo"

print()
print("DADOS ATUAIS DA MISSAO")
print("----------------------")
print("Temperatura:", temperatura, "C")
print("Energia:", energia, "%")
print("Comunicacao:", comunicacao)
print("Painel solar:", painel_solar)
print("Modulo de vida:", modulo_vida)
print("Modulo de pesquisa:", modulo_pesquisa)

print()
print("ALERTAS DO SISTEMA")
print("------------------")

# Verificação da temperatura
if temperatura > 80:
    print("ALERTA: Temperatura critica!")
else:
    print("Temperatura estável.")

# Verificação da energia
if energia < 20:
    print("ALERTA: Energia critica!")
else:
    print("Energia suficiente.")

# Verificação da comunicação
if comunicacao == "offline":
    print("ALERTA: Comunicacao perdida!")
else:
    print("Comunicacao funcionando.")

# Verificação do painel solar
if painel_solar == "ativo":
    print("Painel solar gerando energia renovavel.")
else:
    print("ALERTA: Painel solar inativo!")

print()
print("DECISOES AUTOMATICAS")
print("--------------------")

# Tomada de decisão pela temperatura
if temperatura > 80:
    print("Ação: Ativar sistema de resfriamento.")
else:
    print("Ação: Manter temperatura sendo monitorada.")

# Tomada de decisão pela energia
if energia < 20:
    modulo_pesquisa = "desligado"
    print("Ação: Desligar modulo de pesquisa para economizar energia.")
else:
    print("Ação: Manter todos os modulos ligados.")

# Tomada de decisão pela comunicação
if comunicacao == "offline":
    print("Ação: Tentar reconectar com a base.")
else:
    print("Ação: Continuar transmissao normal.")

print()
print("STATUS FINAL DOS MODULOS")
print("------------------------")
print("Modulo de vida:", modulo_vida)
print("Modulo de pesquisa:", modulo_pesquisa)

print()
print("SUSTENTABILIDADE")
print("----------------")
print("O sistema utiliza energia solar simulada para reduzir o consumo de fontes nao renovaveis.")
print("Quando a energia fica baixa, modulos secundarios sao desligados para economizar recursos.")

print()
print("Monitoramento finalizado.")
