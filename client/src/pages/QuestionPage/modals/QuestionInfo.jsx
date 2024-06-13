import '../styles/modals/QuestionInfo.css'

export default function QuestionModal({ question, closeQuestionModal }) {
  const handleOverlayClick = (event) => {
    // Проверяем, что клик был именно на затемненной области
    if (event.target.classList.contains('questionInfo-modal')) {
      // Закрываем модальное окно
      closeQuestionModal();
    }
  }

  return (
    <div className="questionInfo-modal" onClick={handleOverlayClick}>
      <div className="questionInfo-content">
        <a  href="#" className="questionInfo-button-close" onClick={closeQuestionModal}>&times;</a>
        <div className="questionInfo-question">
          <span>{question.question}</span>
        </div>
        <div className="questionInfo-answer">
          <span>{question.answer}</span>
        </div>
      </div>
    </div>
  )
}