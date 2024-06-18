import pytest


@pytest.mark.asyncio
async def test_preload_data(client):
    """Создание данных для тестирования."""

    data_topics = [
        {
            'name': 'Тестовая тема 1'
        },
        {
            'name': 'Тестовая тема 2'
        },
        {
            'name': 'Тестовая тема 3'
        }
    ]

    data_questions = [
        {
            'question': 'Вопрос 1.1',
            'answer': 'Тестовый ответ 1',
            'topic_id': 1
        },
        {
            'question': 'Вопрос 1.2',
            'answer': 'Тестовый ответ 2',
            'topic_id': 1
        },
        {
            'question': 'Вопрос 1.3',
            'answer': 'Тестовый ответ 3',
            'topic_id': 1
        },
        
        {
            'question': 'Вопрос 2.1',
            'answer': 'Тестовый ответ 1',
            'topic_id': 2
        },
        {
            'question': 'Вопрос 2.2',
            'answer': 'Тестовый ответ 2',
            'topic_id': 2
        },
        {
            'question': 'Вопрос 2.3',
            'answer': 'Тестовый ответ 3',
            'topic_id': 2
        },

        {
            'question': 'Вопрос 3.1',
            'answer': 'Тестовый ответ 1',
            'topic_id': 3
        }
    ]

    for data_topic in data_topics:
        response = await client.post('/topics', json=data_topic)
        assert response.status_code == 200

    for data_question in data_questions:
        response = await client.post('/questions', json=data_question)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_sobes(client):
    """Проверка получения списка собесов."""

    sobes_data = {
        'topic_id_list': [1, 2],
        'count_questions': 6
    }
    response = await client.post('/sobeses', json=sobes_data)
    assert response.status_code == 200
    assert response.json()['count_questions'] == 6
    assert len(response.json()['questions']) == 6

    questions = []
    for question in response.json()['questions']:
        questions.append(question['question'])
    assert 'Вопрос 3.1' not in questions


@pytest.mark.asyncio
async def test_get_sobes(client):
    """Проверка получения списка собесов."""

    response_sobeses = await client.get('/sobeses')
    assert response_sobeses.status_code == 200
    assert response_sobeses.json()[0]['count_questions'] == 6

    response_sobes = await client.get('/sobeses/1')
    assert response_sobes.status_code == 200
    assert response_sobes.json()['count_questions'] == 6

    response_sobes_questions = await client.get('/sobes_questions/sobes/1')
    assert response_sobes_questions.status_code == 200
    assert len(response_sobes_questions.json()) == 6

    response_sobes_question = await client.get('/sobes_questions/1')
    assert response_sobes_question.status_code == 200
    assert response_sobes_question.json()['sobes_id'] == 1


@pytest.mark.asyncio
async def test_patch_sobes_question(client):
    """Проверка редактирования sobes_question."""

    sobes_question_data = {
        'user_answer': 'Тестовый ответ',
        'duration': 500,
        'score': 10,
        'description': 'Тестовое описание'
    }

    response_sobes_question = await client.patch('/sobes_questions/1', json=sobes_question_data)
    assert response_sobes_question.status_code == 200
    assert response_sobes_question.json()['user_answer'] == 'Тестовый ответ'

    sobes_question_data = {
        'user_answer': 'Тестовый ответ',
        'duration': 500,
        'score': 0,
        'description': 'Тестовое описание'
    }
    response_sobes_question = await client.patch('/sobes_questions/2', json=sobes_question_data)
    assert response_sobes_question.status_code == 200
    assert response_sobes_question.json()['user_answer'] == 'Тестовый ответ'

@pytest.mark.asyncio
async def test_patch_sobes(client):
    """Проверка редактирования sobes."""

    sobes_data = {
        'status': 'done'
    }

    response_sobes = await client.patch('/sobeses/1', json=sobes_data)
    assert response_sobes.status_code == 200
    # assert response_sobes.json()['status'] == 'done'



@pytest.mark.asyncio
async def test_recalculate_score(client):
    """Проверка перерасчета собеса."""

    response_recalculate = await client.post('/sobeses/1/recalculate_score')
    assert response_recalculate.status_code == 200
    assert response_recalculate.json()['average_score'] == 5
    assert response_recalculate.json()['duration'] == 1000


@pytest.mark.asyncio
async def test_delete_sobes(client):
    """Проверка удаления собеса."""

    response_delete = await client.delete('/sobeses/1')
    assert response_delete.status_code == 200

    response_sobeses_404 = await client.get('/sobeses')
    assert response_sobeses_404.status_code == 404

    response_sobes_questions_404 = await client.get('/sobes_questions/sobes/1')
    assert response_sobes_questions_404.status_code == 404


@pytest.mark.asyncio
async def test_finaly_clean_data(client):
    """Проверка очистки данных."""

    response = await client.get('/topics')
    assert response.status_code == 200

    for topic in response.json():
        response = await client.delete('/topics/' + str(topic['id']))
        assert response.status_code == 200
    
    response_topic_404 = await client.get('/topics')
    assert response_topic_404.status_code == 404

    response_question_404 = await client.get('/questions')
    assert response_question_404.status_code == 404

    response_sobeses_404 = await client.get('/sobeses')
    assert response_sobeses_404.status_code == 404
