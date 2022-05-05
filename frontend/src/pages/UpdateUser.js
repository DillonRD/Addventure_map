import React, {useEffect, useState} from 'react';
import {Navigate} from "react-router-dom";


const UpdateUser = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [firstname, setFirstname] = useState('');
    const [lastname, setLastname] = useState('');
    const [dateOfBirth, setDateOfBirth] = useState('');
    const [phone, setPhone] = useState('');
    const [address, setAddress] = useState('');
    const [city, setCity] = useState('');
    const [zipcode, setZipcode] = useState('');
    const [redirect, setRedirect] = useState(false);

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://127.0.0.1:8000/LoginAPI/user', {
                    headers: {'Content-Type': 'application/json'},
                    credentials: 'include',
                });

                const content = await response.json();
                setEmail(content.email)
                setFirstname(content.firstname)
                setLastname(content.lastname)
                setDateOfBirth(content.dateOfBirth)
                setPhone(content.phone)
                setAddress(content.address)
                setCity(content.city)
                setZipcode(content.zipcode)
            }
        )();
    }, []);

    const submit = async (e) => {
        e.preventDefault();

        await fetch('http://127.0.0.1:8000/LoginAPI/update', {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',
            body: JSON.stringify({
                email,
                password,
                firstname,
                lastname,
                dateOfBirth,
                phone,
                address,
                city,
                zipcode
            })
        });

        setRedirect(true);
    }

    if (redirect){
        return <Navigate to="/"/>
    }

    return (
        <form onSubmit={submit} class="center">
            <h1 className="h3 mb-3 fw-normal">Update Profile</h1>

            <div className="form-floating">
              <input type="email" className="form-control"  value={email} onChange={e =>setEmail(e.target.value)}/>
                <label htmlFor="floatingInput">Email address</label>
            </div>
            <div className="form-floating">
              <input type="password" className="form-control" placeholder="Password" onChange={e =>setPassword(e.target.value)}/>
                <label htmlFor="floatingPassword">Password</label>
            </div>
            <div className="form-floating">
              <input type="text" className="form-control" value={firstname} onChange={e =>setFirstname(e.target.value)}/>
                <label htmlFor="floatingInput">Firstname</label>
            </div>
            <div className="form-floating">
              <input type="text" className="form-control" value={lastname} onChange={e =>setLastname(e.target.value)}/>
                <label htmlFor="floatingPassword">Lastname</label>
            </div>
            <div className="form-floating">
              <input type="date" className="form-control" value={dateOfBirth} onChange={e =>setDateOfBirth(e.target.value)}/>
                <label htmlFor="floatingInput">DateOfBirth</label>
            </div>
            <div className="form-floating">
              <input type="text" className="form-control" value={phone} onChange={e =>setPhone(e.target.value)}/>
                <label htmlFor="floatingInput">Phone</label>
            </div>
            <div className="form-floating">
              <input type="text" className="form-control" value={address} onChange={e =>setAddress(e.target.value)}/>
                <label htmlFor="floatingInput">Address</label>
            </div>
            <div className="form-floating">
              <input type="text" className="form-control" value={city} onChange={e =>setCity(e.target.value)}/>
                <label htmlFor="floatingInput">City</label>
            </div>
            <div className="form-floating">
              <input type="text" className="form-control" value={zipcode} onChange={e =>setZipcode(e.target.value)}/>
                <label htmlFor="floatingInput">Zipcode</label>
            </div>

            <button className="w-100 btn btn-lg btn-primary" type="submit">Update</button>
        </form>
    );
};


export default UpdateUser;