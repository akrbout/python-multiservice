// import React, { useState, useEffect } from 'react';
// import Cookies from 'js-cookie';
// import { jwtDecode } from 'jwt-decode';
//
// const ProfilePage = () => {
//   const [user, setUser] = useState({
//     profilePhoto: '',
//     fullName: '',
//     email: '',
//     phone: '',
//     orders: []
//   });
//   const [isAuthorized, setIsAuthorized] = useState(true);
//
//   useEffect(() => {
//       const token = Cookies.get('jwtToken');
//       if (token) {
//           setIsAuthorized(true);
//           const decodedToken = jwtDecode(token);
//           const userData = {
//               profilePhoto: decodedToken.profilePhoto,
//               fullName: decodedToken.fullName,
//               email: decodedToken.email,
//               phone: decodedToken.phone,
//               orders: []
//           }
//           setUser(userData);
//       } else {
//           setIsAuthorized(false)
//           const userData = {
//               profilePhoto: '/path-to-profile-photo.jpg',
//               fullName: 'John Doe',
//               email: 'john.doe@example.com',
//               phone: '+1234567890',
//               orders: []
//           };
//           setUser(userData);
//       }
//   }, []);
//
//   const logOutFromProfile = () => {
//       Cookies.remove('jwtToken');
//       setIsAuthorized(false);
//   };
//
//   if (!isAuthorized) {
//     return (
//       <div className="auth-popup">
//         <h2>Please Log In</h2>
//         <button onClick={() => setIsAuthorized(true)}>Log In</button>
//       </div>
//     );
//   }
//
//   return (
//       <div className={`profile-page ${!isAuthorized ? 'blurred' : ''}`}>
//           <div className="profile-header">
//               <img src={user.profilePhoto} alt="Profile"/>
//           </div>
//           <div className="profile-information">
//               <h1>{user.fullName}</h1>
//               <p>Email: {user.email}</p>
//               <p>Phone: {user.phone}</p>
//               <button onClick={logOutFromProfile}>Log Out</button>
//               <div className="order-history">
//                   <h2>Your Orders</h2>
//                   <div className="orders-list">
//                       {user.orders.length > 0 ? (
//                           user.orders.map((order, index) => (
//                               <div key={index} className="order-item">
//                                   <p>Order ID: {order.id}</p>
//                                   <p>Order Date: {order.date}</p>
//                                   <p>Total: ${order.total}</p>
//                                   <p>Goods: {order.goods}</p>
//                               </div>
//                           ))
//                       ) : (
//                           <p>You have no orders.</p>
//                       )}
//                   </div>
//               </div>
//           </div>
//       </div>
//   );
// };
//
// export default ProfilePage;

import './ProfilePage.css'; // Make sure to create a ProfilePage.css file for the styles
import React, { useState, useEffect } from 'react';
import Cookies from 'js-cookie';
import { jwtDecode } from 'jwt-decode';

const ProfilePage = () => {
  // State for profile info, replace with your state management logic
  const [profile, setUser] = useState({
    username: 'username',
    firstName: 'Valerie',
    lastName: 'Luna',
    organization: 'Start Bootstrap',
    location: 'San Francisco, CA',
    email: 'name@example.com',
    phoneNumber: '555-123-4567',
    birthday: '06/10/1988',
  });

  const [orders, setOrders] = useState([
    { id: 1, date: '2023-01-01', total: 99.99, status: 'Shipped' },
    { id: 2, date: '2023-02-15', total: 79.49, status: 'Delivered' },
    // ... other orders
  ]);

  const [isAuthorized, setIsAuthorized] = useState(true);

  // Handler for profile image upload, replace with your logic
  const handleProfileImageUpload = (event) => {
    console.log('Uploaded image', event.target.files[0]);
    // Process the image upload here
  };

  // Handler for saving changes, replace with your logic
  const handleSaveChanges = () => {
    console.log('Save profile changes');
    // Save the profile changes here
  };

  useEffect(() => {
      const token = Cookies.get('jwtToken');
      if (token) {
          setIsAuthorized(true);
          const decodedToken = jwtDecode(token);
          const userData = {
              profilePhoto: decodedToken.profilePhoto,
              fullName: decodedToken.fullName,
              email: decodedToken.email,
              phone: decodedToken.phone,
              orders: []
          }
          setUser(userData);
      } else {
          setIsAuthorized(false)
          const userData = {
              profilePhoto: '/path-to-profile-photo.jpg',
              fullName: 'John Doe',
              email: 'john.doe@example.com',
              phone: '+1234567890',
              orders: []
          };
          setUser(userData);
      }
  }, []);

  const logOutFromProfile = () => {
      Cookies.remove('jwtToken');
      setIsAuthorized(false);
  };

  if (!isAuthorized) {
    return (
      <div className="auth-popup">
        <h2>Please Log In</h2>
        <button onClick={() => setIsAuthorized(true)}>Log In</button>
      </div>
    );
  }

  return (
      <div className="profile-page-wrapper">
          <div className="profile-container">
              <div className="profile-sidebar">
                  <h3>Profile Picture</h3>
                  <img src="/path-to-profile-image.jpg" alt="Profile" className="profile-picture"/>
                  <p>JPG or PNG no larger than 5 MB</p>
                  <input type="file" onChange={handleProfileImageUpload} className="upload-button"/>
              </div>
              <div className="profile-content">
                  <h3>Account Details</h3>
                  <form className="profile-form">
                      <input type="text" value={profile.username} placeholder="Username"/>
                      <input type="text" value={profile.firstName} placeholder="First name"/>
                      <input type="text" value={profile.lastName} placeholder="Last name"/>
                      <input type="text" value={profile.organization} placeholder="Organization name"/>
                      <input type="text" value={profile.location} placeholder="Location"/>
                      <input type="email" value={profile.email} placeholder="Email address"/>
                      <input type="tel" value={profile.phoneNumber} placeholder="Phone number"/>
                      <button type="button" onClick={handleSaveChanges} className="save-changes-button">
                          Save changes
                      </button>
                  </form>
              </div>
          </div>
          <div className="orders-container">
              <h3>Your Orders</h3>
              <div className="orders-list">
                  {orders.map((order) => (
                      <div key={order.id} className="order-card">
                          <div className="order-details">
                              <p><strong>Order ID:</strong> {order.id}</p>
                              <p><strong>Date:</strong> {order.date}</p>
                              <p><strong>Total:</strong> ${order.total}</p>
                              <p><strong>Status:</strong> {order.status}</p>
                          </div>
                      </div>
                  ))}
              </div>
          </div>
      </div>
  );
};

export default ProfilePage;
