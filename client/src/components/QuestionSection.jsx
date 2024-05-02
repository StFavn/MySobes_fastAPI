import { useEffect, useState } from 'react'
import './styles/question.css'

export default function QuestionSection() {
  const [loading, setLoading] = useState(false) // стейт для загрузки данных
  const [questions, setQuestions] = useState([]) // стейт для данных одной спекции вопроса
  const [hoveredItem, setHoveredItem] = useState(null) // стейт для ховер эффекта(наведение мыши на вопрос)

  // Функция для загрузки данных
  async function fetchQuestions() {
    setLoading(true)
    const response = await fetch('http://127.0.0.1:8000/questions')
    const questionsData = await response.json()
    setQuestions(questionsData)
    setLoading(false)
  }

  // функция запускающая загрузку данных
  useEffect(() => {
    fetchQuestions()
  }, [])
  
  // Обработчики событий для наведения и ухода мыши
  const handleMouseEnter = (questionId) => {
    setHoveredItem(questionId);
  }

  const handleMouseLeave = () => {
    setHoveredItem(null);
  }

  return (
    <section>
      { loading && <p>Загрузка...</p> }
      { !loading && 
        <ul>
          { questions.map((question) => 
            <li 
              key={question.id}
              onMouseEnter={() => handleMouseEnter(question.id)}
              onMouseLeave={handleMouseLeave}
              className={hoveredItem === question.id ? 'highlighted' : ''}
            >
              { question.question }
            </li> 
          )}
        </ul> 
      }
    </section>
  )
}


      // <ul>
      //   {questions.map((question) => (
      //     <li
      //       key={question.id}
      //       onMouseEnter={() => handleMouseEnter(question.id)}
      //       onMouseLeave={handleMouseLeave}
      //       className={hoveredItem === question.id ? 'highlighted' : ''}
      //     >
      //       {question.question}
      //     </li>
      //   ))}
      // </ul>
