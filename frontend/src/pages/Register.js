import React, {useState} from 'react';
import {Navigate} from "react-router-dom";


const Register = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [redirect, setRedirect] = useState(false);

    const submit = async (e) => {
        e.preventDefault();

        await fetch('http://127.0.0.1:8000/LoginAPI/register', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                email,
                password
            })
        });

        setRedirect(true);
    }

    if (redirect){
        return <Navigate to="/login"/>
    }

    return (
        <form onSubmit={submit} class="center">
            <h1 className="h3 mb-3 fw-normal">Register</h1>

            <div className="form-floating">
              <input type="email" className="form-control" onChange={e =>setEmail(e.target.value)}/>
                <label htmlFor="floatingInput">Email address</label>
            </div>
            <div className="form-floating">
              <input type="password" className="form-control" onChange={e =>setPassword(e.target.value)}/>
                <label htmlFor="floatingPassword">Password</label>
            </div>

            <button className="w-100 btn btn-lg btn-primary" type="submit">Register</button>
        </form>
    );
};

export default Register;