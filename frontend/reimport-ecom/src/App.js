import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import GoodsPage from './components/GoodsPage';
import Cart from './components/Cart';
import ProfilePage from './components/ProfilePage';

function App() {
  return (
    <Router>
      <Navbar />
        <Routes>
          <Route path="/" element={<GoodsPage />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
    </Router>
  );
}

export default App;
