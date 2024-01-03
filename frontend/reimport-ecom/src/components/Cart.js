import React, { useState, useEffect } from 'react';

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    loadCartItems();
  }, []);

  const loadCartItems = () => {
    let items = JSON.parse(localStorage.getItem('cart')) || [];
    setCartItems(items);
  };

  const updateQuantity = (id, newQuantity) => {
    let updatedCart = cartItems.map(item => {
      if (item.id === id) {
        return { ...item, quantity: newQuantity };
      }
      return item;
    }).filter(item => item.quantity > 0);

    setCartItems(updatedCart);
    localStorage.setItem('cart', JSON.stringify(updatedCart));
  };

  const incrementQuantity = (id) => {
    updateQuantity(id, cartItems.find(item => item.id === id).quantity + 1);
  };

  const decrementQuantity = (id) => {
    updateQuantity(id, cartItems.find(item => item.id === id).quantity - 1);
  };

  return (
    <div className="container">
      <h1>Shopping Cart</h1>
      <ul>
        {cartItems.map((item, index) => (
            <li className="card" key={index}>
              <h3>{item.name}</h3>
              <h4>Total price: <p>{item.price * item.quantity}</p></h4>
              <h4>Quantity: <p>{item.quantity}</p></h4>
              <div className="quantity-selector">
                <button onClick={() => decrementQuantity(item.id)}>-</button>
                <input type="text" value={item.quantity} readOnly/>
                <button onClick={() => incrementQuantity(item.id)}>+</button>
                <button className="delete-button" onClick={() => updateQuantity(item.id, 0)}>Remove</button>
              </div>
              {/*<button onClick={() => updateQuantity(item.id, 0)}>Remove</button>*/}
            </li>
        ))}
      </ul>
      {cartItems.length === 0 && <p>Your cart is empty.</p>}
    </div>
  );
};

export default Cart;
