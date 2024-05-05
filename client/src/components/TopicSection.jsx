import { useEffect, useState } from 'react'
import '../styles/TopicTree.css'

export default function TopicsSection() {
    const [loading, setLoading] = useState(false) // стейт для загрузки данных
    const [topics, setTopics] = useState([]) // стейт для данных одной спекции топика
    const [showQuestionModal, setShowQuestionModal] = useState(false);
    const [selectedQuestion, setSelectedQuestion] = useState(null);

  // Функция для загрузки данных
  async function fetchTopics() {
    setLoading(true)
    const response = await fetch('http://127.0.0.1:8000/topics')
    const topicsData = await response.json()
    setTopics(topicsData)
    setLoading(false)
  }

  // функция запускающая загрузку данных
  useEffect(() => {
      fetchTopics()
  }, [])

  const openQuestionModal = (question) => {
    setSelectedQuestion(question);
    setShowQuestionModal(true);
  };

  const closeQuestionModal = () => {
    setShowQuestionModal(false);
    setSelectedQuestion(null);
  };

  function QuestionModal({ question, closeQuestionModal }) {
    return (
      <div className="question-modal">
        <div className="question-modal-content">
          <a  href="#" className="close-question-modal-button" onClick={closeQuestionModal}>&times;</a>
          <p>Вопрос: {question.question}</p>
          <p>Ответ: {question.answer}</p>
        </div>
      </div>
    );
  }

  function TopicTree({ topic }) {
    return (
      <details open>
        <summary>{topic.name}</summary>
        <ul>
          {topic.children.map((child) => (
              <TopicTree key={child.id} topic={child} />
          ))}

          {topic.questions.map((question) => 
            <span>
              <li key={question.id}>
                <a href="#" className="question" onClick={() => openQuestionModal(question)}>
                  {question.question}
                </a>
              </li>
              <a href="#" className="edit-question-button">1</a>
            </span>
          )}
        </ul>
      </details>
    )
  }

  function returnTopicList() {
    return (
      <section className="tree">
        <dir>
          { loading && <p>Загрузка...</p> }
          { !loading && 
            <ul>
              { topics.map((topic) =>
                  <TopicTree key={topic.id} topic={topic} />
              )}
            </ul> 
          }
        </dir>
        {showQuestionModal && <QuestionModal question={selectedQuestion} closeQuestionModal={closeQuestionModal} />}
      </section>
    )
  }

  return (
    returnTopicList()
  )
}
// <li> я добавил только для того, чтобы был фон. Возможно это тупо