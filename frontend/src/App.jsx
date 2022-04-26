import './App.css';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom"
import Header from './components/Header'
import NotesListPage from './pages/NotesListPage'
import NotePage from './pages/NotePage'

function App() {
  return (
    <BrowserRouter>
    <div className="container dark">
      <div className="app">
      <Header />
      <Routes>
        <Route path="/" exact element={<NotesListPage />} />
        <Route path="/note/:noteId" element={<NotePage />} />
      </Routes>
      </div>
    </div>

    </BrowserRouter>
  );
}

export default App;
