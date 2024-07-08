import { useState } from 'react'
import Content from './components/content/content'
import Navbar from './components/navbar'
import './App.css'

function App() {

  return (
    <>
      <Navbar/>
      <div className='container mt-2'>
      <Content/>
      </div>
    </>
  )
}

export default App
