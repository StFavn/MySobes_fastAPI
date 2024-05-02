import { NavLink } from "react-router-dom"

export default function Header() {
  return (
    <header>
      <NavLink to="/">Главная</NavLink>
      <NavLink to="/questions">Вопросы</NavLink>
      <NavLink to="/sobeses">Собесы</NavLink>
      <NavLink to="/about">Обо мне</NavLink>
    </header>
  )
}