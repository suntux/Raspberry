# Guillaume Evain - Fev 2015 - evain@alteys.fr
# Démo Raspberry PI
# Bouton pressé

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
# On définit l'input
GPIO.setup(12, GPIO.IN)
while True:
    input_value = GPIO.input(12)
    # Si la tension chute au niveau de GPIO12
    if input_value == False:
        print("Boutton pressé!")
        # Tant que bouton enfoncé on reste dans cete bouclepour ne pas
        # afficher 50 fois le message
        while input_value == False:
            input_value = GPIO.input(12)

    