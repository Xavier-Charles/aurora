import "./App.css";
import { useEffect, useState } from "react";

function App() {
    useEffect(() => {
        handleRefresh();
    }, []);

    const handleRefresh = () => {
        setLoading(true);
        fetch("https://tranquil-tor-92195.herokuapp.com/ethPrice/")
            .then((response) => response.json())
            .then((data) => setPrice(data.data.price));
        fetch("https://tranquil-tor-92195.herokuapp.com/article/")
            .then((response) => response.json())
            .then((data) => {
              setArticle(data.data)
              setLoading(false)});
        fetch("https://tranquil-tor-92195.herokuapp.com/recentTx/")
            .then((response) => response.json())
            .then((data) => setValue(data.Ether_value));
    };

    const [price, setPrice] = useState(["..."]);
    const [article, setArticle] = useState([]);
    const [value, setValue] = useState(["..."]);
    const [loading, setLoading] = useState(true);

    return (
        <div className="App" style={{margin: "0 5%"}}>
            <h2>Current Ethereum Price</h2>
            <h3>{price}</h3>
            <button onClick={handleRefresh}>{loading? "Getting...": "Refresh"}</button>
            <h2>Recent Crypto Articles</h2>
            {article.map((e, i) => {
                let a = e.description.lastIndexOf(".");
                return (
                    <a key={i}>
                        <h3>{e.title}</h3>
                        <p>{e.description}</p>
                        <a href={e.link}>Read the Full story</a>
                    </a>
                );
            })}
            <br />
            <br />
            <h2>Recent Ethereum Transaction Value</h2>
            <h3>{value}</h3>
        </div>
    );
}

export default App;
