from termcolor import colored

# 🎯 МАСТЕР-КЛАСС: "Создаём свою компьютерную игру за 45 минут"
# 🕐 Время: 45 минут
# 🎮 Тема: Python-детектив: Создаём текстовый квест"""

print(colored("=" * 60, 'blue'))
print(colored("🎮 ДОБРО ПОЖАЛОВАТЬ НА МАСТЕР-КЛАСС!", 'yellow', attrs=['bold']))
print(colored("🐍 Создаём свою компьютерную игру на Python!", 'green'))
print(colored("=" * 60, 'blue'))

# 🎯 Показываем пример игры
input(colored("\nНажми Enter чтобы начать игру...", 'white'))



# Основной код игры

# 🎯 Запускаем первую часть
print(colored("\n" + "=" * 40, 'yellow'))
print(colored("🚀 ЗАПУСКАЕМ ИГРУ!", 'yellow', attrs=['bold']))
print("Добро пожаловать в игру 'Загадка старого дома'!")
print("Ты стоишь перед темным домом. Войти?")
print("1 - Да, я не боюсь!")
print("2 - Нет, я лучше пойду домой.")
print(colored("=" * 40, 'yellow'))



# 🔥 Запускаем интерактивную часть
print(colored("\n" + "=" * 40, 'green'))
choice = input(colored("Сделай свой выбор (введи 1 или 2): ", 'yellow'))

if choice == "1":
    print(colored("🎉 Ты смело вошел в дом...", 'green'))
    print(colored("🔦 Внутри темно, но ты видишь две двери:", 'cyan'))
    print(colored("🚪 1 - Дверь слева (слышен странный шум)", 'white'))
    print(colored("🚪 2 - Дверь справа (пахнет свежим печеньем)", 'white'))
    
    # Развитие сюжета
    choice2 = input(colored("Куда пойдешь? (1 или 2): ", 'yellow'))
    
    if choice2 == "1":
        print(colored("👻 За дверью оказался дружелюбный призрак!", 'magenta'))
        print(colored("🏆 Он дал тебе ключ от сокровищницы! Ты выиграл!", 'yellow'))
    elif choice2 == "2":
        print(colored("🍪 Ты попал на кухню! Бабушка угощает тебя печеньем!", 'red'))
        print(colored("❤️ Ты нашел нового друга! Победа!", 'yellow'))
    else:
        print(colored("❌ Нужно было выбрать 1 или 2! Попробуй еще раз.", 'red'))
        
elif choice == "2":
    print(colored("🏃 Ты сбежал. Игра окончена.", 'red'))
    print(colored("💡 В следующий раз будь смелее!", 'cyan'))
else:
    print(colored("❌ Такого выбора нет! Запусти игру еще раз.", 'red'))
