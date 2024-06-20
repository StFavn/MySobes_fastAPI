import { useEffect, useState } from 'react'

import './styles/SobesPage.css'

export default function SobesPage() {
  const [sobeses, setSobeses] = useState([]);

  async function fetchSobeses() {
    const response = await fetch('http://127.0.0.1:8000/sobeses');
    if (response.ok) {
      const sobesesData = await response.json();
      setSobeses(sobesesData);
    }
  }

  useEffect(() => {
    fetchSobeses();
  }, []);

  function sobesTableTitle() {
    return (
      <div className='sobesTable-title'>
        <span className='sobesTable-number'>№</span>
        <span className='sobesTable-datetime'>Дата создания</span>
        <span className='sobesTable-count'>Кол-во вопросов</span>
        <span className='sobesTable-avg'>Средний балл</span>
        <span className='sobesTable-status'>Статус</span>
      </div>
    )
  }

  function SobesContainer({ sobes, index }) {
    return (
      <div className='sobesTable-element'>
        <span className='sobesTable-number'>{ index + 1 }</span>
        <span className='sobesTable-datetime'>{ sobes.create_at }</span>
        <span className='sobesTable-count'>{ sobes.count_questions }</span>
        <span className='sobesTable-avg'>{ sobes.average_score }</span>
        <span className='sobesTable-status'>{ sobes.status }</span>
      </div>
    )
  }

  function sobesSectionButtonAdd() {
    return (
      <a href='#' className='sobesSection-button-add'>+</a>
    )
  }

  function sobesSection(sobeses) {
    return (
      <div className='sobes-section'>
        { sobesTableTitle() }
        <div className='sobesTable-container'>
          { sobeses.map((sobes, index) =>
            <SobesContainer key={sobes.id} sobes={sobes} index={index}  />
          )}
        </div>
      </div>
    )
  }
  
  return (
    <div className='SobesPage'>
      { sobesSection(sobeses) }
      { sobesSectionButtonAdd() }
    </div>
  )
}


