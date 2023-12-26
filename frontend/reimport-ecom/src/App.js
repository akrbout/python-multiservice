import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';
import ProductList from './ProductList';
import Cart from './Cart';
import './App.css';
import './AuthPage';
import AuthPage from "./AuthPage";

function App() {
  const [cartItems, setCartItems] = useState([]);
  const cartItemCount = cartItems.length;

  const addToCart = (product) => {
    const cartItem = {...product, cartId: uuidv4()};
    const newCartItems = [...cartItems, cartItem];
    setCartItems(newCartItems);
    localStorage.setItem('cartItems', JSON.stringify(newCartItems));
  };

  const removeFromCart = (cartIdToRemove) => {
    const newCartItems = cartItems.filter(item => item.cartId !== cartIdToRemove);
    setCartItems(newCartItems);
    localStorage.setItem('cartItems', JSON.stringify(newCartItems));
  };

  useEffect(() => {
    const storedCartItems = localStorage.getItem('cartItems');
    if (storedCartItems) {
      setCartItems(JSON.parse(storedCartItems));
    }
  }, []);

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <div className="nav-left">
              <li>
                <Link to="/">Home</Link>
              </li>
              <li className="cart-menu">
                <Link to="/cart">
                  Cart <span className="cart-count">{cartItemCount}</span>
                </Link>
              </li>
            </div>
            <div className="nav-right">
              <li>
                <Link className="last-item" to="/auth">Auth/Register</Link>
              </li>
            </div>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container">
              <ProductList addToCart={addToCart}/>
            </div>
          }/>
          <Route path="/cart" element={
            <div className="container">
              <Cart cartItems={cartItems} removeFromCart={removeFromCart}/>
            </div>
          }/>
          <Route path="/auth" element={
            <div className="container">
              <AuthPage/>
            </div>
          }/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
