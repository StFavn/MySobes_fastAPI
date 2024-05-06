export default function QuestionModal({ question, closeQuestionModal }) {
  return (
    <div className="question-modal">
      <div className="question-modal-content">
        <a  href="#" className="close-question-modal-button" onClick={closeQuestionModal}>&times;</a>
        <p>Вопрос: {question.question}</p>
        <p>Ответ: {question.answer}</p>
      </div>
    </div>
  )
}