import { useState, useRef, useEffect} from 'react';

import '../styles/CreateTopic.css'

export default function CreateTopic({ topics }) {
  const [parentTopic, setParentTopic] = useState(null);
  const [nameTopic, setNameTopic] = useState('');
  const parentMenuRef = useRef(null);

  function handleTextareaChange(event) {
    setNameTopic(event.target.value);
  }

  useEffect(() => {
    // Восстанавливаем позицию прокрутки после изменения выбора родительского элемента
    if (parentMenuRef.current) {
      parentMenuRef.current.scrollTop = localStorage.getItem('scrollPosition') || 0;
    }
  }, [parentTopic]);

  function handleInputChange(topicId) {
    setParentTopic(topicId);
    // Сохраняем позицию прокрутки при выборе родительского элемента
    localStorage.setItem('scrollPosition', parentMenuRef.current.scrollTop);
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
            onChange={handleTextareaChange}
          />
        </div>
      </>
    )
  }

  function createTopicButton() {
    return (
      <a href="#" className="createItem-button">Создать тему</a>
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



