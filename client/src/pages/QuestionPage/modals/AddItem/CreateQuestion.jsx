import { useState } from 'react';
import TopicSelectorForModal from '../../components/TopicSelectorForModal';

import '../../styles/CreateQuestion.css'

export default function CreateQuestionComponent({ topics }) {
  const [questionName, setQuestionName] = useState('');
  const [answerName, setAnswerName] = useState('');
  const [parentTopic, setParentTopic] = useState(null);

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
      <TopicSelectorForModal 
        topics={topics}
        nullSelect={false}
        parentTopic={parentTopic} 
        setParentTopic={setParentTopic} 
        className="select-parent-for-question"
      />
      { textAreaQuestionName() }
      { textAreaAnswerName() }
      { createQuestionButton() }
    </div>
  );
}