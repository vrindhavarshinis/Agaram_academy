import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom';
import { useState } from 'react';
import Create from './Users/Create';
import List from './Users/List';
import View from './Users/View';
import Edit from './Users/Edit';




function App() {
const [users,setUsers]=useState([]);
  return (
    <div className="App">
      <header className="App-header">
       <Router>
        <Routes>
          <Route path='/user/create' element={<Create  users={users} setUsers={setUsers}/>}/>
          <Route path='/users' element={<List users={users}  setUsers={setUsers}/>}/>
          <Route path='/user/view/:name' element={<View users={users}/>}/>
          <Route path='/user/edit/:name' element={<Edit  users={users} setUsers={setUsers}/>}/>
        </Routes>
       </Router>
      </header>
    </div>
  );
}

export default App;
