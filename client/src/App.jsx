import Header from "./components/Header"

import { Routes, Route} from "react-router-dom"

import QuestionsPage from "./pages/QuestionPage/QuestionsPage"
import SobesesPage from "./pages/SobesesPage"
import AboutPage from "./pages/AboutPage"
import HomePage from "./pages/HomePage"
import NotfoundPage from "./pages/NotfoundPage"

export default function App() {
  return (
    <>
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/questions" element={<QuestionsPage />} />
          <Route path="/sobeses" element={<SobesesPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="*" element={<NotfoundPage />} />
        </Routes>
      </main>
    </>
  )
}