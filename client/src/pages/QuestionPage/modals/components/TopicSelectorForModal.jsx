import { useState, useRef, useEffect } from 'react';

export default function TopicSelectorForModal({ topics, nullSelect, parentTopic, setParentTopic, className }) {
  const parentMenuRef = useRef(null);

  useEffect(() => {
    if (parentMenuRef.current) { // Восстанавливаем позицию прокрутки после изменения выбора родительского элемента
      parentMenuRef.current.scrollTop = localStorage.getItem('scrollPosition') || 0;
    }
  }, [parentTopic]);

  function handleInputChange(topicId) {
    setParentTopic(topicId);
    localStorage.setItem('scrollPosition', parentMenuRef.current.scrollTop); // Сохраняем позицию прокрутки при выборе родительского элемента
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
  
        { topic.children.map((child) => (
          <ParentMenuTree key={child.id} topic={child} />
        ))}
      </>
    )
  }

  function renderNullOption() {
    return (
      <>
        <input 
          type="radio" 
          id="null" 
          name="parent" 
          onChange={() => handleInputChange(null)} 
          checked={parentTopic === null} 
        /> 
        <label htmlFor="null">...</label>
      </>
    );
  }


  return (
    <>
      <p>Выберите родительскую тему:</p>
      <div className={className} ref={parentMenuRef}>
        { nullSelect && renderNullOption() }
        { topics.map((topic) => (
          <ParentMenuTree key={topic.id} topic={topic} />
        ))}
      </div>
    </>
  )
}