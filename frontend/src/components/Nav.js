import React from 'react';
import {Link} from "react-router-dom";

const Nav = (props) => {

    const logout = async () => {
        await fetch('http://127.0.0.1:8000/LoginAPI/logout', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',
        });

        props.setId('');
    }

    let navbarMenu;

    if (props.id === '' || props.id === undefined){
        navbarMenu = (
            <ul className="navbar-nav me-auto mb-2 mb-md-0">
                <li className="nav-item">
                    <Link to="/login" className="navbar-brand">Login</Link>
                </li>
                <li className="nav-item">
                    <Link to="/register" className="navbar-brand">Register</Link>
                </li>
            </ul>
        )
    } else {
        navbarMenu = (
            <ul className="navbar-nav me-auto mb-2 mb-md-0">
                <li className="nav-item">
                    <Link to="/login" className="navbar-brand" onClick={logout} >Logout</Link>
                </li>
                <li className="nav-item">
                    <Link to="/UpdateUser" className="navbar-brand" >Profile</Link>
                </li>
            </ul>
        )
    }

    return (
        <nav className="navbar navbar-expand-md navbar-dark bg-dark mb-4">
            <div className="container-fluid">
                 <Link to="/" className="navbar-brand">Home</Link>

                <div>
                    {navbarMenu}
                </div>
            </div>
        </nav>
    );
};

export default Nav;