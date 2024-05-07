export default function CreateQuestion({ topics }) {
  return (
    <div className="create-question-block">
      <p>Add Question Section</p>
      <ul>
        {topics.map((topic) => (
          <li key={topic.id}>{topic.name}</li>
        ))}
      </ul>
    </div>
  );
}