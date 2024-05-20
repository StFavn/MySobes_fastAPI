import { useEffect, useState } from 'react'
import QuestionModal from '../modals/QuestionInfo' 
import AddItemModal from '../modals/AddItem/AddItem'
import Message from '../../../components/Message'

import '../styles/TopicTree.css'


export default function TopicsSection() {
    const [loading, setLoading] = useState(false) // стейт для загрузки данных
    const [topics, setTopics] = useState([]) // стейт для данных одной спекции топика
    const [showQuestionModal, setShowQuestionModal] = useState(false);
    const [selectedQuestion, setSelectedQuestion] = useState(null);
    const [showAddItemModal, setShowAddItemModal] = useState(false);

  // Функция для загрузки данных
  async function fetchTopics() {
    setLoading(true)
    const response = await fetch('http://127.0.0.1:8000/topics')
    const topicsData = await response.json()
    setTopics(topicsData)
    setLoading(false)
  }

  useEffect(() => {  // функция запускающая загрузку данных
      fetchTopics()
  }, [])

  const openQuestionModal = (question) => {
    setSelectedQuestion(question);
    setShowQuestionModal(true);
  }

  const closeQuestionModal = () => {
    setShowQuestionModal(false);
    setSelectedQuestion(null);
  }

  const openAddItemModal = () => {
    setShowAddItemModal(true);
  }

  const closeAddItemModal = () => {
    setShowAddItemModal(false);
  }

  function addItem() {
    return (
      <a href="#" className="add-item-button" onClick={() => openAddItemModal()}>+</a>
    )
  }

  // Нужно добавить сохранение состояния открытости details
  function TopicTree({ topic }) {
    return (
      <details open>
        <summary>{topic.name}</summary>
        <ul>
          {topic.children.map((child) => (
              <TopicTree key={child.id} topic={child} />
          ))}

          {topic.questions.map((question) => 
            <span key={question.id}>
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

  function returnTopicList(topics) {
    return (
      <section className="tree">
        <div>
          <ul>
            { topics.map((topic) =>
                <TopicTree key={topic.id} topic={topic} />
            )}
          </ul> 
        </div>
      </section>
    )
  }

  return (
    <>
      { loading && <p>Загрузка...</p> }
      { !loading && returnTopicList(topics) }
      { addItem() } 
      {showQuestionModal && <QuestionModal question={selectedQuestion} closeQuestionModal={closeQuestionModal} />}
      {showAddItemModal && <AddItemModal topics={topics} closeAddItemModal={closeAddItemModal} />}
      { Message('тестовое сообщени') }
    </>
  )
}