import './App.css';
import Login from "./pages/Login";
import Home from "./pages/Home";
import Register from "./pages/Register";
import Nav from "./components/Nav";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import {useEffect, useState} from "react";
import UpdateUser from "./pages/UpdateUser";

function App() {
    const [id, setId] = useState('');

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://127.0.0.1:8000/LoginAPI/user', {
                    headers: {'Content-Type': 'application/json'},
                    credentials: 'include',
                });

                const content = await response.json();
                setId(content.id);
            }
        )();
    }, []);

    // catch the errors and show a error and redirect to the same page to try again
    // figure out how to get the change password working

    return (
        <div className="App">
            <BrowserRouter>
                <Nav id={id} setId={setId}/>

                <main className="form-signin">
                    <Routes>
                        <Route path="/" element={<Home id={id}/>}/>
                        <Route path="/login" element={<Login setId={setId}/>}/>
                        <Route path="/register" element={<Register />}/>
                         <Route path="/UpdateUser" element={<UpdateUser />}/>
                    </Routes>
                </main>
            </BrowserRouter>
        </div>
    );
}

export default App;
