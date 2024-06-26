import { useEffect, useState } from 'react'

export default function TopicSelector({ setSelectedTopicList, selectedTopicsList }) {

  const [topics, setTopics] = useState([])

  async function fetchTopics() {
    const response = await fetch('http://127.0.0.1:8000/topics')
    if (response.ok) {
      const topicsData = await response.json()
      setTopics(topicsData)

      // Инициализировать выбранные темы на основе полученных данных
      const allTopicIds = topicsData.flatMap(topic => [topic.id, ...getChildTopicIds(topic)])
      setSelectedTopicList(allTopicIds)
    }
  }

  useEffect(() => {
    fetchTopics()
  }, [])

  function getChildTopicIds(topic) {
    if (!topic.children) return []
    return topic.children.flatMap(child => [child.id, ...getChildTopicIds(child)])
  }

  function handleCheckboxChange(event, topic) {
    const isChecked = event.target.checked
    const allTopicIds = [topic.id, ...getChildTopicIds(topic)]

    if (isChecked) {
      setSelectedTopicList(prev => [...new Set([...prev, ...allTopicIds])])
    } else {
      setSelectedTopicList(prev => prev.filter(id => !allTopicIds.includes(id)))
    }
  }

  function TopicItem({ topic }) {
    return (
      <>
        <div className="AddSobesModal-topicSelector-item">
          <input 
            type="checkbox" 
            id={topic.id} 
            name="topic" 
            checked={selectedTopicsList.includes(topic.id)} 
            onChange={(e) => handleCheckboxChange(e, topic)} 
          />
          <label htmlFor={topic.id}>{topic.name}</label>
        </div>

        {topic.children && topic.children.map((child) => (
          <TopicItem key={child.id} topic={child} />
        ))}
      </>
    )
  }

  function renderTopics() {
    return (
      <div className="AddSobesModal-topicSelector-container">
        {topics.map((topic) => (
          <TopicItem key={topic.id} topic={topic} />
        ))}
      </div>
    )
  }

  return (
    <div>
      {renderTopics()}
    </div>
  )
}




