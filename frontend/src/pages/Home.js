import React, {useEffect, useState} from 'react';

const Home = (props) => {

    /*
    const [id, setId] = useState('');
    const [email, setEmail] = useState('');

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://127.0.0.1:8000/LoginAPI/user', {
                    method: 'GET',
                    headers: {'Content-Type': 'application/json'},
                    credentials: 'include',
                });

                const content = await response.json();
                setId(content.id)
                setEmail(content.email)
            }
        )();
    });

    {id ? 'Your id is ' + id : 'You need to login'}<br/>
    {email ? 'Your email is ' + email : 'You need to login'}

     */

    return (
        <div>
            {props.id ? 'Your id is ' + props.id : 'You are not logged in'}
        </div>
    );
};

export default Home;