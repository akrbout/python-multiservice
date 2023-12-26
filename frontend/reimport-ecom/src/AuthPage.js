import React, { useState } from 'react';
import './AuthPage.css';

function AuthPage() {
  const [isSignIn, setIsSignIn] = useState(true);

  return (
    <div className="auth-page">
      <div className={isSignIn ? "auth-tab active" : "auth-tab"} onClick={() => setIsSignIn(true)}>
        SIGN IN
      </div>
      <div className={!isSignIn ? "auth-tab active" : "auth-tab"} onClick={() => setIsSignIn(false)}>
        SIGN UP
      </div>
      {isSignIn ? <SignInForm /> : <SignUpForm />}
    </div>
  );
}

function SignInForm() {
  // Форма для входа (пример поля ниже)
  return (
    <form className="auth-form">
      <input type="email" className="auth-form-field" placeholder="Email" required />
      <input type="password" className="auth-form-field" placeholder="Password" required />
      <button type="submit" className="auth-form-action">Sign In</button>
      {/*<div className="auth-form-footer">*/}
      {/*  <a>Forgot Password?</a>*/}
      {/*</div>*/}
    </form>
  );
}

function SignUpForm() {
  // Форма для регистрации (аналогично SignInForm)
    return (
    <form className="auth-form">
      <input type="email" className="auth-form-field" placeholder="Email" required />
      <input type="password" className="auth-form-field" placeholder="Password" required />
      <button type="submit" className="auth-form-action">Sign In</button>
      {/*<div className="auth-form-footer">*/}
      {/*  <a>Forgot Password?</a>*/}
      {/*</div>*/}
    </form>
  );
}

export default AuthPage;
