import React, { useState, useEffect } from 'react';
import Product from './Product';

function ProductList({ addToCart }) {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/products')
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => setProducts(data.products))
      .catch(error => console.error('There has been a problem with your fetch operation:', error));
  }, []);

  return (
    <div className="products-grid">
      {products.map(product => (
        <Product key={product.id} product={product} addToCart={addToCart} />
      ))}
    </div>
  );
}

export default ProductList;
