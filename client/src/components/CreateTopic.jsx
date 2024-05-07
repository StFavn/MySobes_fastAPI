export default function CreateTopic({ topics }) {
  return (
    <div className="addItem-selected-content">
      <div className="select-parent">
        {topics.map((topic) => (
          <>
            <input type="radio" id={topic.id} name="parent" />
            <label htmlFor={topic.id}>{topic.name}</label>
          </>
        ))}
      </div>
    </div>
  );
}


// function TreeParentMenu({ topic }) {
//   return (
//     <>
//       {topic.children.map((child) => (
//         <TopicTree key={child.id} topic={child} />
//       ))}
//     </>
//   )
// }