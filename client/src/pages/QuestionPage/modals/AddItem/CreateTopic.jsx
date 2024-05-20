import { useState } from 'react';
import TopicSelectorForModal from '../../components/TopicSelectorForModal';

import '../../styles/CreateTopic.css'

export default function CreateTopicComponent({ topics }) {
  const [parentTopic, setParentTopic] = useState(null); // parent_id
  const [nameTopic, setNameTopic] = useState(''); // topic_name

  async function createTopic() {
    if (!nameTopic) { console.log('Введите название темы') }

    if (nameTopic !== '') {
      try {
        const response = await fetch('http://127.0.0.1:8000/topics', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ 
            'name': nameTopic,
            'parent_id': parentTopic })
        });

        if (response.ok) {
          console.log('Тема успешно создана!');
        } else {
          console.error('Ошибка при создании темы');
        }
      } catch (error) {
        console.error('Произошла ошибка:', error);
      }
    } else {
      console.log('Пожалуйста, введите название темы');
    }
  }

  function textAreaTopicName() {
    return (
      <>
        <p>Укажите название темы:</p>
        <div className="topicName-input">
          <textarea 
            placeholder="Введите текст"
            value={nameTopic}
            onChange={(event) => setNameTopic(event.target.value)}
          />
        </div>
      </>
    )
  }

  function createTopicButton() {
    return (
      <a href="#" className="createItem-button" onClick={createTopic}>Создать тему</a>
    )
  }

  return (
    <div className="addItem-selected-content">
      <TopicSelectorForModal 
        topics={topics} 
        nullSelect={true}
        parentTopic={parentTopic} 
        setParentTopic={setParentTopic}
        className={'select-parent'}
      />
      { textAreaTopicName() }
      { createTopicButton() }
    </div>
  );
}



