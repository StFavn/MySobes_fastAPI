import '../styles/Message.css'

export default function Message({ message }) {
  return (
    <div className="message">
      <p>{message}</p>
    </div>
  );
}
