import React from 'react';

function Product({ product, addToCart }) {
  return (
    <div className="product-card">
      <img src={product.imageUrl} alt={product.name} />
      <h3 className="product-name">{product.name}</h3>
      <p className="product-price">${product.price}</p>
      <button onClick={() => addToCart(product)}>Add to Cart</button>
    </div>
  );
}

export default Product;
