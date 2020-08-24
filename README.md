# Simple auto-generated ResNet

Архитектура ResNet достаточно гибкая и имеет большое количество различных мета-параметров. Поэтому реализации этой архитектуры, сохраняющие всю ее гибкость, большие и сложные. Кроме того, при фиксированных мета-параметрах, примерно 70% кода такой реализации никогда не используются. Однако просто убрать все что не используется - не вариант, так как тогда не будет возможности изменять мета-параметры.

Данный проект предоставляет инструменты, которые существенно упрощают код реализации, при этом не теряя гибкость архитектуры.

## Как это работает?

Для выполнения данной задачи предлагается использовать промежуточный скрипт, который принимает набор мета-параметров и на их основе генерирует код для даного ResNet. Таким образом, сгенерированный файл содержит только минимальное необходимое для работы сети с указанными мета-параметрами.

Пример сгенерированного файла: `resnet_example.py`

## Как использовать в своем проекте?

1. Клонируем репозиторий
2. Открываем файл `build.py`, указываем желаемые параметры и запускаем этот файл.
3. Созданный файл `resnet.py` копируем в папку с Вашим проектом
4. Если при генерации вы указали `test_only=False`, то так же нужно будет скопировать файлы `libs/conv_wrapper.py` и `libs/freeze_batchnorm.py`
5. Написать создание сети и ее запуск (в качестве примера, см. `main.py`)
