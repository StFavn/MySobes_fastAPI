import pytest

# --- NORMAL ---

@pytest.mark.asyncio
async def test_create_topic(client):
    """Проверка создания темы."""

    data = {
        'name': 'Тестовая тема'
    }
    response = await client.post('/topics', json=data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_topics(client):
    """Проверка получения списка тем."""

    response = await client.get('/topics')
    assert response.status_code == 200

    # Пока что создана только одна тема с конкретным названием
    assert len(response.json()) == 1
    assert response.json()[0]['name'] == 'Тестовая тема'


@pytest.mark.asyncio
async def test_get_topic(client):
    """Проверка получения конкретной темы."""

    response = await client.get('/topics/1')
    assert response.status_code == 200
    assert response.json()['name'] == 'Тестовая тема'


@pytest.mark.asyncio
async def test_edit_topic(client):
    """Проверка редактирования темы."""

    data = {
        'name': 'Измененная тема'
    }
    response_patch = await client.patch('/topics/1', json=data)
    assert response_patch.status_code == 200
    assert response_patch.json()['name'] == 'Измененная тема'

    response_get = await client.get('/topics/1')
    assert response_get.status_code == 200
    assert response_get.json()['name'] == 'Измененная тема'


@pytest.mark.asyncio
async def test_get_topic_tree(client):
    """Проверка, что дерево тем корректно собирается."""

    children_data = {
        'name': 'Тестовая подтема',
        'parent_id': 1
    }
    response_create = await client.post('/topics', json=children_data)
    assert response_create.status_code == 200
    assert response_create.json()['name'] == children_data['name']

    response = await client.get('/topics')
    assert response.status_code == 200

    # Провер]ем, что не смотря на то, что тем 2, приходит только одна корневая тема
    assert len(response.json()) == 1
    assert response.json()[0]['children'][0]['name'] == children_data['name']


@pytest.mark.asyncio
async def test_delete_topic(client):
    """Проверка удаления темы."""

    data = {
        "name": "Тема для удаления",
    }
    response_create = await client.post('/topics', json=data)
    assert response_create.status_code == 200
    assert response_create.json()['name'] == data['name']

    created_id = response_create.json()['id']
    response = await client.delete(f'/topics/{created_id}')
    assert response.status_code == 200
    assert response.json() == 'Удаление успешно завершено.'

    response_deleted_obj = await client.get(f'/topics/{created_id}')
    assert response_deleted_obj.status_code == 404


@pytest.mark.asyncio
async def test_delete_parent_topic(client):
    """
    Проверка удаления родительской темы.
    Вместе с родительской темой должныудаляться все дочерные элементы.
    """

    response_get = await client.get('/topics')
    assert response_get.status_code == 200
    assert len(response_get.json()) == 1
    assert response_get.json()[0]['name'] == 'Измененная тема'
    assert response_get.json()[0]['children'][0]['name'] == 'Тестовая подтема'

    topic_id = response_get.json()[0]['id']
    children_id = response_get.json()[0]['children'][0]['id']

    response = await client.delete(f'/topics/{topic_id}')
    assert response.status_code == 200
    assert response.json() == 'Удаление успешно завершено.'
    
    response_get_children = await client.get(f'/topics/{children_id}')
    assert response_get_children.status_code == 404

# --- EDGE ---

# TODO: Проверка добавления с отсутствующим name
# TODO: Проверка добавления с несуществующим parent_id
# TODO: Проверка изменения с несуществующим id
# TODO: Проверка изменения с отсутствующим name
# TODO: Проверка изменения с несуществующим parent_id
# TODO: Проверка удаления с несуществующим id

@pytest.mark.asyncio
async def test_finaly_topics_tests(client):
    """Проверка, что после окончания тестирования, база данных чиста."""
    response = await client.get('/topics')
    assert response.status_code == 404