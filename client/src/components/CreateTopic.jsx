import { useState, useRef, useEffect} from 'react';

import '../styles/CreateTopic.css'

export default function CreateTopic({ topics }) {
  const [parentTopic, setParentTopic] = useState(null);
  const parentMenuRef = useRef(null);

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
      <ul>
        <li>
          <input 
            type="radio" 
            id={topic.id} 
            name="parent" 
            onChange={() => handleInputChange(topic.id)} 
            checked={parentTopic === topic.id}
          />
          <label htmlFor={topic.id}>{topic.name}</label>
        </li>
        {topic.children.map((child) => (
          <ParentMenuTree key={child.id} topic={child} />
        ))}
      </ul>
    );
  }

  function ParentMenu({ topics }) {
    return (
      <div className="select-parent" ref={parentMenuRef}>
        <input 
          type="radio" 
          id="null" 
          name="parent" 
          onChange={() => handleInputChange(null)} 
          checked={parentTopic === null}
        />
        <label htmlFor="null">...</label>
        <div className="select-parent-loaded">
          {topics.map((topic) => (
            <ParentMenuTree key={topic.id} topic={topic} />
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="addItem-selected-content">
      <ParentMenu topics={topics} />
    </div>
  );
}



