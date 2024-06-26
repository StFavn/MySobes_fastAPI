import '../../styles/modals/AddSobesModal.css'

import { useState } from 'react'

import TopicSelector from './topicSelector'

export default function AddSobesModal({ closeAddSobesModal, fetchSobeses }) {
  const [selectedTopicList, setSelectedTopicList] = useState([])
  const [questionCount, setQuestionCount] = useState(1)

  async function createSobes() {
    console.log('Список выбранных тем', selectedTopicList);
    console.log('Кол-во вопросов', questionCount);
    if (selectedTopicList && questionCount) {
      try {
        const response = await fetch('http://127.0.0.1:8000/sobeses', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          }, 
          body: JSON.stringify({ 
            'topic_id_list': selectedTopicList,
            'count_questions': questionCount
          })
        })

        if (response.ok) {
          console.log('Собес успешно создан!');
          fetchSobeses()
        } else {
          console.error('Ошибка при создании Собеса');
        }
      } catch (error) {
        console.error('Произошла ошибка:', error);
      }
    }
  }

  function inputCountQuestions() {
    return (
      <input
        className='AddSobesModal-input-countQuestions'
        type="number"
        placeholder="Кол-во вопросов"
        value={questionCount}
        onChange={(event) => setQuestionCount(event.target.value)}
      />
    )
  }

  function closeAddSobesModalButton() {
    return (
      <a href='#' className='AddSobesModal-button-close' onClick={closeAddSobesModal}>&times;</a>
    )
  }

  function submitAddSobesButton() {
    return (
      <a href='#' className='AddSobesModal-button-submit' onClick={createSobes}>Сохранить</a>
    )
  }
  
  return (
    <div className="AddSobesModal-modal">
      <div className="AddSobesModal-content">
        <TopicSelector 
          setSelectedTopicList={setSelectedTopicList} 
          selectedTopicsList={selectedTopicList} 
        />

        { inputCountQuestions() }
        { closeAddSobesModalButton() }
        { submitAddSobesButton() }
      </div>
    </div>
  )
}