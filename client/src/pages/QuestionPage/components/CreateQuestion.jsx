import { useState, useRef, useEffect} from 'react';

import '../styles/CreateQuestion.css'

export default function CreateQuestionComponent({ topics }) {
  const [questionName, setQuestionName] = useState('');
  const [answerName, setAnswerName] = useState('');
  const [parentTopic, setParentTopic] = useState(null);
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

  async function createQuestion() {
    if (!questionName) { console.log('Введите вопрос') }
    if (!answerName) { console.log('Введите ответ') }
    if (!parentTopic) { console.log('Выберите тему') }

    if (questionName && answerName && parentTopic) {
      try {
        const response = await fetch('http://127.0.0.1:8000/questions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ 
            'question': questionName,
            'answer': answerName,
            'topic_id': parentTopic })
        })

        if (response.ok) {
          console.log('Вопрос успешно создан!');
        } else {
          console.error('Ошибка при создании вопроса');
        }
      } catch (error) {
        console.error('Произошла ошибка:', error);
      }
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
        <div className="select-parent-for-question" ref={parentMenuRef}>
          {topics.map((topic) => (
            <ParentMenuTree key={topic.id} topic={topic} />
          ))}
        </div>
      </>
    )
  }

  function textAreaQuestionName() {
    return (
      <>
        <p>Укажите текст вопроса:</p>
        <div className="questionName-input">
          <textarea 
            placeholder="Введите текст"
            value={questionName}
            onChange={(event) => setQuestionName(event.target.value)}
          />
        </div>
      </>
    )
  }

  function textAreaAnswerName() {
    return (
      <>
        <p>Укажите текст ответа:</p>
        <div className="answerName-input">
          <textarea 
            placeholder="Введите текст"
            value={answerName}
            onChange={(event) => setAnswerName(event.target.value)}
          />
        </div>
      </>      
    )
  }

  function createQuestionButton() {
    return (
      <a href="#" className="createItem-button" onClick={createQuestion}>Создать вопрос</a>
    )
  }

  return (
    <div className="addItem-selected-content">
      <ParentMenu topics={topics} />
      { textAreaQuestionName() }
      { textAreaAnswerName() }
      { createQuestionButton() }
    </div>
  );
}