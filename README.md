### Hexlet tests and linter status:
[![Actions Status](https://github.com/SergeyChalkov/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/SergeyChalkov/python-project-lvl1/actions)
### CodeClimate Maintainability:
[![Maintainability](https://api.codeclimate.com/v1/badges/bf052ae5647e163be2a1/maintainability)](https://codeclimate.com/github/SergeyChalkov/python-project-lvl1/maintainability)
### Linter check badge:
[![flake8-check](https://github.com/SergeyChalkov/python-project-lvl1/actions/workflows/flake8_check.yml/badge.svg?event=push)](https://github.com/SergeyChalkov/python-project-lvl1/actions/workflows/flake8_check.yml)

Небольшой пакет, содержащий несколько простейших, запускающихся из командной строки, игр.
Написан в рамках обучающего проекта онлайн-школы программирования <a href="https://ru.hexlet.io/"><b>Хекслет</b></a>.<br>
Для использования требуется ОС на базе Linux / MacOS, а также установленный менеджер зависимостей и управления пакетами <a href="https://python-poetry.org/"><b>Poetry</b></a>.<br>
После скачивания репозитория Вы можете воспользоваться следующими командами для установки пакета:
1. **make install** либо **poetry install** *- устанавливает требующиеся для пакета зависимости*
2. **make build** либо **poetry build** *- подготавливает пакет для установки в систему*
3. **make package-install** либо **python3 -m pip install --user dist/\*.whl** - *устанавливает пакет*<br>
(также возможно, что в Вашей системе интерпретатор Питона вызывается командой *python*, в этом случае требуется использование команды **python -m pip install --user dist/\*.whl**)<br>
**Все команды требуется запускать из родительской директории проекта, содержащей Makefile**<br>

После успешной установки пакета Вы можете запускать головоломки следующими командами:
- brain-games - *выводит на экран приветствие*
- <a href="https://asciinema.org/a/449730"><b>brain-even</b></a> - *задачи на (не)чётность чисел*
- <a href="https://asciinema.org/a/450329"><b>brain-calc</b></a> - *решение примеров на сложение, вычитание, умножение*
- <a href="https://asciinema.org/a/450356"><b>brain-gcd (greater common divisor)</b></a> - *вычисление наибольшего общего делителя двух чисел*
- <a href="https://asciinema.org/a/450466"><b>brain-progression</b></a> - *поиск недостающего члена арифметической прогрессии*
- <a href="https://asciinema.org/a/450526"><b>brain-prime</b></a> - *является-ли число простым?* 

### Демонстрация установки и запуска пакета, записи созданы с помощью <a href="https://asciinema.org/"><b>asciinema</b></a> :
<a href="https://asciinema.org/a/449730"><b>brain-even:</b></a>

<a href="https://asciinema.org/a/449730"><img src="https://asciinema.org/a/449730.svg" alt="brain-even" title="brain-even game" width="200"/></a>

<a href="https://asciinema.org/a/450329"><b>brain-calc:</b></a>

<a href="https://asciinema.org/a/452547"><img src="https://asciinema.org/a/452547.svg" alt="brain-calc" title="brain-calc game" width="200"/></a>

<a href="https://asciinema.org/a/450356"><b>brain-gcd:</b></a>

<a href="https://asciinema.org/a/450356"><img src="https://asciinema.org/a/450356.svg" alt="brain-gcd" title="brain-gcd game" width="200" /></a>

<a href="https://asciinema.org/a/450466"><b>brain-progression:</b></a>

<a href="https://asciinema.org/a/450466"><img src="https://asciinema.org/a/450466.svg" alt="brain-progression" title="brain-progression game" width="200" /></a>

<a href="https://asciinema.org/a/450526"><b>brain-prime:</b></a>

<a href="https://asciinema.org/a/450526"><img src="https://asciinema.org/a/450526.svg" alt="brain-prime" title="brain-prime game" width="200" /></a>
