import React from 'react';

function Navbar() {
  const navbarStyle = {
    backgroundColor: '#997950', // warna coklat yang diinginkan
  };

  return (
    <nav className="navbar navbar-expand-lg" style={navbarStyle}>
      <div className="container-fluid">
        <a className="navbar-brand text-white" href="#">ZAL KAFE </a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarText">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <a className="nav-link active text-white" aria-current="page" href="#">Home</a>
            </li>
            <li className="nav-item text-white">
              <a className="nav-link text-white" href="#">Features</a>
            </li>
            <li className="nav-item text-white">
              <a className="nav-link text-white" href="#">Pricing</a>
            </li>
          </ul>
          <span className="navbar-text text-white">
            HAlo Selamat datang Para-Penikmat cafe pesera KKN
          </span>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
