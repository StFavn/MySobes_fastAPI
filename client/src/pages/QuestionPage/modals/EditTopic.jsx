import { useState } from 'react'
import TopicSelectorForModal from './components/TopicSelectorForModal';

import '../styles/modals/EditTopic.css'

export default function EditTopicModal({ topic, topics, closeEditTopicModal, fetchTopics }) {
  const [topicName, setTopicName] = useState(topic.name);
  const [parentTopic, setParentTopic] = useState(topic.parent_id);

  async function editTopic() {
    if (!topicName) { console.log('Название темы') }
    if (!parentTopic) { console.log('Выберите тему') }

    if (topicName && parentTopic) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/topics/${topic.id}`, {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ 
            'name': topicName,
            'parent_id': parentTopic
          })
        });

        if (response.ok) {
          console.log('Тема успешно изменена!');
          fetchTopics();
        } else {
          console.error('Ошибка при изменении темы');
        }
      } catch (error) {
        console.error('Произошла ошибка:', error);
      }
    }
  }

  async function deleteTopic() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/topics/${topic.id}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        console.log('Тема успешно удалена!');
        fetchTopics();
        close();
      } else {
        console.error('Ошибка при удалении темы');
      }
    } catch (error) {
      console.error('Произошла ошибка:', error);
    }
  }

  function textAreaTopicName() {
    return (
      <>
        <p>Укажите название темы:</p>
        <div className="topicName-input">
          <textarea 
            placeholder="Название темы"
            value={topicName}
            onChange={(event) => setTopicName(event.target.value)}
          />
        </div>
      </>
    )
  }

  function submitButton() {
    return (
      <a href="#" className="editTopic-button-submit" onClick={editTopic}>Сохранить</a>
    )
  }

  function deleteButton() {
    return (
      <a href="#" className="editTopic-button-delete" onClick={deleteTopic}>Удалить</a>
    )
  }

  function close() {
    setTopicName(topic.name);
    setParentTopic(topic.parent_id);
    closeEditTopicModal();
  }

  function closeEditTopicButton() {
    return (
      <a href="#" className="editTopic-button-close" onClick={close}>&times;</a>
    )
  }

  return (
    <div className="editTopic-modal">
      <div className="editTopic-content">
        <p>Редактировать тему</p>
        <TopicSelectorForModal 
          topics={topics}
          nullSelect={true}
          parentTopic={parentTopic} 
          setParentTopic={setParentTopic} 
          className="select-parent-for-question"
        />
        {textAreaTopicName()}
        {submitButton()}
        {deleteButton()}
        {closeEditTopicButton()}
      </div>
    </div>
  )
}