import { useState } from 'react'
import CreateTopicComponent from '../CreateTopic'
import CreateQuestionComponent from '../CreateQuestion'

import '../../styles/modals/AddItem.css'

export default function AddItemModal({ topics, closeAddItemModal }) {
  const [addItemType, setAddItemType] = useState("Topic");

  function SelectMenu() {
    return (
      <div className="addItem-select">
        <input type="radio" id="tab1" name="tabs" checked={addItemType === "Topic"} onChange={() => setAddItemType("Topic")} />
        <label className="addItem-select-topic" htmlFor="tab1">Create Topic</label>
        <input type="radio" id="tab2" name="tabs" checked={addItemType === "Question"} onChange={() => setAddItemType("Question")} />
        <label className="addItem-select-question" htmlFor="tab2">Create Question</label>
      </div>
    )
  }
  
  return (
    <div className="addItem-modal">
      <div className="addItem-content">
        <a href="#" className="close-addItem-button" onClick={ closeAddItemModal }>&times;</a>
        {SelectMenu()}
        {addItemType === "Topic" && <CreateTopicComponent topics={topics} />}
        {addItemType === "Question" && <CreateQuestionComponent topics={topics} />}
      </div>
    </div>
  )
}