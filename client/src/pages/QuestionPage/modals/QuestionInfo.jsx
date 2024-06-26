import '../styles/modals/QuestionInfo.css'

export default function QuestionModal({ question, closeQuestionModal }) {
  const handleOverlayClick = (event) => {
    const isClickOnDarkArea = event.target.classList.contains('questionInfo-modal');
    if (isClickOnDarkArea) closeQuestionModal();
  }

  return (
    <div className="questionInfo-modal" onClick={handleOverlayClick}>
      <div className="questionInfo-content">
        <a  href="#" className="questionInfo-button-close" onClick={closeQuestionModal}>&times;</a>
        <div className="questionInfo-question">
          <pre>{question.question}</pre>
        </div>
        <div className="questionInfo-answer">
          <span>{question.answer}</span>
        </div>
      </div>
    </div>
  )
}