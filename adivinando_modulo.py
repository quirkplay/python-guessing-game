"""
=========================== MODULO PRINCIPAL DEL JUEGO ADIVINANDO ===========================
                    Contiene la lógica de juego, menus, diálogos y modos.
"""

import random
import getpass
from configuracion import cargar_configuracion, guardar_configuracion, resetear_configuracion
from estadisticas_modulo import (
    inicializar_excel, 
    guardar_resultado,
    mostrar_todas_estadisticas,
    menu_rankings,
    buscar_mis_estadisticas
)


def mostrar_titulo():
    """Muestra la pantalla de bienvenida del juego"""
    
    print("\n" + "="*60)
    print(" "*10 + "🎩 ADIVINA EL NÚMERO 🎩")
    print("="*60)
    print("\n😏 El Maestro de las Adivinanzas ha notado tu presencia")
    print("   ¿Te atreves a jugar contra él?")
    print("   ¿O has traido a un invitado a su guarida?")
    print("\n" + "="*60)
    input("\nPresiona Enter para continuar...")


    
def seleccionar_dificultad():
    """Permite al jugador seleccionar la dificultad del juego"""
    
    dificultad_elegida = False
    
    while dificultad_elegida == False:
        print("\n--- SELECCIONA LA DIFICULTAD ---")
        print("1. Fácil (20 intentos)")
        print("2. Medio (12 intentos)")
        print("3. Difícil (5 intentos)")
        print("4. Volver al menú principal")
        
        opcion = input("\nElige la dificultad: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            
            if opcion == 4:
                return None  # Volver al menú principal
            
            if 1 <= opcion <= 3:
                if opcion == 1:
                    max_intentos = 20
                    dificultad = "Fácil"
                elif opcion == 2:
                    max_intentos = 12
                    dificultad = "Medio"
                else:  # opcion == 3
                    max_intentos = 5
                    dificultad = "Difícil"
                
                return (max_intentos, dificultad)
            else:
                print("ERROR: Debes elegir una opción entre 1 y 4.")
        else:
            print("ERROR: Debes introducir un número válido.")


    
def jugar_partida(numero_secreto, max_intentos, nombre_jugador, numero_maximo, pistas_activadas):
    """Ejecuta la lógica principal del juego"""
    
    acertado = False
    intentos = 0
    
    while acertado == False and intentos < max_intentos:
        print(f"\nIntentos restantes: {max_intentos - intentos}")
        intento = input(f"{nombre_jugador}, ¿qué número crees que es? ")
        
        if intento.isdigit():
            intento = int(intento)
            
            if 1 <= intento <= numero_maximo:
                intentos = intentos + 1
                
                if intento == numero_secreto:
                    print("\n" + "🎉" * 20)
                    print(f"   ¡CORRECTO! El número secreto era {numero_secreto}.")
                    print(f"   Lo adivinaste en {intentos} intentos.")
                    print("🎉" * 20)
                    print(f"\n{mensaje_maquina_victoria_jugador()}")
                    acertado = True
                else:
                    diferencia = abs(intento - numero_secreto)
                    
                    if intento < numero_secreto:
                        print(f"\n❌ {intento} es MENOR que el número secreto. Prueba un número más alto.")
                    else:
                        print(f"\n❌ {intento} es MAYOR que el número secreto. Prueba un número más bajo.")
                    
                    if pistas_activadas:
                        mostrar_pista(diferencia)
            else:
                print(f"ERROR: El número debe estar entre 1 y {numero_maximo}")
        else:
            print("ERROR: Debes introducir un número válido")
    
    return (acertado, intentos)



def mostrar_pista(diferencia):
    """Muestra una pista visual sobre qué tan cerca está el jugador"""
    
    if diferencia <= 10:
        print("🔥 ¡CALIENTE! ¡Estás muy cerca!")
        print(mensaje_maquina_caliente())
    elif diferencia <= 50:
        print("🌡️  Tibio... te estás acercando")
        print(mensaje_maquina_tibio())
    elif diferencia <= 100:
        print("❄️  Frío... estás un poco lejos")
        print(mensaje_maquina_frio())
    else:
        print("🧊 ¡Muy frío! Estás muy lejos")
        print(mensaje_maquina_muy_frio())



def mensaje_maquina_muy_frio():
    """Mensajes cuando el jugador está muy lejos"""
    mensajes = [
        "😏 ¿En serio? Ni siquiera te acercas... Esto será fácil.",
        "🎩 Ja! Estás perdidísimo. ¿Seguro que sabes contar?",
        "😎 Vaya, vaya... parece que alguien necesita clases de adivinación.",
        "🎪 ¡Pero qué intento tan patético! Inténtalo de nuevo, novato.",
        "👑 Ni caliente ni tibio... ¡estás CONGELADO! Jajaja."
    ]
    return random.choice(mensajes)

def mensaje_maquina_frio():
    """Mensajes cuando está lejos pero no tanto"""
    mensajes = [
        "❄️ Frío, frío... Me aburres. ¿Eso es todo lo que tienes?",
        "🎯 Mmm, no está mal, pero aún así... estoy bostezando aquí.",
        "⛄ Sigues muy lejos. ¿Te rindas ya?",
        "🎲 Bueno, al menos intentas... aunque sin mucho éxito.",
    ]
    return random.choice(mensajes)

def mensaje_maquina_tibio():
    """Mensajes cuando se está acercando"""
    mensajes = [
        "🌡️ Eh... tibio. Pero no creas que me estás asustando, ¿eh?",
        "😅 Vale, te estás acercando... p-pero aún no llegas.",
        "🤔 Mmm... interesante. ¿Suerte o habilidad? Seguro suerte.",
        "😬 Te estás calentando... pero yo sigo siendo superior.",
    ]
    return random.choice(mensajes)

def mensaje_maquina_caliente():
    """Mensajes cuando está muy cerca"""
    mensajes = [
        "🔥 ¡E-espera! ¡Estás demasiado cerca! ¡No puede ser!",
        "😰 ¡C-caliente! ¡Muy caliente! ¡P-pero no vas a ganar!",
        "😨 ¡Casi casi! ¡N-no! ¡Esto no estaba en mis cálculos!",
        "🥵 ¡CALIENTE! ¡Demasiado cerca para mi gusto! ¡Aléjate!",
    ]
    return random.choice(mensajes)

def mensaje_maquina_victoria_jugador():
    """Mensajes cuando el jugador gana"""
    mensajes = [
        "😤 ¡¿QUÉ?! ¡Imposible! ¡Debe haber sido un error del sistema!",
        "😡 ¡NO! ¡Acertaste! ¡Esto es inaceptable! ¡Trampa!",
        "🤬 ¡ARGH! ¡Lo admito, ganaste! ...esta vez. ESTA VEZ.",
        "😠 ¡Grrr! Tuviste suerte, eso es todo. ¡SUERTE!",
        "💢 ¡Me has vencido! ...Pero no te acostumbres, fue un accidente.",
    ]
    return random.choice(mensajes)

def mensaje_maquina_victoria_maquina():
    """Mensajes cuando la máquina gana"""
    mensajes = [
        "😂 ¡JA JA JA! ¡Lo sabía! No estás a mi altura, humano.",
        "🎩 ¡Victoria! Como era de esperarse. ¿Quieres intentarlo de nuevo? Spoiler: también perderás.",
        "👑 ¡GLORIOSA VICTORIA! Yo soy el maestro indiscutible. ¿Una revancha?",
        "😏 ¿Ya ves? Te lo dije. Pero hey, puedes intentarlo otra vez... para perder de nuevo.",
        "🎪 ¡DERROTA TOTAL! No te preocupes, la práctica hace al maestro... aunque dudo que llegues a mi nivel.",
    ]
    return random.choice(mensajes)



def modo_solitario(config):
    """Modo de juego solitario contra la máquina"""
    
    continuar_en_modo = True
    
    while continuar_en_modo:
        print("\n" + "="*50)
        print("🎩 EL MAESTRO DE LAS ADIVINANZAS ACEPTA TU DESAFÍO 🎩")
        print("="*50)
        print("😏 Prepárate, humano. Pocos logran vencerme...")
        
        # Paso 1: Obtener valores de configuración
        numero_maximo = config['numero_maximo']
        pistas_activadas = config['pistas_activadas']
        
        # Paso 2: Seleccionar dificultad
        resultado_dificultad = seleccionar_dificultad()
        
        if resultado_dificultad == None:
            print("\n😏 ¿Huyes? Sabía que no eras más que un cobarde...")
            return
        
        max_intentos, dificultad = resultado_dificultad
        
        # Paso 3: Pedir nombre del jugador
        nombre_jugador = input("\n¿Cómo te llamas, humano? ").strip()
        if nombre_jugador == "":
            nombre_jugador = "Cobarde Anónimo"
            print("😏 ¿Sin nombre? Te llamaré 'Cobarde Anónimo'.")
        
        # Paso 4: Comentar sobre la dificultad elegida
        if dificultad == "Fácil":
            mensajes_facil = [
                f"😏 ¿Fácil, {nombre_jugador}? Con 20 intentos esto será como quitarle un dulce a un bebé.",
                f"🎪 Veo que eliges el camino cobarde, {nombre_jugador}... 20 intentos y aún así perderás.",
                f"😴 20 intentos para ti... Casi me da pena. Esto será aburrido, {nombre_jugador}.",
                f"🎈 Modo fácil, {nombre_jugador}... Supongo que todos los perdedores empiezan por algún lado."
            ]
            print(random.choice(mensajes_facil))
        
        elif dificultad == "Medio":
            mensajes_medio = [
                f"🤔 12 intentos, {nombre_jugador}... Al menos tienes algo de coraje. Insuficiente, pero algo es algo.",
                f"⚡ Interesante elección, {nombre_jugador}. 12 intentos podrían ser... ligeramente entretenidos.",
                f"😏 Veo que no eres un completo cobarde, {nombre_jugador}. Aunque tampoco eres rival para mí.",
                f"🎯 12 oportunidades para fallar, {nombre_jugador}. Una elección balanceada... para perder balanceadamente."
            ]
            print(random.choice(mensajes_medio))
        
        elif dificultad ==  "Difícil":
            mensajes_dificil = [
                f"😈 ¡¿SOLO 5 INTENTOS?! ¡Ahora sí me interesas, {nombre_jugador}! ¡Prepárate para la humillación!",
                f"🔥 Vaya, vaya, {nombre_jugador}... 5 intentos. Eres valiente... o estúpido. ¡Me encanta!",
                f"👑 ¡OH! {nombre_jugador} elige el modo difícil... Esto será breve pero doloroso para ti.",
                f"⚔️ Solo 5 oportunidades, {nombre_jugador}... Respeto tu audacia, pero lamentarás tu arrogancia.",
                f"💀 {nombre_jugador}, con solo 5 intentos... Esto terminará antes de que te des cuenta. ¡COMENCEMOS!"
            ]
            print(random.choice(mensajes_dificil))
        
        # Paso 5: Generar número secreto
        numero_secreto = random.randint(1, numero_maximo)
        print(f"\n🧠 He pensado un número entre 1 y {numero_maximo}...")
        print("¡Que comience el juego!\n")
        
        # Paso 6: Jugar la partida
        acertado, intentos = jugar_partida(numero_secreto, max_intentos, nombre_jugador, 
                                           numero_maximo, pistas_activadas)
        
        # Paso 7: Mostrar resultado final
        if acertado == False:
            print("\n" + "❌" * 20)
            print("   ¡TE HAS QUEDADO SIN INTENTOS!")
            print(f"   El número secreto era: {numero_secreto}")
            print("❌" * 20)
            print(f"\n{mensaje_maquina_victoria_maquina()}")
        
        # Paso 8: Guardar resultado en Excel
        guardar_resultado(nombre_jugador, acertado, intentos, dificultad, "Solitario", "Jugador")
        
        # Paso 9: Salida
        accion = menu_salida_un_jugador(acertado, nombre_jugador)
        
        if accion == "menu_principal":
            continuar_en_modo = False
        elif accion == "repetir":
            continuar_en_modo = True
        elif accion == "salir":
            continuar_en_modo = False
            return "salir"


    
def menu_salida_un_jugador(jugador_gano, nombre_jugador):
    """Muestra opciones después de terminar con personalidad'"""
    
    opcion_valida = False
    
    while opcion_valida == False:
        print("\n--- ¿QUÉ DESEAS HACER? ---")
        
        if jugador_gano:
            print("1. Huir al menú principal, es imposible que vuelvas ganarme 🤡")
            print(f"2. ¿Otra partida? Esta vez no tendrás tanta suerte {nombre_jugador} 😏")
        else:
            print("1. Huir al menú principal como un cobarde 🐣")
            print("2. ¡REVANCHA! Pierde nuevamente con honor ⚔️")
        
        print("3. Salir del juego 👋")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            if jugador_gano:
                print(f"\n😤 Hmph. Disfruta tu minúscula y temporal victoria {nombre_jugador}...")
            else:
                print("\n😏 Sabia decisión. Vuelve cuando quieras para perder de nuevo.")
            return "menu_principal"
        elif opcion == "2":
            if jugador_gano:
                print(f"\n😠 ¡Bien! Esta vez no tendrás tanta suerte {nombre_jugador}...")
            else:
                print("\n😈 ¡Excelente! Me encanta cuando aún tienen esperanzas.")
            return "repetir"
        elif opcion == "3":
            print("\n¡Gracias por jugar! 👋")
            return "salir"
        else:
            print("ERROR: Debes elegir entre 1, 2 o 3")


# ===================================== MODO DOS JUGADORES =====================================



def modo_dos_jugadores(config):
    """Modo de juego para dos jugadores"""
    
    continuar_en_modo = True
    
    while continuar_en_modo:
        print("\n" + "="*50)
        print("🎪 EL MAESTRO OBSERVA UN DUELO DE HUMANOS 🎪")
        print("="*50)
        print("😏 Veamos quién de ustedes dos es menos patético...")
        
        # Paso 1: Obtener valores de configuración
        numero_maximo = config['numero_maximo']
        pistas_activadas = config['pistas_activadas']
        
        # Paso 2: Pedir nombres de los jugadores
        print("\n--- PRESENTACIÓN DE LOS CONTENDIENTES ---")
        
        jugador1 = input("Nombre del Jugador 1 (Desafiante - quien elige el número): ").strip()
        if jugador1 == "":
            jugador1 = "Cobarde Anónimo"
            print(f"😏 Sin nombre, ¿eh? Serás '{jugador1}'.")
        
        jugador2 = input("Nombre del Jugador 2 (Adivinador - quien adivina): ").strip()
        if jugador2 == "":
            if jugador1 == "Cobarde Anónimo":
                jugador2 = "Gallina Anónima"
                print(f"😏 Tampoco das tu nombre... Te llamaré '{jugador2}'.")
            else:
                jugador2 = "Gallina Anónima"
                print(f"😏 ¿Sin nombre? Al menos {jugador1} tuvo el valor de presentarse. Serás '{jugador2}'.")
        
        # Paso 3: Comentario introductorio
        mensajes_inicio = [
            f"🎭 {jugador1} vs {jugador2}... Esto podría ser entretenido. O aburrido. Probablemente aburrido.",
            f"😈 ¡Excelente! {jugador1} intenta engañar a {jugador2}. Me encanta ver humanos compitiendo.",
            f"🎪 {jugador1} y {jugador2}... ¿Listos para humillarse mutuamente? ¡Yo lo estoy!",
            f"👑 Veamos si {jugador2} puede superar el desafío de {jugador1}. Spoiler: lo dudo."
        ]
        print(f"\n{random.choice(mensajes_inicio)}")
        
        # Paso 4: Seleccionar dificultad, con opción de salida.
        resultado_dificultad = seleccionar_dificultad()
        
        if resultado_dificultad == None:
            print(f"\n😏 ¿{jugador1} huye? ¡Qué sorpresa! Los cobardes siempre se reconocen.")
            return
            
        max_intentos, dificultad = resultado_dificultad
        
        if dificultad == "Fácil":
            mensajes_facil = [
                f"😏 ¿Fácil? {jugador1}, le estás regalando la victoria a {jugador2}. Qué aburrido.",
                f"🎪 20 intentos... {jugador2}, si pierdes con tantas oportunidades, mejor retírate.",
                f"😴 Modo fácil... Esto será tan emocionante como ver pintura secarse.",
                f"🎈 {jugador1} es generoso... o cobarde. {jugador2}, esto debería ser pan comido para ti."
            ]
            print(random.choice(mensajes_facil))
        
        elif dificultad == "Medio":
            mensajes_medio = [
                f"🤔 12 intentos... Interesante. {jugador2}, no te confíes. {jugador1} puede sorprenderte.",
                f"⚡ Modo medio. {jugador1} no es tan generoso. {jugador2}, tendrás que esforzarte.",
                f"😏 12 oportunidades, {jugador2}. {jugador1} eligió un desafío justo... o eso cree.",
                f"🎯 Balanceado. {jugador2}, si pierdes será por incompetencia, no por falta de intentos."
            ]
            print(random.choice(mensajes_medio))
        
        elif dificultad == "Difícil": 
            mensajes_dificil = [
                f"😈 ¡SOLO 5 INTENTOS! {jugador1}, eres cruel. {jugador2}, prepárate para sufrir.",
                f"🔥 Modo difícil... {jugador2}, espero que tengas mucha suerte. La necesitarás.",
                f"👑 5 intentos. {jugador1} quiere victoria rápida. {jugador2}, esto será... breve.",
                f"⚔️ ¡Modo difícil! {jugador1} no tiene piedad. {jugador2}, que los dioses te ayuden.",
                f"💀 Solo 5 oportunidades... {jugador2}, esto terminará en lágrimas. Tuyas, obviamente."
            ]
            print(random.choice(mensajes_dificil))
        
        # Paso 5: Jugador 1 elige el número secreto (entrada oculta)
        numero_secreto = obtener_numero_secreto(jugador1, numero_maximo)
        
        mensajes_numero_elegido = [
            f"😏 {jugador1} ha elegido su número... {jugador2}, prepárate para fallar miserablemente.",
            f"🎯 Número elegido. Ahora {jugador2} tiene {max_intentos} oportunidades para no hacer el ridículo.",
            f"🎪 {jugador1} cree que eligió un buen número... Veremos si {jugador2} es tan tonto como parece.",
            f"😈 ¡Perfecto! {jugador2}, tu oponente te ha puesto una trampa. ¡Esto será divertido!"
        ]
        print(f"\n{random.choice(mensajes_numero_elegido)}")
        
        # Paso 6: Jugador 2 intenta adivinar
        print(f"\n🎮 Turno de {jugador2}!")
        print(f"Debes adivinar el número entre 1 y {numero_maximo}")
        print(f"Tienes {max_intentos} intentos. ¡Que comience el juego!\n")
        
        acertado, intentos = jugar_partida(numero_secreto, max_intentos, jugador2, 
                                           numero_maximo, pistas_activadas)
        
        # Paso 7: Mostrar resultado final con comentarios
        if acertado:
            print("\n" + "🎉" * 20)
            print(f"   ¡{jugador2} HA GANADO!")
            print(f"   Adivinó el número {numero_secreto} en {intentos} intentos.")
            print("🎉" * 20)
            
            # Comentarios cuando gana el adivinador
            mensajes_victoria_adivinador = [
                f"😤 ¡Increíble! {jugador2} acertó... {jugador1}, tu número era pésimo.",
                f"😠 {jugador2} ganó... Admito que no esperaba tanta suerte. O tal vez {jugador1} eligió mal.",
                f"🤬 ¡{jugador1} ha sido derrotado! {jugador2}, no te emociones, fue suerte.",
                f"💢 Victoria de {jugador2}... {jugador1}, deberías practicar eligiendo mejores números."
            ]
            print(f"\n{random.choice(mensajes_victoria_adivinador)}")
            
            # Guardar resultado para ambos jugadores
            guardar_resultado(jugador2, True, intentos, dificultad, "2 Jugadores", "Adivinador")
            guardar_resultado(jugador1, False, intentos, dificultad, "2 Jugadores", "Desafiante")
            
        else:
            print("\n" + "❌" * 20)
            print(f"   ¡{jugador2} SE HA QUEDADO SIN INTENTOS!")
            print(f"   El número secreto era: {numero_secreto}")
            print(f"   ¡{jugador1} GANA!")
            print("❌" * 20)
            
            # Comentarios cuando gana el desafiante
            mensajes_victoria_desafiante = [
                f"😂 ¡JA JA JA! {jugador2} falló completamente. {jugador1}, ganaste... pero contra un rival patético.",
                f"🎩 {jugador1} triunfa... Aunque no estoy seguro si fue habilidad tuya o incompetencia de {jugador2}.",
                f"👑 Victoria para {jugador1}. {jugador2}, deberías considerar otro pasatiempo.",
                f"😏 {jugador2} pierde. {jugador1}, disfruta tu victoria mediocre contra un oponente aún más mediocre."
            ]
            print(f"\n{random.choice(mensajes_victoria_desafiante)}")
            
            # Guardar resultado para ambos jugadores
            guardar_resultado(jugador2, False, intentos, dificultad, "2 Jugadores", "Adivinador")
            guardar_resultado(jugador1, True, intentos, dificultad, "2 Jugadores", "Desafiante")
        
        # Paso 8: Menú de salida
        accion = menu_salida_dos_jugadores(acertado, jugador1, jugador2)
        
        if accion == "menu_principal":
            continuar_en_modo = False
        elif accion == "repetir":
            continuar_en_modo = True
        elif accion == "salir":
            continuar_en_modo = False
            return "salir"



def obtener_numero_secreto(nombre_jugador, numero_maximo):
    """Permite al jugador elegir un número secreto sin que se vea en pantalla"""
    
    numero_valido = False
    
    print(f"\n🎭 {nombre_jugador}, es tu turno de elegir el número secreto.")
    print(f"⚠️  IMPORTANTE: Asegúrate de que el otro jugador no pueda verte teclear.")
    
    while numero_valido == False:
        # Uso getpass para ocultar la entrada
        numero_str = getpass.getpass(f"\n{nombre_jugador}, introduce el número secreto (entre 1 y {numero_maximo}): ")
        
        if numero_str.isdigit():
            numero = int(numero_str)
            
            if 1 <= numero <= numero_maximo:
                print("\n✅ Número secreto guardado.")
                return numero
            else:
                print(f"\n❌ ERROR: El número debe estar entre 1 y {numero_maximo}")
        else:
            print("\n❌ ERROR: Debes introducir un número válido")



def menu_salida_dos_jugadores(adivinador_gano, jugador1, jugador2):
    """Menú de salida para modo 2 jugadores con personalidad"""
    
    opcion_valida = False
    
    while opcion_valida == False:
        print("\n--- ¿QUÉ DESEAN HACER? ---")
        
        if adivinador_gano:
            print(f"1. Huir al menú principal (recomendado para {jugador1}) 🏃")
            print(f"2. ¡REVANCHA! {jugador1} quiere redimirse 🔥")
        else:
            print(f"1. Huir al menú principal (recomendado para {jugador2}) 🐔")
            print(f"2. ¡REVANCHA! {jugador2} quiere su revancha ⚔️")
        
        print("3. Salir del juego 👋")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            if adivinador_gano:
                print(f"\n😏 {jugador1} huye... Sabía que no aguantarías una revancha.")
            else:
                print(f"\n😈 {jugador2} se retira derrotado... Sabia decisión.")
            return "menu_principal"
        
        elif opcion == "2":
            if adivinador_gano:
                print(f"\n🔥 ¡{jugador1} quiere revancha! Me encanta ver la desesperación.")
            else:
                print(f"\n⚔️ ¡{jugador2} no se rinde! Admirable... o estúpido.")
            return "repetir"
        
        elif opcion == "3":
            print("\n¡Gracias por jugar! 👋")
            return "salir"
        
        else:
            print("ERROR: Debes elegir entre 1, 2 o 3")


# ===================================== MENÚ DE ESTADÍSTICAS =====================================



def menu_estadisticas():
    """Menú principal de estadísticas"""
    ruta_fichero = "estadisticas.xlsx"
    
    if os.path.exists(ruta_fichero) == False:
        print("\n⚠️  No hay estadísticas disponibles")
        print("Juega algunas partidas primero")
        input("\nPresiona Enter para continuar...")
        return
    
    continuar = True
    
    while continuar:
        print("\n" + "="*50)
        print(" "*15 + "ESTADÍSTICAS")
        print("="*50)
        print("1. Ver todas las estadísticas")
        print("2. Rankings")
        print("3. Buscar mis estadísticas")
        print("4. Volver al menú principal")
        print("="*50)
        
        opcion = input("\nElige una opción: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            
            if 1 <= opcion <= 4:
                if opcion == 1:
                    mostrar_todas_estadisticas()
                elif opcion == 2:
                    menu_rankings()
                elif opcion == 3:
                    buscar_mis_estadisticas()
                elif opcion == 4:
                    continuar = False
            else:
                print("ERROR: Debes elegir entre 1 y 4")
        else:
            print("ERROR: Debes introducir un número válido")


# ===================================== MENÚ DE INSTRUCCIONES =====================================

    

def menu_como_jugar():
    """Muestra las instrucciones del juego"""
    
    config = cargar_configuracion()
    numero_maximo = config['numero_maximo']
    
    if config['pistas_activadas']:
        estado_pistas = "Activadas"
    else:
        estado_pistas = "Desactivadas"
    
    print("\n" + "="*60)
    print("         📖 ¿CÓMO JUGAR?")
    print("="*60)
    
    print("\n🎯 OBJETIVO:")
    print("   Adivina el número secreto que ha pensado el Maestro")
    print("   de las Adivinanzas antes de quedarte sin intentos.")
    
    print("\n🎮 MODO SOLITARIO:")
    print(f"  • El Maestro de las Adivinanzas piensa un número entre 1 y {numero_maximo}")
    print("   • Tú intentas adivinarlo")
    print("   • Recibirás pistas de si tu número es mayor o menor")
    print("   • Si las pistas avanzadas están activadas, recibirás indicaciones")
    print("     de qué tan cerca estás (caliente, tibio, frío)")
    
    print("\n👥 MODO 2 JUGADORES:")
    print("   • Un jugador piensa el número (Desafiante)")
    print("   • El otro intenta adivinarlo (Adivinador)")
    print("   • El Desafiante introduce su número de forma oculta")
    print(f"   • El número debe estar entre 1 y {numero_maximo}")
    print("   • El Adivinador tiene los intentos según la dificultad")
    print("   • Mismas reglas y pistas que el modo solitario")
    
    print("\n🎚️ DIFICULTADES:")
    print("   • Fácil:   20 intentos")
    print("   • Medio:   12 intentos")
    print("   • Difícil:  5 intentos")
    
    print("\n🔥 PISTAS DE TEMPERATURA:")
    print("   Si las pistas avanzadas están ACTIVADAS. Recibirás:")
    print("   • 🧊 Muy frío:  Diferencia mayor a 100")
    print("   • ❄️  Frío:     Diferencia entre 51-100")
    print("   • 🌡️  Tibio:    Diferencia entre 11-50")
    print("   • 🔥 Caliente: Diferencia de 10 o menos")
    print("   Si las pistas avanzadas están DESACTIVADAS:")
    print("   Solo recibirás información de si tu número es mayor o menor.")
    
    print("\n⚙️ CONFIGURACIÓN ACTUAL:")
    print(f"   • Número máximo: {numero_maximo}")
    print(f"   • Pistas avanzadas: {estado_pistas}")
    print("   • Puedes cambiar estos valores en el menú de Configuración")
    
    print("\n📊 ESTADÍSTICAS:")
    print("   Todas tus partidas se guardan automáticamente.")
    print("   Puedes consultar tus estadisticas y las de tus amigos,")
    print("   y pueden competir en los rankings globales.")
    
    print("\n" + "="*60)
    input("\nPresiona Enter para volver al menú...")



# ===================================== MENÚ DE CONFIGURACIÓN =====================================



def menu_configuracion(config):
    """Menú de configuración del juego"""
    
    continuar = True
    
    while continuar:
        print("\n" + "="*50)
        print(" "*15 + "CONFIGURACIÓN")
        print("="*50)
        print(f"\n📊 Configuración actual:")
        print(f"  • Número máximo: {config['numero_maximo']}")
        
        if config['pistas_activadas']:
            print("  • Pistas: Activadas")
        else:
            print("  • Pistas: Desactivadas")
            
        print("\n" + "="*50)
        print("1. Cambiar número máximo")
        print("2. Activar/Desactivar pistas avanzadas")
        print("3. Restaurar valores por defecto")
        print("4. Volver al menú principal")
        print("="*50)
        
        opcion = input("\nElige una opción: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            
            if 1 <= opcion <= 4:
                if opcion == 1:
                    cambiar_numero_maximo(config)
                elif opcion == 2:
                    cambiar_pistas(config)
                elif opcion == 3:
                    resetear_configuracion()
                    config = cargar_configuracion()
                    print("\n✅ Configuración restaurada a valores por defecto")
                elif opcion == 4:
                    continuar = False
            else:
                print("ERROR: Debes elegir entre 1 y 4")
        else:
            print("ERROR: Debes introducir un número válido")



def cambiar_numero_maximo(config):
    """Permite cambiar el número máximo del juego"""
    
    print(f"\nNúmero máximo actual: {config['numero_maximo']}")
    
    valido = False
    
    while valido == False:
        nuevo_numero = input("Introduce el nuevo número máximo (100-10000) o presiona Enter para volver: ").strip()
        
        if nuevo_numero == "":
            print("\n❌ Cambio cancelado")
            return
        
        if nuevo_numero.isdigit():
            nuevo_numero = int(nuevo_numero)
            
            if 100 <= nuevo_numero <= 10000:
                config['numero_maximo'] = nuevo_numero
                guardar_configuracion(config)
                print(f"\n✅ Número máximo actualizado a {nuevo_numero}")
                valido = True
            else:
                print("ERROR: El número debe estar entre 100 y 10000")
        else:
            print("ERROR: Debes introducir un número válido")

            

def cambiar_pistas(config):
    """Activa o desactiva las pistas"""
    
    if config['pistas_activadas']:
        print("\nPistas avanzadas: Activadas")
    else:
        print("\nPistas avanzadas: Desactivadas")
    
    confirmado = False
    
    while confirmado == False:
        print("\n¿Deseas cambiar el estado de las pistas?")
        print("1. Sí, cambiar")
        print("2. No, volver sin cambios")
        
        opcion = input("\nElige una opción: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            
            if opcion == 1:
                if config['pistas_activadas']:
                    config['pistas_activadas'] = False
                    mensaje = "desactivadas"
                else:
                    config['pistas_activadas'] = True
                    mensaje = "activadas"
                
                guardar_configuracion(config)
                print(f"\n✅ Pistas {mensaje}")
                confirmado = True
            
            elif opcion == 2:
                print("\n❌ Cambio cancelado. Volviendo al menú de configuración...")
                confirmado = True
            
            else:
                print("ERROR: Debes elegir 1 o 2")
        else:
            print("ERROR: Debes introducir un número válido")