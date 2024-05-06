import { useState } from 'react'

export default function AddItemModal({ topic_list, closeAddItemModal }) {
  const [addItemType, setAddItemType] = useState("Topic");

  function SelectMenu() {
    return (
      <div className="select-menu-add-item-modal">
        <select value={addItemType} onChange={(e) => setAddItemType(e.target.value)}>
          <option value="Topic">Create Topic</option>
          <option value="Question">Create Question</option>
        </select>
      </div>
    )
  }

  function AddTopic(topic_list) {
    return (
      <div>{ topic_list }</div>
    )
  }

  function AddQuestion(topic_list) {
    return (
      <div>Add Question Section</div>
    )
  }
  
  return (
    <div className="add-item-modal">
      <a href="#" className="close-question-modal-button" onClick={closeQuestionModal}>&times;</a>
      {SelectMenu()}
      {addItemType === "Topic" ? <AddTopic topic_list={topic_list}/> : <AddQuestion topic_list={topic_list}/>}
    </div>
  )
}
