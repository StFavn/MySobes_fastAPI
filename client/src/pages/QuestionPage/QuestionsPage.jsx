import { useEffect, useState } from 'react'
import QuestionModal from './modals/QuestionInfo' 
import EditQuestionModal from './modals/EditQuestion'
import EditTopicModal from './modals/EditTopic'
import AddItemModal from './modals/AddItem/AddItem'
import Message from './../../components/Message'

import './styles/QuestionPage.css'


export default function QuestionPage() {
  const [topics, setTopics] = useState([]) // стейт для данных одной спекции топика
  const [selectedQuestion, setSelectedQuestion] = useState(null); // стейт для выбранного вопроса
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [showQuestionModal, setShowQuestionModal] = useState(false); // модальное окно QuestionInfo
  const [showAddItemModal, setShowAddItemModal] = useState(false);  // модальное окно AddItem
  const [showEditQuestionModal, setShowEditQuestionModal] = useState(false); // модальное окно EditQuestion
  const [showEditTopicModal, setShowEditTopicModal] = useState(false); 

  // Функция для загрузки данных
  async function fetchTopics() {
    const response = await fetch('http://127.0.0.1:8000/topics')
    if (response.ok) {
      const topicsData = await response.json()
      setTopics(topicsData)
    }
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

  const openEditQuestionModal = (question) => {
    setSelectedQuestion(question);
    setShowEditQuestionModal(true);
  }

  const openEditTopicModal = (topic) => {
    setSelectedTopic(topic);
    setShowEditTopicModal(true);
  }

  const closeEditQuestionModal = () => {
    setShowEditQuestionModal(false);
    setSelectedQuestion(null);
  }

  const closeEditTopicModal = () => {
    setShowEditTopicModal(false);
    setSelectedTopic(null);
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
      <span>
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
                    <pre>{question.question}</pre>
                  </a>
                </li>
                <a href="#" className="edit-question-button" onClick={() => openEditQuestionModal(question)}>1</a>
              </span>
            )}
          </ul>
        </details>
        <a href="#" className="edit-topic-button" onClick={() => openEditTopicModal(topic)}>1</a>
      </span>
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
    <div className="QuestionsPage">
      { returnTopicList(topics) }
      { addItem() } 
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