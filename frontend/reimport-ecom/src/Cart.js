import React from 'react';

function Cart({ cartItems, removeFromCart }) {
  const totalPrice = cartItems.reduce((total, item) => total + item.price, 0);

  return (
    <div className="cart-container">
      <div className="cart-items">
        <h2>Cart</h2>
        {cartItems.map((item) => (
          <div key={item.cartId} className="cart-item">
            <div className="cart-item-details">
              <img src={item.imageUrl} alt={item.name} />
              <div className="cart-item-info">
                <h4>{item.name}</h4>
              </div>
            </div>
            <div className="cart-item-actions">
              <span className="cart-item-price">${item.price}</span>
              <button onClick={() => removeFromCart(item.cartId)}>Remove</button>
            </div>
          </div>
        ))}
      </div>

      <div className="cart-summary">
        <h3>Total: ${totalPrice.toFixed(2)}</h3>
        <button className="checkout-button">Checkout</button>
      </div>
    </div>
  );
}

export default Cart;
