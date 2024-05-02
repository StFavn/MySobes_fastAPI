import { useEffect, useState } from 'react'
import './styles/tree.css'

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
      <li>
        <details>
          <summary>{topic.name}</summary>
          <ul>
            {topic.children.map((child) => (
              <TopicTree key={child.id} topic={child} />
            ))}

            {topic.questions.map((question) => 
              <li>{question.question}</li>
            )}
          </ul>
        </details>
      </li>
    )
  }

  return (
    <section>
      { loading && <p>Загрузка...</p> }
      { !loading && 
        <ul className="tree">
          { topics.map((topic) =>
            <TopicTree key={topic.id} topic={topic} />
          )}
        </ul> 
      }
    </section>
  )
}


  // function formatTopics(topics, level = 0) {
  //   let formattedTopics = [];
  //   for (const topic of topics) {
  //     formattedTopics.push({
  //       // id: topic.id,
  //       // parent_id: topic.parent_id,
  //       // name: topic.name,
  //       ...topic,
  //       level: level
  //     });
  //     if (topic.children && topic.children.length > 0) {
  //         formattedTopics = formattedTopics.concat(formatTopics(topic.children, level + 1));
  //     }
  //   }
  //   return formattedTopics;
  // }

  // function renderTopics(topics) {
  //   return (
  //     <ul>
  //       {topics.map((topic) => (
  //         <li key={topic.name} style={{ paddingLeft: `${topic.level * 20}px` }}>
  //           {topic.name}
  //         </li>
  //       ))}
  //     </ul>
  //   );
  // }