# БОТ-КАЛЬКУЛЯТОР ДЛЯ РАЦИОНАЛЬНЫХ И КОМПЛЕКСНЫХ ЧИСЕЛ

## Данный бот имеет следующую структуру:
1. bot_calculator_commands - данный модуль отвечает за совершение арифметических операций двух рациональных или 
   комплексных чисел
2. another_bot_commands - модуль в котором указаны дополнителные команды (/help - для отображения существующих 
   команд в боте; /manual - инструкция по взаимодействию с ботом; /hello - привествие пользователя)
3. logger - модуль записи результатов деятельности в БД
4. main - модуль запуска

## Как осуществляется работа с ботом
1. Выбрать тип чисел: для комплексных чисел: /complex; для рациональных чисел: /rational
2. Осуществить соответсвующий ввод операции. Т.е указываем тип числа, вводим числа без пробела, отделяем пробелом 
   только оператор с двух сторон.
3. Получить вывод.

## Примеры ввода:
/complex 5+9j - 3-8j <br>
/complex 8-18j * 13+2j <br>
/rational 8 * 9 <br>
/rational 77 / 6 <br>
и т.д.