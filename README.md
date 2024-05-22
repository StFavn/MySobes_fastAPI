# MySobes_fastAPI

### Описание:

Очередная моя попытка создать приложение для собственного использования. Это приложение, где вы можете создать список открытых вопросов и затем попробовать пройти тестирование по этим вопросам.

### Серверная часть

Фреймворк fastAPI  
Запуск приложения через  main.py  
команда запуска: `uvicorn main:app --reload`

### Клиентская часть

Написана на React  
Запуск клиентской части: `npm run dev`

### Использование

1. Скачиваем репозиторий
2. Устанавливаем python3.10
3. Устанавливаем node и npm  
```
sudo apt update
sudo apt install nodejs
sudo apt install npm
```
Обновляем nvm до версии 21.6.2 
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```
```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```
```bash
nvm install 21.6.2
```
4. Запускаем клиент-сервер
```
cd client -> npm run dev
```
5. В папке проекта создаем виртуальное окружение: `python3.10 -m venv venv`
6. Активируем виртуальную среду: `source venv/bin/activate`
7. Устанавливаем зависимости: `pip install -r requirements.txt`
8. Переходим в директорию server `cd server`
9. Накатываем миграции `alembic upgrade head`
10. Запускаем сервер: `uvicorn main:app --reload`


---

## Дневник разработчика

### TODO server

- Написать тесты API компонентов
- Добавить авторизацию/аутентификацию
- Таблица собес-контейнера
- Добавить функцию сборки собес-контейнера


### TODO client:

- ~~Настроить отображение тем и вопросов в виде дерева~~
- ~~Настроить подсветку при наведении мыши~~ (как оказалось, это делается просто в css)
- Стили модального окна QuestionInfo
- Стили edit окна
- Стили и функционал  для message
- Страница списка собес контейнеров
- Страница оценки результатов + отправка результатов на сервер
- Страница просмотра результатов
- Отложено:
  - Страница Экзамена + таймер
  - \*настроить анимацию details(Сложная задача со звездочкой) https://css-tricks.com/how-to-animate-the-details-element/

### Просто идеи

Есть еще идея при изменении вопроса создавать просто новую версию этого вопроса и сохранять историю изменений этого вопроса.
Также у каждого вопроса будет средний показатель успешности ответа на этот вопрос. При изменении вопроса, последняя версия будет отображаться в общем списке. При нажатии на вопрос будет отображаться страница

Появилась идея, добавить к вопросам дополнительные "направляющие вопросы" которые могут быть подсказками во время экзамена. Для этого нужно создать дополнительную таблицу (id, question_id, sub_question - один ко многим).  
Еще вопрос, стоит ли при запросе /topics отправлять к списко вопросов answer? Мне кажется лучше будет, если все доп вопросы и answer клиент будет запрашивать в момент нажатия на вопрос из списка.

Определенно, в моем приложении будет поддержка markdown! тем более я выяснил, что на react это делается просто.

## Короче ближайшие задачи:

- ~~Добавить возможность с фронта создавать тему и вопрос~~ (07-... .10.24)
- ~~Добавить возможность редактировать вопрос и тему~~ (23.05.24)
- Добавить авторизацию/футентификацию
- Начать работу над Sobes-контейнерами

---

- Написать функцию сборки собесов + таблицу для таких контейнеров
- Отображение списка контейнеров и статусов
- Страница экзамена
- Отправка результатов тестирования на сервер
- Завернуть в докер и задеплоить
- написать все тоже самое на elixir

---

## История коммитов

**Коммит от 05.05.24:**

- Добавил на фронтенде кнопки для вывода модального окна вопроса и кнопку редактирования справа от вопроса. Подредачил немного стили, стало красивее.

**Коммиты от 06.05.24:**

- Настроил миграции.
- Сделал поле topic_id обязательным для таблицы question
- Добавил код 404 для get_by_id
- Начал работать над клиентской возможностью добавлять вопрос или тему. Идея: создать модальное окно с селектом "создать тему" или "создать вопрос"

**Коммит от 07.05.24:**

- Настроил стиль модального окна AddItem
- Настроил селектор (создать тему или создать вопрос) чтобы он выглядел красиво
  _(На самом деле работа с клиентской стороной отнимает много времени, я попробую так не заморачиваться со стилем и постараюсь поскорее закончить с функцией создания темы и создания вопроса. Но все-таки нужно корректно отображать дерево тем для выбора parent темы вопроса или подтемы, это скорее всего отнимет много времени, возможно весь день 08.05.24. И это стремно капец)_

**Коммиты от 08.05.24:**

- Настроил отображение селектора родительских тем в CreateTopic.jsx. Но не получилось адеватно настроить стили отображения дерева в селекторе. Я скорее всего оставлю так и перейду к следующей задаче.
- Почти настроил отображение остальных элементов для CreateTopic.jsx
- Настроил корректный прием данных POST запроса на сервер.
- Почти закончил со стилями CreateTopicComponent. Осталось только отображать пользователю, что тема была создана успешно и отчищать поле ввода названия темы.  

**10.05.24**

- Закончил с версткой и функциональной частьюсоздания тем и вопросов.
  _Появилось ощущение, что верстать и писать функционал на фронтенде - это просто болото, от которого нужно уже отказываться. Я вдруг понял, как много важных задач лежит на бэкенде. Да и кроме того, я ведь хотел еще сделать все тоже самое на elixir._
  _Думаю, мне уже хватит работать со стилями. На клиенте сосредоточусь чисто на функционале и отдам преоритет бекенду_

**23.05.24**

- Добавил edit и delete функционал для вопросов и тем
