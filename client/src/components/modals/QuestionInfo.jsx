import '../../styles/modals/QuestionInfo.css'

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
        <a  href="#" className="close-questionInfo-button" onClick={closeQuestionModal}>&times;</a>
        <p>Вопрос: {question.question}</p>
        <p>Ответ: {question.answer}</p>
      </div>
    </div>
  )
}