import './App.css';
import axios from 'axios';
import {useState, useEffect} from 'react';


function App() {
  const [people, setPeople] = useState([]);
  useEffect(() => {
    axios.get('http://localhost:8000/api').then(res => setPeople(res.data))
    .catch(err => console.error(err));
  }, []);

  return people.map((p, index) => {
    return <p key={index}>{p.id} {p.name} {p.age}</p>
  });

}

export default App;
