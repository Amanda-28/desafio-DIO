nome= input("Qual o nome do pokemon?")
experiencia=  int(input("Qual a quantidade de experiência XP do pokemon?"))

def verifica_o_nivel_do_pokemon(nome,experiencia):
    if experiencia <= 1000:
        print(f"o pokemon {nome} tem {experiencia} de XP e está no nível Ferro")
    elif experiencia <= 2000:
        print(f"o pokemon {nome} tem {experiencia} de XP e está no nível bronze")
    elif experiencia <= 5000:
        print(f"o pokemon {nome} tem {experiencia} de XP e está no nível prata")  
    elif experiencia <= 7000:
        print(f"o pokemon {nome} tem {experiencia} de XP e está no nível ouro")
    elif experiencia <= 8000:
        print(f"o pokemon {nome} tem {experiencia} de XP e está no nível platina")
    elif experiencia <= 9000:
        print(f"o pokemon {nome} tem {experiencia} de XP e está no nível Ascendente") 
    elif experiencia <= 10000:
        print(f"o pokemon {nome} tem {experiencia} de XP e está no nível Imortal")     
    else:
        print(f"o pokemon {nome} tem {experiencia} de XP e está no nível Radiante")  
         


verifica_o_nivel_do_pokemon(nome,experiencia)
