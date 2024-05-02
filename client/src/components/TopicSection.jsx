import { useEffect, useState } from 'react'
import '../styles/TopicTree.css'

export default function TopicsSection() {
    const [loading, setLoading] = useState(false) // стейт для загрузки данных
    const [topics, setTopics] = useState([]) // стейт для данных одной спекции топика
    // const [hoveredItem, setHoveredItem] = useState(null) // стейт для ховер эффекта(наведение мыши на топик)

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

  function TopicTree({ topic }) {
    return (
      // <details open={isOpen} onClick={toggleAccordion}>
      <details>
        <summary>{topic.name}</summary>
        <ul>
          {topic.children.map((child) => (
              <TopicTree key={child.id} topic={child} />
          ))}

          {topic.questions.map((question) => 
            <li className="tree-question">{question.question}</li>
          )}
        </ul>
      </details>
    )
  }

  return (
    <section className="tree">
      { loading && <p>Загрузка...</p> }
      { !loading && 
        <ul>
          <li>
            { topics.map((topic) =>
                <TopicTree key={topic.id} topic={topic} />
            )}
          </li>
        </ul> 
      }
    </section>
  )
}
// <li> я добавил только для того, чтобы был фон. Возможно это тупо