import { useEffect, useState } from 'react'

import QuestionModal from './modals/QuestionInfo' 
import EditQuestionModal from './modals/EditQuestion'
import EditTopicModal from './modals/EditTopic'
import AddItemModal from './modals/AddItem/AddItem'
import Message from './../../components/Message'

import './styles/QuestionPage.css'


export default function QuestionPage() {
  const [topics, setTopics] = useState([]) // стейт для данных одной спекции топика
  const [selectedQuestion, setSelectedQuestion] = useState(null) // стейт для выбранного вопроса
  const [selectedTopic, setSelectedTopic] = useState(null)
  const [showQuestionModal, setShowQuestionModal] = useState(false) // модальное окно QuestionInfo
  const [showAddItemModal, setShowAddItemModal] = useState(false)  // модальное окно AddItem
  const [showEditQuestionModal, setShowEditQuestionModal] = useState(false) // модальное окно EditQuestion
  const [showEditTopicModal, setShowEditTopicModal] = useState(false)
  
  // Функция для загрузки данных
  async function fetchTopics() {
    const response = await fetch('http://127.0.0.1:8000/topics')
    if (response.ok) {
      const topicsData = await response.json()
      setTopics(topicsData)
    }
  }

  useEffect(() => {
    fetchTopics()
  }, [])

  const openQuestionModal = (question) => {
    setSelectedQuestion(question)
    setShowQuestionModal(true)
  }

  const closeQuestionModal = () => {
    setShowQuestionModal(false)
    setSelectedQuestion(null)
  }

  const openEditQuestionModal = (question) => {
    setSelectedQuestion(question)
    setShowEditQuestionModal(true)
  }

  const openEditTopicModal = (topic) => {
    setSelectedTopic(topic)
    setShowEditTopicModal(true)
  }

  const closeEditQuestionModal = () => {
    setShowEditQuestionModal(false)
    setSelectedQuestion(null)
  }

  const closeEditTopicModal = () => {
    setShowEditTopicModal(false)
    setSelectedTopic(null)
  }

  const openAddItemModal = () => {
    setShowAddItemModal(true)
  }

  const closeAddItemModal = () => {
    setShowAddItemModal(false)
  }

  function addItemButton() {
    return (
      <a href="#" className="QuestionPage-button-addItem" onClick={
        () => openAddItemModal()}>+</a>
    )
  }

  function editTopicButton( topic ) {
    return (
      <a href="#" className="QuestionPage-button-editTopic" onClick={
        () => openEditTopicModal(topic)}>1</a>
    )
  }

  function editQuestionButton( question) {
    return (
      <a href="#" className="QuestionPage-button-editQuestion" onClick={
        () => openEditQuestionModal(question)}>1</a>
    )
  }

  function questionInfoButton( question) {
    return (
      <a href="#" className="QuestionPage-button-questionInfo" onClick={
        () => openQuestionModal(question)}>
        <pre>{ question.question }</pre>
      </a>
    )
  }

  function TopicItem({ topic }) {
    return (
      <div className="QuestionPage-topicItem">
        <details open>  
          <summary>{topic.name}</summary>
          <ul>
            {topic.children.map((child) => (
              <TopicItem key={child.id} topic={child} />
            ))}

            {topic.questions.map((question) => (
              <QuestionItem key={question.id} question={question} />
            ))}
          </ul>
        </details>
        { editTopicButton(topic) }
      </div>
    )
  }

  function QuestionItem({ question }) {
    return (
      <div className="QuestionPage-questionItem">
        <li className="QuestionPage-question">
          { questionInfoButton(question) }
        </li>
        { editQuestionButton(question) }
      </div>
    );
  }

  function topicList(topics) {
    return (
      <section className="QuestionPage-topicList">
        <ul>
          { topics.map((topic) =>
              <TopicItem key={topic.id} topic={topic} />
          )}
        </ul> 
      </section>
    )
  }

  return (
    <div className="QuestionsPage">
      { topicList(topics) }
      { addItemButton() } 
      { showQuestionModal && <QuestionModal 
        question={selectedQuestion} 
        closeQuestionModal={closeQuestionModal} 
      /> }
      { showEditQuestionModal && <EditQuestionModal 
        question={selectedQuestion} 
        topics={topics} 
        closeEditQuestionModal={closeEditQuestionModal} 
        fetchTopics={fetchTopics}
      /> }
      { showEditTopicModal && <EditTopicModal 
        topic={selectedTopic} 
        topics={topics} 
        closeEditTopicModal={closeEditTopicModal} 
        fetchTopics={fetchTopics}
      />}
      { showAddItemModal && <AddItemModal 
        topics={topics}
        closeAddItemModal={closeAddItemModal}
        fetchTopics={fetchTopics}
      /> }
      {/* { message && <Message message={message} /> } */}
    </div>
  )
}