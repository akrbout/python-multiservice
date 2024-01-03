// import React from 'react';
//
// const GoodsPage = () => {
//   const goods = [
//     { id: 1, name: 'Product 1', price: 10 },
//     { id: 2, name: 'Product 2', price: 20 },
//     // Add more products here
//   ];
//   const addToCart = (product) => {
//   let cart = JSON.parse(localStorage.getItem('cart')) || [];
//   let found = cart.find(item => item.id === product.id);
//
//   if (found) {
//     found.quantity += 1;
//   } else {
//     cart.push({ ...product, quantity: 1 });
//   }
//
//   localStorage.setItem('cart', JSON.stringify(cart));
//   alert(`${product.name} added to cart`);
// };
//
//   return (
//       <div className="container">
//         <h1>Goods</h1>
//         <ul>
//           {goods.map(item => (
//               <li className="card" key={item.id}>
//                 <h3>{item.name}</h3>
//                 <p>${item.price}</p>
//                 <button className="button" onClick={() => addToCart(item)}>Add to Cart</button>
//               </li>
//           ))}
//         </ul>
//       </div>
//
//   );
// };
//
// export default GoodsPage;

import React from 'react';
import { useState, useEffect } from "react";

const GoodsPage = () => {
  // Mocked products data
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('http://localhost:8000/products');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setProducts(data.products);
      } catch (error) {
        console.error("Fetching products failed:", error);
        setError(error.message);
      }
    };

    fetchProducts();
  }, []); // The empty array means this effect runs once on mount

  // ... (rest of your component, including rendering the products)

  if (error) {
    return <div>Error fetching products: {error}</div>;
  }

  const addToCart = (product) => {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const existingProduct = cart.find(item => item.id === product.id);
    if (existingProduct) {
      existingProduct.quantity += 1;
    } else {
      cart.push({ ...product, quantity: 1 });
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    // Add additional feedback for the user if needed, e.g., a confirmation message
  };

  // Function to truncate the description to the first 40 characters
  const truncateDescription = (description) => {
    return description.length > 40 ? description.substring(0, 40) + '...' : description;
  };

  return (
    <div className="goods-page">
      <div className="cards-container">
        {products.map(product => (
          <div key={product.id} className="product-card">
            <img src={product.imageUrl} alt={product.name} className="product-image" />
            <h3 className="product-name">{product.name}</h3>
            <p className="product-price">${product.price}</p>
            <p className="product-description">{truncateDescription(product.description)}</p>
            <button onClick={() => addToCart(product)} className="add-to-cart-button">
              Add to Cart
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GoodsPage;
