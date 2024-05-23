import '../styles/Message.css'

export default function Message({ message }) {
  return (
    <div className="message">
      <span>{message}</span>
      <a href="#" class="close-button">&times;</a>
    </div>
  );
}
