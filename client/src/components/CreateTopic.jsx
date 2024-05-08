import { useState, useRef, useEffect} from 'react';

import '../styles/CreateTopic.css'

export default function CreateTopicComponent({ topics }) {
  const [parentTopic, setParentTopic] = useState(null); // parent_id
  const [nameTopic, setNameTopic] = useState(''); // topic_name
  const parentMenuRef = useRef(null); // для сохранения состояния прокрутки при выборе элемента из селектора

  useEffect(() => {
    if (parentMenuRef.current) { // Восстанавливаем позицию прокрутки после изменения выбора родительского элемента
      parentMenuRef.current.scrollTop = localStorage.getItem('scrollPosition') || 0;
    }
  }, [parentTopic]);

  function handleInputChange(topicId) {
    setParentTopic(topicId);
    localStorage.setItem('scrollPosition', parentMenuRef.current.scrollTop); // Сохраняем позицию прокрутки при выборе родительского элемента
  }

  // Функция для отправки POST запроса
  async function createTopic() {
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

  function ParentMenuTree({ topic }) {
    return (
      <>
        <input 
          type="radio" 
          id={topic.id} 
          name="parent" 
          onChange={() => handleInputChange(topic.id)} 
          checked={parentTopic === topic.id}
        />
        <label htmlFor={topic.id}>{topic.name}</label>

        {topic.children.map((child) => (
          <ParentMenuTree key={child.id} topic={child} />
        ))}
      </>
    )
  }

  function ParentMenu({ topics }) {
    return (
      <>
        <p>Выберите родительскую тему:</p>
        <div className="select-parent" ref={parentMenuRef}>
          <input 
            type="radio" 
            id="null" 
            name="parent" 
            onChange={() => handleInputChange(null)} 
            checked={parentTopic === null}
          />
          <label htmlFor="null">...</label>

          {topics.map((topic) => (
            <ParentMenuTree key={topic.id} topic={topic} />
          ))}
        </div>
      </>
    )
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
      <ParentMenu topics={topics} />
      {textAreaTopicName()}
      {createTopicButton()}
    </div>
  );
}



