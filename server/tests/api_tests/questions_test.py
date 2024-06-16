import pytest


@pytest.mark.asyncio
async def test_create_question(client):
    """Проверка создания вопроса."""

    data_topic = {
        'name': 'Тестовая тема'
    }
    response = await client.post('/topics', json=data_topic)
    assert response.status_code == 200

    parent_id = response.json()['id']
    data_question = {
        'question': 'Тестовый вопрос 1',
        'answer': 'Ответ для вопроса 1',
        'topic_id': parent_id
    }
    response = await client.post('/questions', json=data_question)
    assert response.status_code == 200
    assert response.json()['question'] == 'Тестовый вопрос 1'


@pytest.mark.asyncio
async def test_get_questions(client):
    """Проверка получения списка вопросов."""

    response = await client.get('/questions')
    assert response.status_code == 200

    # Пока что создана только один вопрос
    assert len(response.json()) == 1
    assert response.json()[0]['question'] == 'Тестовый вопрос 1'


@pytest.mark.asyncio
async def test_get_question(client):
    """Проверка получения конкретного вопроса."""

    response = await client.get('/questions/1')
    assert response.status_code == 200
    assert response.json()['question'] == 'Тестовый вопрос 1'


@pytest.mark.asyncio
async def test_edit_question(client):
    """Проверка редактирования вопроса."""

    data = {
        'question': 'Измененный вопрос 1',
    }
    response_patch = await client.patch('/questions/1', json=data)
    assert response_patch.status_code == 200
    assert response_patch.json()['question'] == 'Измененный вопрос 1'

    response_get = await client.get('/questions/1')
    assert response_get.status_code == 200
    assert response_get.json()['question'] == 'Измененный вопрос 1'


@pytest.mark.asyncio
async def test_get_question_tree(client):
    """Проверка, что дерево тем корректно собирается и в нем присутствует вопрос."""

    response_topics = await client.get('/topics')
    assert response_topics.status_code == 200
    assert response_topics.json()[0]['name'] == 'Тестовая тема'
    assert response_topics.json()[0]['questions'][0]['question'] == 'Измененный вопрос 1'


@pytest.mark.asyncio
async def test_delete_question(client):
    """Проверка удаления вопроса."""

    response_topics = await client.get('/topics')
    assert response_topics.status_code == 200
    parent_id = response_topics.json()[0]['id']

    data_question = {
        'question': 'Вопрос для удаления',
        'answer': 'Ответ для вопроса для удаления',
        'topic_id': parent_id
    }
    response_create = await client.post('/questions', json=data_question)
    assert response_create.status_code == 200
    assert response_create.json()['question'] == 'Вопрос для удаления'
    created_id = response_create.json()['id']

    response = await client.delete(f'/questions/{created_id}')
    assert response.status_code == 200
    assert response.json() == 'Удаление успешно завершено.'

    response_deleted_obj = await client.get(f'/questions/{created_id}')
    assert response_deleted_obj.status_code == 404


@pytest.mark.asyncio
async def test_delete_parent_question(client):
    """
    Проверка удаления родительской темы.
    Вместе с родительской темой должныудаляться все дочерные элементы.
    """

    response_get = await client.get('/topics')
    assert response_get.status_code == 200
    assert response_get.json()[0]['name'] == 'Тестовая тема'
    assert response_get.json()[0]['questions'][0]['question'] == 'Измененный вопрос 1'

    topic_id = response_get.json()[0]['id']
    question_id = response_get.json()[0]['questions'][0]['id']

    response = await client.delete(f'/topics/{topic_id}')
    assert response.status_code == 200
    assert response.json() == 'Удаление успешно завершено.'
    
    response_get_question = await client.get(f'/questions/{question_id}')
    assert response_get_question.status_code == 404


# --- EDGE ---

# TODO: Проверка добавления с отсутствующим question
# TODO: Проверка добавления с отсутствующим answer
# TODO: Проверка добавления с отсутствующим parent_id
# TODO: Проверка добавления с несуществующим parent_id
# TODO: Проверка изменения с несуществующим id
# TODO: Проверка изменения с несуществующим parent_id
# TODO: Проверка изменения с пустым полем question
# TODO: Проверка изменения с пустым полем answer
# TODO: Проверка изменения с пустым полем parent_id
# TODO: Проверка удаления с несуществующим id


@pytest.mark.asyncio
async def test_finaly_questions_tests(client):
    """Проверка, что после окончания тестирования, база данных чиста."""
    response = await client.get('/topics')
    assert response.status_code == 404

    response = await client.get('/questions')
    assert response.status_code == 404

