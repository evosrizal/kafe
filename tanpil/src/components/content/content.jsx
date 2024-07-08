import React, { useEffect, useState } from 'react';

function Content() {
  const [menuItems, setMenuItems] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/menu/')
      .then(response => response.json())
      .then(data => setMenuItems(data));
  }, []);

  return (
    <div className="row row-cols-1 row-cols-md-2 g-4">
    {menuItems.map(item => (
      <div key={item.id} className="col">
        <div className='card bg-info-subtle' >
          <div className='card-body'>
            <div className='card-title'>{item.nama}</div>
            <div className='card-text'>
              {item.deskripsi}
            </div>
            <div className='card-text'>
              Harga: {item.harga}
            </div>
            <div className='card-text'>
              Kategori: {item.kategori}
            </div>
          </div>
        </div>
      </div>
    ))}
  </div>
  );
}

export default Content;
