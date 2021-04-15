import './App.css';
import {useEffect, useState} from 'react'


function App() {

  useEffect(() => {
    fetch("https://tranquil-tor-92195.herokuapp.com/ethPrice/")
        .then((response) => response.json())
        .then((data) => console.log(data));
    fetch("https://tranquil-tor-92195.herokuapp.com/article/")
        .then((response) => response.json())
        .then((data) => setArticle(data.data));
    fetch("https://tranquil-tor-92195.herokuapp.com/recentTx/")
        .then((response) => response.json())
        .then((data) => console.log(data));
  }, [])

  const [price, setPrice] = useState(["..."]);
  const [article, setArticle] = useState([]);
  const [value, setValue] = useState(["..."]);

  return (
      <div className="App">
          <h2>Current Ethereum Price</h2>
          <h3>{price}</h3>
          <h2>Recent Crypto Articles</h2>
          {article.map((e, i) => {
            let a = e.description.lastIndexOf(".");
            return (
                <a key={i}>
                    <h3>{e.title}</h3>
                    <p>{e.description.slice(0, a + 1)}</p>
                    <a>{e.description.slice(a+2)}</a>
                </a>
            );})}
          <br />
          <br />
          <h2>Recent Ethereum Transaction Value</h2>
          <h3>{value}</h3>
      </div>
  );
}

export default App;
