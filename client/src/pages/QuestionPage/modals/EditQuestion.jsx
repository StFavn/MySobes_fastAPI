import { useState } from 'react'
import TopicSelectorForModal from '../../components/TopicSelectorForModal';

import '../styles/modals/EditQuestion.css'

export default function EditQuestionModal({ question, topics, closeEditQuestionModal }) {
  const [questionName, setQuestionName] = useState(question.question);
  const [answerName, setAnswerName] = useState(question.answer);
  const [parentTopic, setParentTopic] = useState(question.topic_id);

  async function editQuestion() {
    if (!questionName) { console.log('Введите вопрос') }
    if (!answerName) { console.log('Введите ответ') }
    if (!parentTopic) { console.log('Выберите тему') }

    if (questionName && answerName && parentTopic) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/questions/${question.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ 
            'question': questionName,
            'answer': answerName,
            'topic_id': parentTopic })
        })

        if (response.ok) {
          console.log('Вопрос успешно изменен!');
        } else {
          console.error('Ошибка при изменении вопроса');
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

  function submitQuestionButton() {
    return (
      <a href="#" className="editQuestion-button" onClick={editQuestion}>Сохранить</a>
    )
  }

  function closeEditQuestionModal() {
    setQuestionName(question.question);
    setAnswerName(question.answer);
    setParentTopic(question.topic_id);
    closeEditQuestionModal();
  }

  return(
    <div className="editQuestion-modal">
      <p>Редактировать вопрос</p>
      <TopicSelectorForModal 
        topics={topics}
        nullSelect={false}
        parentTopic={parentTopic} 
        setParentTopic={setParentTopic} 
        className="select-parent-for-question"
      />
      { textAreaQuestionName() }
      { textAreaAnswerName() }
      { submitQuestionButton() }
      <a href="#" className="editQuestion-button" onClick={closeEditQuestionModal}>Отменить</a>
    </div>
  )
}